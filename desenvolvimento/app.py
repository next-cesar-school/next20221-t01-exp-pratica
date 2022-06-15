from flask import Flask
from flask import request
from xlsx import extrair_imagens

app = Flask(__name__)

### apagar

#def extrair_imagens (arquivo):
    #print(arquivo)
    #print(type(arquivo))
    #planilha = openpyxl.load_workbook(arquivo)

### apagar

@app.route('/cadastro', methods=['POST'])
def rota_cadastro():
    if 'arquivo' not in request.files:
        return 'Erro'
    #content = request.files['file'].read()
    arquivo = request.files['arquivo'].read()
    print(arquivo)
    print(type(arquivo))
    extrair_imagens(arquivo)
    return type(arquivo)
    #return "Rota cadastro"

@app.route('/recupera_doc/<id_documento>', methods=['GET'])
def rota_recupera_doc(id_documento):
    return "Rota recupera " + id_documento

@app.route('/recupera_img/<id_imagem>', methods=['GET'])
def rota_recupera_img(id_imagem):
    return "Rota recupera " + id_imagem

@app.route('/lista_img', methods=['GET'])
def rota_lista_img():
    return "Rota lista img"

@app.route('/lista_doc', methods=['GET'])
def rota_lista_doc():
    return "Rota lista doc"

@app.route('/deletar/<id_documento>', methods=['DELETE'])
def rota_deletar(id_documento):
    return {'sucesso': True, 'acao': 'DELETAR'}

if __name__ == '__main__':
    app.run()