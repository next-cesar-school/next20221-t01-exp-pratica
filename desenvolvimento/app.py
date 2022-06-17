import os
from pathlib import Path

import flask
from flask import Flask, request

from actions import register_document, remove_document
from requirements import there_are_images, there_is_token
from xlsx import extract_images

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def route_register():
    if 'file' not in request.files:
        return 'Error'
    file = request.files['file']
    file_bytes = file.read()
    try:
        list_images = extract_images(file_bytes)
    except:
        return {'Success': False, 'Error': 'The document may be corrupted or may be not a .XLSX'}
    if not there_are_images(list_images):
        return {'Success': False, 'Error': 'There are no images in the document'}
    return {'Success': True, 'ID': register_document(list_images)}

# Encontrar pontos que podem virar funções, pois têm vários pontos repetidos
@app.route('/recover_doc/<id_doc>', methods=['GET'])
def route_recover_doc(id_doc):
    if not there_is_token(id_doc):
        return {'Success': False, 'Error': 'This document does not exists'}
    doc = request.args.get(id_doc)
    if doc is not None:
        return {'Success': False, 'Error': 'This document does not exists'}
    path_dir = Path(Path.home(), id_doc)
    if not os.path.exists(path_dir):
        return {'Success': False, 'Error': 'This document does not exists'}
    #Tirar o ".png" do final (usar o map(função, lista))
    list_files = os.listdir(path_dir)
    return {'Success': True, 'Document ID': id_doc, 'Images': list_files}

@app.route('/recover_img/<id_img>', methods=['GET'])
def route_recover_img(id_img):
    if not there_is_token(id_img):
        return {'Success': False, 'Error': 'This image does not exists'}
    img = request.args.get(id_img)
    if img is not None:
        return {'Success': False, 'Error': 'This image does not exists'}
    id_img_split = id_img.split('_')
    id_doc = f'{id_img_split[0]}_{id_img_split[1]}'
    print(id_doc)
    path_dir = Path(Path.home(), id_doc, f'{id_img}.png')
    if not os.path.exists(path_dir):
        return {'Success': False, 'Error': 'This image does not exists'}
    return flask.send_file(path_dir, mimetype='image/png')

@app.route('/list_doc', methods=['GET'])
def route_list_doc():
    home_path = Path.home()
    list_files = os.listdir(home_path)
    dic_next = list(filter(there_is_token, list_files))
    return {'Success': True, 'List': dic_next}

@app.route('/delete/<id_doc>', methods=['DELETE'])
def route_delete(id_doc):
    if not there_is_token(id_doc):
        print(1)
        return {'Success': False, 'Error': 'This document does not exists'}
    if not os.path.exists(Path(Path.home(), id_doc)):
        print(2)
        return {'Success': False, 'Error': 'This document does not exists'}
    remove_document(id_doc)
    return {'Success': True, 'action': 'DELETE'}

if __name__ == '__main__':
    app.run()