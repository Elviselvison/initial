# scritura di un file se non preciso nessun percorso me lo crea nella stessa cartella
# 'a' append va aggiunta una nuova frase 
#  /n vai su una nuova line
# readlines ogni volta che trova a capo mette l'informazione in una lista

x= open ('scrittura.txt', 'w') 
x.write(' tutto quello che è scritto in questo file è stato generato da python')
x.close()

# vado a leggere un file già creato quindi in modalità read
x= open('testo.txt', 'r')
t=x.readlines()
y= x.read() # questo esempio serve anche per capire che quando entra a leggere non entra di nuovo

for elementi in t: # con questo ciclo for stampo tutti gli elementi di t 
    print(elementi)
print(y)
print(t)
x.close()

x= open('testo.txt', 'a')
x.write('fine del testo')
x.close()

