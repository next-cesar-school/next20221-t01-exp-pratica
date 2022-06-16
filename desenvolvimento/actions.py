import os
from fileinput import filename
import datetime
from re import I

def register_document (file, list_images):
    id_doc = generate_id_doc
    
    #criar uma pasta que representa o documento e salvar as imagens dentro dessa pasta    
    print(f'Document "{filename(file)}" registered!\nID: {id_doc}')

def generate_id_doc ():
    now = datetime.datetime.now()
    return now.strftime("%m%d%Y%I%M%S%f")

def register_image (id_doc, count, image):
    #id_doc_count
    print(f'Image "{filename}" registered!')

def remove_document (id_doc):
    #apagar a pasta que tem o id que representa o doc
    os.remove(id_doc)
