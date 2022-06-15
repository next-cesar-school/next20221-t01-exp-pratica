import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader
import openpyxl_image_loader

planilha = openpyxl.load_workbook('D:\\O QUE DEIXAR\\Cursos Online\\NExT\\Projeto Final NExT - T1\\F1_imagem.xlsx')
sheet = planilha.active
image_loader = SheetImageLoader(sheet)
cell_range = sheet['A1':'B40']

for row in cell_range:
    for cell in row:
        if image_loader.image_in(cell):
            image = image_loader.get(cell)
            image.show()
            print(cell)
        else:
            print(cell, " - Não há imagem")