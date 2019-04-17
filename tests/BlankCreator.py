from xlwt import *
from xlrd import *
from xlutils.copy import copy

class BlankCreator():
    def __init__(self, path, templ, sheet=0):
        self.path = path
        self.template = templ

    def create(self, block=''):
        wb = copy(self.template)
        sheet = wb.get_sheet(0)
        sheet.write(20, 2, '123')
        sheet.write(26, 2, '123')
        sheet.write(35, 1, '123.0')
        sheet.write(35, 2, '143.0')
        sheet.write(35, 3, '1.0')
        wb.save('123.xls')

