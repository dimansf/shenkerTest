from datetime import *

class Dater():
    def __init__(self, sheet):
        self.graph = sheet
        self.days = {'пн':1, 'вт':2,'ср':3,'чт':4,'пт':5 }

    def addDates(self, mainSheet, dateShip=None):
        # преобразовать дату в нужный формат
        if dateShip is not None:
            for row in mainSheet:
                row.append(self.calcDate(row[17], dateShip))
        else:
            for row in mainSheet:
                d = row[0]
                dateShip = datetime(d[0], d[1], d[2])
                row.append(self.calcDate(row[17], dateShip))
        return 1

    def searchRow(self, city):
        for rowGraph in self.graph.get_rows():
            if rowGraph[0].value == city:
                return [r.value for r in rowGraph]
        return None
        
                
    def calcDate(self, city, dateForm):
        row = self.searchRow(city)
        isoweek = dateForm.isoweekday()
        # print(row, city)
        if isoweek > 5:
            curr = 1
            dateForm = dateForm + timedelta(days=8-isoweek)
        else:
            curr = isoweek

        try:
            daySplitted = row[curr].split(',')
        except:
            return 'Отсуствуют данные по данному городу'
        print('daySplitted - ' + str(daySplitted) + ' ' + str(city))
        s = []
        for d in daySplitted:
            matches = d.count('*') 
            # print('days[] ' + str(d[:-matches]))
            try:
                td = timedelta(days=7*matches + self.days[d[:-matches]] - curr)
            except:
                td = timedelta(days=7*matches + self.days[d] - curr)
            dd = dateForm+td
            # s = s + " " + str(dd.date())
            s.append(str(dd.date()))
        return s[0]
            

            

        
