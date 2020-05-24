def complementare(nucleotide):
    nucleotide = nucleotide.capitalize()  #converts the first caracter in capital in originally its 
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'T':
        return 'A'

nucleotide = input('inserisci un ')
print(complementare(nucleotide))

def filamento_opposto(filamento):
    opposto = ''

    for nucleotide in filamento:
        opposto += complementare(nucleotide)

    return opposto