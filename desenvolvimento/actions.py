import os
from fileinput import filename
from pathlib import Path
from utils import create_dir, save_image, generate_id_doc

def register_document (list_images):
    id_doc = generate_id_doc()
    path_dir = create_dir(id_doc)
    count_img = 0
    for img in list_images:
        name_image = f'{id_doc}_{count_img}'
        count_img += 1
        save_image(path_dir, img, name_image)
    #print(f'Document "{os.path.basename(file)}" registered!\nID_Document: {id_doc}\nDirectory: {path_dir}')
    return path_dir

def remove_document (dir_doc):
    #apagar a pasta que tem o id que representa o doc
    os.remove(dir_doc)
