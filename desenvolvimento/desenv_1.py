import openpyxl
from openpyxl import Workbook
import openpyxl_image_loader

worksheet = openpyxl.load_workbook('D:\\O QUE DEIXAR\\Cursos Online\\NExT\\Projeto Final NExT - T1\\F1_imagem.xlsx')
sheet = worksheet.active

#print(cell_range = planilha['A1':'C2'])

for row in sheet.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell in row:
        print(cell)