import xlrd
import xlwt
import DateOperator
import BlankCreator
from datetime import *
from os import makedirs



class Task():
    '''
    Главный класс задачи формирования бланков
    '''
    def __init__(self, fileList=None):
        if fileList:
            self.files = fileList
        else:
            self.files = {}
            
        self.wb = None
        self.dater = None
        self.bc = None
        self.f = open('log.txt','w')
        # self.setMainFile(r"C:\Users\dimansf\Documents\projects\python\dbshenker\files\Regions.xls")
        # self.formBid((2019,4, 17))
        


    def getSheet(self, filename, index=0):
        self.wb = xlrd.open_workbook(self.files[filename], 'r')
        return self.wb.sheet_by_index(index)
    

    def setMainFile(self, filename):
        if filename.split('\\')[-1].split('.')[-1] == 'xls':
            self.files['regions'] = filename
            if len(filename.split('\\')) == 1:
                self.files['path'] = '/'.join(filename.split('/')[0:-1])
            else:
                self.files['path'] = '/'.join(filename.split('\\')[0:-1])
            print(filename)
            print('path - ' + self.files['path'])
            self.files['bi_base'] = self.files['path']+'/BI_Base.xls'
            self.files['graph'] = self.files['path']+'/Graph.xls'
            self.files['cities'] = self.files['path']+'/Cities.xls'
            self.files['template'] = self.files['path']+'/Blank.xlt'
            self.files['xmls'] = self.files['path']+'/xmls'
            self.bc = BlankCreator.BlankCreator(self.files['xmls'], self.files['template'])
            self.dater = DateOperator.Dater(self.getSheet('graph'))

            print(self.files)
            return 1
        return 0

    def formBid(self, dateTuple=None):
        if(len(self.files) != 7):
            return 0
        try:
            y,m,d = dateTuple
            dateShipment = datetime(y,m,d)
        except TypeError:
            dateShipment = None

        # вернул массив вида [ [var, var2,...], ...]
        elements = self.sheetToList(self.getSheet('regions'))
        elements = self.belongCodes(elements)
        elements = self.mergeMainSheet(elements)
        dict1 = elements
        elements = elements.values()
        elements = self.belongCities(elements)
        # (2019, 4, 17)
        self.dater.addDates(elements, dateShipment)
        for row in elements:
            self.bc.create(row, dateShipment)
        
        self.f.write('\n'.join(str(elements).split('],')))
       

    def openDir(self):
        import subprocess
        from pathlib import Path
        path1 = '\\'.join(self.files['xmls'].split('/'))
        cmnd = 'explorer.exe "' + path1 + '"'
        subprocess.Popen(cmnd)
        print(cmnd)
        return 1

    def belongCities(self, sheet):
        citiesBook = self.getSheet('cities')
        for row in sheet:
            for rowCities in citiesBook.get_rows():
                # print(str(r[16]) + ' ' + self.toD(c[1].value))
                if row[16] == self.toD(rowCities[0].value):
                    row.append(self.toD(rowCities[1].value))
        return sheet
    
    def belongCodes(self, sheet):
        ''' @var sheet [ [], ... ]'''
        codes = self.getSheet('bi_base')
        for row in sheet:
            for rowBibase in codes.get_rows():
                if(rowBibase[2].value == row[10]):
                    row.append(self.toD(rowBibase[0].value)) # код юзера
                    row.append(self.toD(rowBibase[1].value)) # код города
        return sheet

    def toD(self, fl):
        try:
            return str(int(fl))
        except ValueError:
            return str(fl)

    def mergeMainSheet(self, elements):
        els = {}
        for i in range(len(elements)):
            newWawe = True
            specialKey = elements[i][15] + '_' + elements[i][10]
            for k in range(i+1, len(elements)):
                if elements[i][15] == elements[k][15] and elements[i][10] == elements[k][10]:
                    # если ключ есть и это новый цикл значит ничего не делаем
                    if els.get(specialKey) is not None:
                        if newWawe:
                            continue
                        else:
                            els[specialKey] = self.mergeRow(
                                els[specialKey], elements[k])
                                
                            
                    else:
                        els[specialKey] = self.mergeRow(
                            elements[k], elements[i])
                        newWawe = False
            if newWawe and els.get(specialKey) == None:
                els[specialKey] = elements[i]
        # print(len(tm1))
        return els


    def mergeRow(self, e1, e2):
        e = []
        for i in range(len(e1)):
            if i == 2:
                e.insert(i,  str(e1[i]) + ',  ' + str(e2[i]))
                continue
            if i in range(7, 10):
                e.insert(i, e1[i] + e2[i])
                continue
            if i == 13:
                e.insert(i, e1[i] + ' ' + e2[i])
                continue
            e.insert(i, e1[i])
        return e

    def sheetToList(self, sheet):
        res = []
        f = True
        for cells in sheet.get_rows():
            if f:
                f = False
                continue
            n = []
            for i in range(len(cells)):
                if i == 0:
                    d = xlrd.xldate_as_tuple(
                        cells[i].value, self.wb.datemode)
                    n.append(d[0:3])
                    continue
                if i == 2:
                    n.append(str(int(cells[i].value)))
                    continue
                if i == 7:
                    n.append(int(cells[i].value))
                    continue

                n.append(cells[i].value)

            res.append(n)
            del n
        return res
