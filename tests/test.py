for i in range(10):
    print(i)

r = [1,3,2]
print(len(r))


r = 'пн**'

print(r.split(','))
print(r[:-r.count('*')])


from datetime import *
from time import *
t = date.today()
print(t.year, t.month, t.day)
d = timedelta(3)
# print(t.isoweek())
# d.days = 30
s = t - d
print(s)

