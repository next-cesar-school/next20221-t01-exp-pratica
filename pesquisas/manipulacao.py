import openpyxl
from openpyxl_image_loader import SheetImageLoader

#loading the Excel File and the sheet
wb = openpyxl.load_workbook('D:\\O QUE DEIXAR\\Cursos Online\\NExT\\Projeto Final NExT - T1\\F1_imagem.xlsx')
sheet = planilha['Plan1']

#calling the image_loader
image_loader = SheetImageLoader(sheet)

#get the image (put the cell you need instead of 'A1')
image = image_loader.get('A1')   #__init__('Plan1')    #get('A1')

#showing the image
image.show()

#saving the image
#image.save('D:\\O QUE DEIXAR\\Cursos Online\\NExT\\Projeto Final NExT - T1\\Imagens\\image_name.jpg')