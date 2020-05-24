a = input('inserisci una stringa  ')
b= ''
i = (len(a)-1)
while i>=0:
    b+=a[i]
    i-=1
if a==b:
    print('è un palindromo')
else: 
    print('non è un palindromo')

# non entra nell'if 