from datetime import *

class Dater():
    def __init__(self, sheet):
        self.graph = sheet
        self.days = {'пн':1, 'вт':2,'ср':3,'чт':4,'пт':5 }

    def addDates(self, mainSheet, dates=''):
        # преобразовать дату в нужный формат
        if dates != '':
            y,m,d = dates
            df = datetime(y,m,d)
            for row in mainSheet.values():
                row.append(self.calcDate(row[17], df))
        else:
            for row in mainSheet.values():
                y, m, d, mm, s, ms = row[0]
                print( y, m, d, mm, s, ms)
                df = datetime(y, m, d)
                row.append(self.calcDate(row[17], df))
            
        
        return 1

    def searchRow(self, city):
        for rowGraph in self.graph.get_rows():
            if rowGraph[0].value == city:
                return [r.value for r in rowGraph]
        
                


    def calcDate(self, city, dateForm):
        row = self.searchRow(city)
        isoweek = dateForm.isoweekday()
        print(row, city)
        if isoweek > 5:
            curr = 1
            dateForm = dateForm + timedelta(days = 8 - isoweek)
        else:
            curr = isoweek

        try:
            daySplitted = row[curr].split(',')
        except:
            return 'Отсуствуют данные по данному городу'
        print('daySplitted - ' + str(daySplitted))
        s = ''
        for d in daySplitted:
            matches = d.count('*') 
            # print('days[] ' + str(d[:-matches]))
            try:
                td = timedelta(days=7*matches + self.days[d[:-matches]])
            except:
                td = timedelta(days=7*matches + self.days[d])
            dd = dateForm+td
            s = s +" " + str(dd.date())
        return s
            

            

        
