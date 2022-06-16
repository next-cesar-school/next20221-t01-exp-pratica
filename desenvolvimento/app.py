from flask import Flask
from flask import request
from actions import register_document
from xlsx import extract_images
from actions import remove_document

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def route_register():
    if 'file' not in request.files:
        return 'Erro'
    file = request.files['file']
    file_bytes = file.read()
    list_images = extract_images(file_bytes)
    register_document(file, list_images)
    return "Rota cadastro"

@app.route('/recover_doc/<id_doc>', methods=['GET'])
def route_recover_doc(id_doc):
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