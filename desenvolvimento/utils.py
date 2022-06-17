import datetime
import io
import os
from pathlib import Path

import PIL


def generate_id_doc ():
    now = datetime.datetime.now()
    return now.strftime("NExT_%m%d%Y%I%M%S%f")

def save_image(path_dir, img, name_image):
    #salvar a img no diretório da variável dir_doc
    image_str = io.BytesIO(img._data())
    image = PIL.Image.open(image_str)
    image.save(os.path.join(path_dir, f'{name_image}.png'))

def create_dir(id_doc):
    path_dir = Path(Path.home(), id_doc)
    os.mkdir(path_dir)
    return path_dir