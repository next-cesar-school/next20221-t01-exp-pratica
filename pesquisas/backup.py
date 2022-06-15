from flask import Flask
from flask import request
from markupsafe import escape
app = Flask(__name__)

"""
GET (NAO TEM ALTERACAO DE ESTADO)
 - recuperar informacoes (documentos, imagens) ou listagens
 - R do CRUD

POST (TEM ALTERACAO DE ESTADO)
 - cadastro (inserir um registro no banco de dados que nao existe)
 - C do CRUD

DELETE (TEM ALTERACAO DE ESTADO)
 - delecao
 - D do CRUD

UPDATE - x
 - atualizacao de um registro no banco de dados que existe!
 - U do CRUD
"""


@app.route("/")  # PADRAO - GET
def hello_world():
    return {"sucesso": True}


@app.route("/deletar", methods=['DELETE'])  # PADRAO - GET
def deletar_item():
    return {"sucesso": True, "acao": "DELETAR"}


@app.route("/deletar_v2/<id_delecao>", methods=['DELETE'])  # PADRAO - GET
def deletar_item_v2(id_delecao):
    return {"sucesso": True, "acao": "DELETAR", "id": id_delecao}


@app.route("/overview", methods=['POST'])
def overview_parametros():
    print("=================================================")
    print("\ntype(request)")
    print(type(request))
    print("\nrequest")
    print(request)
    print("\nrequest.method")
    print(request.method)
    print("\nrequest.path")
    print(request.path)
    print("\nrequest.args")
    print(request.args)
    print("\nrequest.form")
    print(request.form)
    print("\nrequest.files")
    print(request.files)
    print("=================================================")

    return {"sucesso": True, "acao": "OVERVIEW"}