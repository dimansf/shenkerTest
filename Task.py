import xlrd
import xlwt
import DateOperator
import BlankCreator

class Task():
    '''
    Главный класс задачи формирования бланков
    '''
    def __init__(self, fileList=None):
        self.files = None
        if fileList:
            self.files = fileList
        # self.formBid()
        self.wb = None
        self.files = {}
        self.eSheet = None

    def getWB(self, filename):
        return xlrd.open_workbook(self.files[filename], on_demand=True)

    def getSheet(self, filename, index=0):
        self.wb = xlrd.open_workbook(self.files[filename], 'r')
        return self.wb.sheet_by_index(index)
    

    def setMainFile(self, filename):
        if filename.split('\\')[-1].split('.')[-1] == 'xls':
            self.files['regions'] = filename
            print()
            # return 0
            self.files['path'] = '/'.join(filename.split('/')[0:-1])
            self.files['bi_base'] = self.files['path']+'/BI_Base.xls'
            self.files['graph'] = self.files['path']+'/Graph.xls'
            self.files['cities'] = self.files['path']+'/Cities.xls'
            self.files['template'] = self.files['path']+'/Blank.xlt'
            self.files['xmls'] = self.files['path']+'/xmls'
            print(self.files)
            return 1
        
        return 0

    def formBid(self, dateTuple=''):
        mergedSheet = self.mergeMainSheet()
        self.eSheet = self.belongsCodesAndCities(mergedSheet)
        # (2019, 4, 17)
        self.addDates(dateTuple)
        bc = BlankCreator.BlankCreator(self.files['xmls'], self.getWB('template'))
        for row in self.eSheet.values():
            bc.create(row, dateTuple)
            # break

        print(self.eSheet)

    def openDir(self):
        import subprocess
        subprocess.Popen('explorer.exe "' + '\\'.join(self.files['xmls'].split('/')) + '"')
        # print('explorer.exe "' + '\\'.join(self.files['xmls'].split('/')) + '"')

    def addDates(self, dates):
        daysSheet = self.getSheet('graph')
        dater = DateOperator.Dater(daysSheet)
        dater.addDates(self.eSheet, dates)


    def belongsCodesAndCities(self, sheet):
        citiesBook = self.getSheet('cities')
        codes = self.getSheet('bi_base')
        for r in sheet.values():
            for row in codes.get_rows():
                if(row[2].value == r[10]):
                    r.append(self.toD(row[0].value))
                    r.append(self.toD(row[1].value))

        # print(sheet)
        for r in sheet.values():
            for c in citiesBook.get_rows():
                # print(str(r[16]) + ' ' + self.toD(c[1].value))
                if r[16] == self.toD(c[0].value):
                    r.append(self.toD(c[1].value))
        # print(sheet)
        return sheet

    def toD(self, fl):
        try:
            return str(int(fl))
        except ValueError:
            return str(fl)

    def mergeMainSheet(self):
        elements = self.sheetToList(self.getSheet('regions'))
        # print(elements)
        els = {}
        for i in range(len(elements)):
            newWawe = True
            specialKey = elements[i][4] + ' ' + elements[i][10]
            for k in range(i+1, len(elements)):
                if(self.compareRow(elements[i], elements[k])):
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
        # print(els)
        return els

    def compareRow(self, e1, e2):
        if e1[10] == e2[10] and e1[4] == e2[4]:
            return True
        return False

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
                    n.append(xlrd.xldate_as_tuple(
                        cells[i].value, self.wb.datemode))
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
