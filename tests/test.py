for i in range(10):
    print(i)

r = [1,3,2]
print(len(r))


r = 'пн**'

print(r.split(','))
print(r[:-r.count('*')])


from datetime import *

t = datetime(2017,2,25)
print(t)
d = timedelta(days=30)
# d.days = 30
s = t - d
print(s.date())


from BlankCreator import *
from xlrd import *

r1 = [r"C:\Users\dimansf\Documents\projects\python\dbshenker\files\Blank.xlt"]
wb = open_workbook(r1[0], 'r')
# BlankCreator('/', wb).create()

r12 = {1:2}
t = 'C:/12'
print(len(t.split('\\')))
print(len(r12))