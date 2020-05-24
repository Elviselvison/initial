# max tra 2 funzioni 
def  my_max(a , b ):
    if a==b:
        print('i due nuemri sono uguali')
    if a>b:
        print('il numero max è' +str(a))
    else:
        print('il numero max è' +str(b))

#max tra 3 numeri 
def my_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

      #  funzione che restituisce un se è un vocale o no 
def vocali(parametro):
    vocali= 'aeiuo'
    if parametro in vocali:
        print(True)
    else:
        print(False)

def sum_lista( lalist):
    lalist =0
    for i in lalist:
        n=n+1
        i+=1
        return n

def sommatrice(lista):
    risultato = 0
    for numero in lista:
        risultato += numero
    print('Il risultato della somma è... ' + str(risultato))

