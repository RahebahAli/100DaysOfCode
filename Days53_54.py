import modules as m
import datetime as dt
#1
print("1 + 8 =", m.add(1, 8))

print("4 - 2 =", m.sub(4, 2))

print("6 * 6 =", m.mul(6, 6))

print("8 / 2 =",m.div(8, 2))

#2
d = dt.datetime.now()
print(d)
print(d.strftime("%Y")) # Or print(d.year)
print(d.strftime("%B"))
print(d.strftime("%m")) # Or print(d.month)
print(d.strftime("%A"))
print(d.strftime("%d")) # Or print(d.day)

#3
yesterday = d - dt.timedelta(days = 1)
tomorrow = d + dt.timedelta(days = 1)
print("yesterday: " , yesterday)
print("tomorrow: " , tomorrow)