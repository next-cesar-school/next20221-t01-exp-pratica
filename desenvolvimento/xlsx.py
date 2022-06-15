import openpyxl

def extrair_imagens (arquivo):
    print(arquivo)
    print(type(arquivo))
    planilha = openpyxl.load_workbook(arquivo)