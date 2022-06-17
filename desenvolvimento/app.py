from flask import Flask
from flask import request
from actions import register_document
from requirements import is_file
from requirements import there_are_images
from requirements import is_xlsx
from xlsx import extract_images
from actions import remove_document
import json
from pathlib import Path

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def route_register():
    if 'file' not in request.files:
        return 'Erro'
    file = request.files['file']
    #is_file (file) # Pq não está reconhecendo?
    #if is_xlsx(file) == False: # Como faz para reconhecer o tipo do arquivo como .xlsx?
        #return 'Type file invalid! It must be ".xlsx"'
    file_bytes = file.read()
    list_images = extract_images(file_bytes)
    #print(list_images) # Usar um print pra mostrar a imagem no retorno
    #there_are_images(list_images) # Pq não está pegando essa função?
    if not list_images:
        return 'There is no images in the document!'
    register_document(list_images)
    return "Rota cadastro"

@app.route('/recover_doc/<id_doc>', methods=['GET'])
def route_recover_doc(id_doc):
    doc = request.args.get(id_doc) # é melhor do que request.args[id_doc]
    
    '''document_dic = {
        'Document name' = 
        'ID' = id_doc
        'Number of images' = 
        'Document directory path' = 
    }
    doc_jason = json.dumps(document_dic)
    return doc_jason'''
    return "Rota recupera " + id_doc

@app.route('/recover_img/<id_img>', methods=['GET'])
def rota_recover_img(id_img):
    return "Rota recupera " + id_img

@app.route('/list_doc', methods=['GET'])
def route_list_doc():
    return "Rota lista doc"

@app.route('/delete/<id_doc>', methods=['DELETE'])
def route_delete(id_doc):
    delete_doc = remove_document(id_doc)
    return {'success': True, 'action': 'DELETE'}

if __name__ == '__main__':
    app.run()