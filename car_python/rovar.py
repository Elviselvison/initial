'''def rovar(w):
    c='aeiouy'
    for i in w :
        if i not in c:
            i=i+'o'+i
            
    print(w)

m = input('inserisci una parola   ')
rovar(m)'''
def traduttore():
    print('''
    Ciao! questo programma traduce un testo passato in "rövarspråket".
    Ció significa che raddoppia ogni consonante delle parole e ci mette una "o" in mezzo...
    ''')

    vocali = "aeiou"
    specials = [" ", ",", ".", "?", "!", '"',"'"]
    
    while True:
        testo = input('\nInserisci il testo che desideri tradurre -> ')
        tradotta = ""
        for x in testo:
            if x in vocali or x in specials:
                tradotta += x #tradotta = tradotta + x
            else:
                tradotta = tradotta + x + "o" + x

        print(f"Ecco a te la traduzione! '{tradotta}'")

        if input("\nDesidere tradurre un'altra frase? ") == "no":
            break

traduttore()

# ca
