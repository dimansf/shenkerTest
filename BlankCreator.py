from xlwt import *
import xlutils.copy


class BlankCreator():

    def __init__(self, path, templ=0):
        self.path = path
        self.template = templ


    '''
    @var array[] block 
    @var string date   
    '''
    def create(self, block, date):
            wb = xlutils.copy.copy(self.template)
            sheet = wb.get_sheet(0)
            sheet.write(19, 2, block[15])
            sheet.write(25, 2, block[16])
            # короба в комментарии
            sheet.write(34, 1, float(block[9]) / 1.15)
            sheet.write(34, 2, block[8])
            sheet.write(34, 3, block[9])
            sheet.write(43, 2, date)
            sheet.write(48, 2, block[2])
            sheet.write(51, 2, block[18])
            sheet.write(52, 1, block[7])
            # sheet.write(52, 2, block[18])
            wb.save(self.path + '\\' + block[15]+block[12] + '.xls')
