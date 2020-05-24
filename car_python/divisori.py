# scrivo una funzione che dato un input restituisce una lista con tutti i divisori 
def my_divisori():
    n=int(input('inserisci un numero   '))
    div =[]
    for i in range (1,n):
        if(n%i==0):
            div.append(i)
    print(div)  
    print(sum(div))      
    return
       

my_divisori()

