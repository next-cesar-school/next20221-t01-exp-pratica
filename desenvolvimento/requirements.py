from pickle import EMPTY_LIST
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation
from pathlib import Path

def is_file (file):
    if not Path.is_file(file):
        return 'This is not a file!'

def is_xlsx (file):
    #extention = Path.suffix(file)
    #if extention != '.xlsx':
    if type(file) == 'werkzeug.datastructures.FileStorage':
        return True
    else:
        return False

def there_are_images (list_images):
    if not list_images:
        return 'There is no images in the document!'
    
    #count = 0
    #for _ in list_images:
        #count += 1
    #if count > 0:
        #return True
    #else:
        #return False

    #if list_images == False:
        #return False
    #else:
        #return True