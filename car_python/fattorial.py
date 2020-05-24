#una funzione che mi calcola il fattoriale dato un numero
def my_fattorial(r):
    temp=1
    for i in range(1, r+1):
        temp*= i
    print('il fattoriale di %d è %d' %(r,temp))

my_fattorial(5)
my_fattorial(10)
my_fattorial(15)
my_fattorial(20)