import csv
domanda = input("nome prodotto ")
x= open('esempiocsv.csv','r')
alfa =csv.reader(x, delimiter= ';')
print (alfa)

for i in alfa:
    if domanda ==i[0]:
        print(i[1])
        #print('il prezzo del %a è %d' % (domanda, i[1] ))  % SI APSETTA SOLO NUMERI
        print("il prezzo di {} è {} euro".format(domanda, i[1]))
       


 