# inserito un cucleotide restituisca un valore corrispondente 
# Capire perché non si può usare raw input

nucleotide = input('Inserisci un nucleotide (A,C,G,T):')
if nucleotide == 'A' or nucleotide == 'a':
    print ('T')
elif nucleotide == 'C' or nucleotide == 'c':
    print ('G')
elif nucleotide == 'G' or nucleotide == 'g':
    print ('C')
elif nucleotide == 'T' or nucleotide == 't':
    print ('A')