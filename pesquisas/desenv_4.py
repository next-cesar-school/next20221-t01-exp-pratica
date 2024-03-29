import openpyxl
from openpyxl import Workbook                           # não precisa dessa
from openpyxl import load_workbook                      # não precisa dessa
from openpyxl_image_loader import SheetImageLoader      # não precisa dessa
import openpyxl_image_loader                            # não precisa dessa
import io
import PIL

worksheet = openpyxl.load_workbook('D:\\O QUE DEIXAR\\Cursos Online\\NExT\\Projeto Final NExT - T1\\F1_imagem.xlsx')
sheet = worksheet.active # abre a aba ativa, ou seja, aquela que foi modificada por último
cont = 0

for image in sheet._images:
    cont += 1
    #print(image)
    #print(type(image.anchor))
    #print(type(image.anchor._from))
    #print(image.anchor._from.col)                                                              # mostra a coluna que a imagem está
    #print(image.anchor._from.row)                                                              # mostra a linha que a imagem está
    #print(image.path)                                                                          # mostra o diretório no qual a imagem está salva
    #print(image._data())                                                                       # mostra a matriz da imagem, ou seja, a sequência de RGB's dos pixels
    stream_str = io.BytesIO(image._data())                                                      # "BytesIO()" mantém os dados como bytes em um buffer na memória
    #print(stream_str.getvalue())                                                               # ".getvalue()" pega o valor do buffer como uma string
    imagem = PIL.Image.open(stream_str)                                                         # armazena a imagem numa variável
    imagem.save(f'D:\\O QUE DEIXAR\\Cursos Online\\NExT\\Projeto Final NExT - T1\\{cont}.png')  # salva a imagem no diretório (path)