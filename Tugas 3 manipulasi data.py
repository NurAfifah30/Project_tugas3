import datetime

y=datetime.datetime(2022, 5, 17)

print(y) 

x = datetime.datetime.now()
print("hari ini " ,x) 

print("tahun :",x.year)
print("bulan :",x.month)
print("day :",x.day)

print(x.strftime("%A")) 
print(x.strftime("%B"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%w"))