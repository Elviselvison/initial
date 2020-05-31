# quadrati= []
# for i in range(0, 10):
#     quadrati.append(i**2)
# print(quadrati)

# quadrati =[ i**2 for i in range (10)]
# print (quadrati)

r = [i**2 for i in range (0, 10 )]

print (r)

# list1 = [1,2,3]
# list2 = [3,1,4]

# mix = []
# for i in (list1):
#     for y in list2:
#         if i not in mix:
#             mix.append(i)
#         elif y not in mix:
#             mix.append(y)

# print(mix)
# mix = []
# for i in (list1):
#     if i not in mix:
#             mix.append(i)
# for y in (list2):
#     if y not in mix:
#             mix.append(y)

#creare delle coppie con delle valori diversi tra di loro

# mix= []
# for i in list1:
#     for y in list2 :
#         if i!=y:
#             mix.append((i,y))
# print(mix)

# mix = [(i,y) for i in list1 for y in list2 if i!=y ]
# print(mix)
# strigati= []
# for i in list1:
#     strigati.append(str(i))
# print(strigati)
# stringati = [str(i) for i in list1]
# print(stringati)

# l'istruzione with 
#permette di fare la chiusura di un file quando il file viene chiuso 
#utiliso dei file 

# zenigata= open("zaza.txt" , "r")
# for i in zenigata:
#     print(riga)
# zenigata.close()
# #per verificare che il file sia chiuso faccio
# print(zenigata.closed)


# # esepio con with 

# with open ("zaza.txt","r") as zenigata:
#     for i in zenigata:
#         print (i)


# #altro esempio

# numeri=[]
# dati = open("dati_importanti.txt", "r")
# try:
#     for num in dati:
#         numeri.append(float(num))
# except ValueError:
#     print("C'è qualcosa che non va ")


# print(dati.closed)


# #con with 
# with open("dati_importanti.txt", "r") as dati:
#     try:
#         for num in dati:
#             numeri.append(float(num))
#     except ValueError:
#         pass

# print(dati.closed)
# def mia_funzione():
#     spam = 24
#     return spam 
 