# stampa numeri perfetti
def fun_numperfetto():
    n=int(input('inserisci un valore   '))
    if n==0:
        return False

    temp =0
    for i in range (1,n):
        if (n%i==0):
            temp+=i
    if temp==n:
        print ('il tuo numero è perfetto ')       
    else:
        print('il tuo numero non è perfetto')


fun_numperfetto()
'''
    def perfetto(n):
    if n == 0:
        return False

    divisori = []
    for i in range(1,n):
        if n % i == 0:
        divisori.append(i)  # crea una lista con tutti i valori divisibili

    return sum(divisori) == n
    n = int(raw_input( 'Inserisci un numero positivo: ' ))
    for i in range(0, n):
    if perfetto(i):
    print i  '''


