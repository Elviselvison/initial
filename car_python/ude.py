n = int(input("inserisci un numero  "))
i=1

'''for  i in range(n):
   # i+=1
    print (i)'''
while i<n:
    if (i%3==0):
        i+=2
        #break blocca il ciclo se si determina una certa condizione 
        continue # fa tornare all'inizio del loop
    print (i)
    i+=2