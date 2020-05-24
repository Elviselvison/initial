class Veicoli:
    def __init__(self, marca, modello,colore, prezzo ):
        self.marca= marca 
        self.modello = modello 
        self.colore = colore 
        self.prezzo = prezzo

    def scheda(self):
        x= " In sede ho una {}  modello {}  di colore  {}  ".format(self.marca, self.modello, self.colore)
        return x
    def prezzi(self):
        x= "il veicolo {} {} costa {} euro ".format(self.marca, self.modello, self.prezzo)
        return x


class Automobile(Veicoli): # metto la classe che deve ereditare in parentesi 
    def __init__ (self, marca, modello, colore,prezzo, cilindrata):
        super().__init__(marca,modello, colore, prezzo)
        self.cilindrata = cilindrata
    
    def scheda(self):
        x= " cilindrata {}".format(self.cilindrata)
        return super().scheda() + x

class bicicletta(Veicoli):
    pass # salta 
 

newauto = Automobile('fiat', 'bravo', 'griggio', '1800', '2500')
print(newauto.scheda())
    
        # creo un'istanza per richiamare la mia funzione 
nv = Veicoli("Mercedes", "C220", "Nera", "1500")


