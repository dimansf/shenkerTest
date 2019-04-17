import xlrd
import xlwt
import datetime

reader = xlrd.open_workbook('./workTable.xls', 'r')

sheet1 = reader.sheet_by_index(1)

for n in range(0, sheet1.nrows):
    print(sheet1.row_values(n))

wb = xlwt.Workbook()
shet = wb.add_sheet('testSheet')
shet.write(0,0, 'Somebody')
wb.save('./blankResult.xls')

d = {'sheet': sheet1, 'r':2, 12: datetime.date(2017,1,1), }
print(d['sheet'].row_values(1))
print(d[12])