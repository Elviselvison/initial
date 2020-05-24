#tres
a= ['gato', 'cane' ,'topo', 'capra', 'polo', 'gallina']

indice =(len(a) -1) # -1 vuole dire parti dall'altra parte
nuova_stringa= ''
while indice >= 0 :
    nuova_stringa+= a[indice]
    indice-=1
print(nuova_stringa)

for i in range(len(a),-1 ):
    print('%d) %s' %(i+1,  a[i]))
     

for i in a:
    print( '-%s' %(i))

for i, k in enumerate(a):
    print('-%d %s'% (i+1,k))
   
  
def reverser(stringa):
    indice =(len(stringa), -1)
    nuova_stringa= ''
    while indice >= 0 :
        nuova_stringa+= stringa[indice]
    return nuova_stringa
       
