import  datetime 

t = datetime.datetime(2018,2,3 ,1,2,3,4)
now1 = datetime.datetime.now()

print('user time: ',t)
print('\nSystem time ',now1)
print('Hours: ', t.hour)
print('Minutes: ', t.minute)
print('Seconds: ', t.second)
print('Tzinfo: ', t.tzinfo);




''' OUTPUT

user time:  2018-02-03 01:02:03.000004

System time  2018-07-13 11:37:49.320285
Hours:  1
Minutes:  2
Seconds:  3
Tzinfo:  None
'''
