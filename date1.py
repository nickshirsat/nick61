import  datetime 

t = datetime.datetime(1,2,3)
now1 = datetime.datetime.now()

print('user time: ',t)
print('\nSystem time ',now1)
print('Hours: ', t.hour)
print('Minutes: ', t.minute)
print('Seconds: ', t.second)
print('Tzinfo: ', t.tzinfo);




''' OUTPUT

user time:  0001-02-03 00:00:00

System time  2018-07-13 11:32:13.147310
Hours:  0
Minutes:  0
Seconds:  0
Tzinfo:  None
'''
