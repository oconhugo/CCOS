import xlsxwriter
import openpyxl
from datetime import datetime


workbook = xlsxwriter.Workbook('Inventory-2020.xlsx')
worksheet = workbook.add_worksheet()
row , orderNum = 0, 0
counter = 0
date = ""

class Inv(object):
    def __init__(self,master,**kwargs):
        # Create a workbook and add a worksheet.
        global date
        date = datetime.today().strftime('%Y-%m-%d')

    def add(self, order):
        global row, orderNum
        colText =0
        worksheet.write(row, colText, "Order #"+ str(orderNum))
        colText, colValue = 1, 2
        for i in order:
            for key in i:
                worksheet.write(row, colText, key)
                worksheet.write(row, colValue, i[key])
            row += 1
        orderNum += 1
        Inv.closeXLSX(self)

    def closeXLSX(self):
        global date
        workbook.close()
        ss = openpyxl.load_workbook("Inventory-2020.xlsx")
        ss_sheet = ss['Sheet1']
        ss_sheet.title = date
        ss.save("Inventory-2020.xlsx")

