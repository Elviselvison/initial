import datetime
x=datetime.datetime.now()
y= datetime.date.today()
print(y)
print(x.year)
#formatazione italiana 
print('{}/{}/{}'.format(x.day, x.month, x.year))

#operazioni con le date ,,
t= datetime.datetime(2018,5, 26,12,30)
p= datetime.datetime(2018,7,12,12,30)
z= p-t
z=str(z) 
z=z.split(" ") # metto un separatore per trasformare la tringa in lista 
print(z[:2])