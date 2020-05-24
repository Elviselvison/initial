nomi = ('Numa', 'Tullo', 'Anco')
cognomi =  ('Pompilio', 'Ostilio', 'Marzio')
l = []
for nome, cognome in zip(nomi,cognomi): 
    l.append({'nome': nome, 'cognome': cognome})
print(l)

# usare la funzione zip 
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
l=[]

for   i , j  in  zip( a, b ):
    l.append({'a': i, 'b':j})
       
print (l)

