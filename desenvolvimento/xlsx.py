import io

import openpyxl


def extract_images (file_bytes):
    sheet = openpyxl.load_workbook(io.BytesIO(file_bytes))
    active_sheet = sheet.active
    return active_sheet._images