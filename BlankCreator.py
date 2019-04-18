import xlwt
import shutil
from os import makedirs
import xlrd
import xlutils.copy
import math
class BlankCreator():

    def __init__(self, path, template=0):
        self.path = path
        self.templ = template
        
    '''
    @var array[] block 
    @var string date   
    '''
    def create(self, row, date=None):
        makedirs(self.path, exist_ok=True)
        file1 = self.path+'/'+row[15]+row[12]+'.xlt'
        print(file1)
        shutil.copy(self.templ, file1)
        rb = xlrd.open_workbook(file1, formatting_info=True)
        wb = xlutils.copy.copy(rb)
        sheet = wb.get_sheet(0)
        right = xlwt.XFStyle()
        right.alignment.horz = right.alignment.HORZ_RIGHT
        lft = xlwt.XFStyle()
        lft.alignment.horz = right.alignment.HORZ_LEFT
        centr = xlwt.XFStyle()
        centr.alignment.horz = centr.alignment.HORZ_CENTER 
        sheet.write(19, 2, str(row[15]), right)
        sheet.write(25, 2, row[16], right)
        # короба в комментарии
        sheet.write(34, 1, math.ceil(float(row[9]) / 1.15), centr)
        sheet.write(34, 2, row[8], centr)
        sheet.write(34, 3, row[9], centr)
        sheet.write(43, 2, str(date.date()))
        sheet.write(48, 2, row[2])
        sheet.write(51, 2, row[18])
        sheet.write(52, 2, 'Число коробов ' + str(row[7]), lft)
        # sheet.write(52, 2, block[18])
        # path = self.path + '/' +block[15]+block[12]
        wb.save(file1)
            
            