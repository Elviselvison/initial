class Studente:
    ore_settimanali=36 # variabile di classe
    def __init__(self, nome, cognome,corso_di_studio):
        self.nome =nome
        self.cognome = cognome
        self.corso_di_studio = corso_di_studio
    def scheda_personale(self):
        return f"scheda_personale:\n nome:{self.nome} \n cognome:{self.cognome} \n corso_di_studio: {self.corso_di_studio} \n ore settimanale:{Studente.ore_settimanali}"


studente1=Studente('Edem','kpogo','programmazione')
studente2= Studente('kodjo', 'noudefia', 'science politiche')  
print(studente1.scheda_personale())
print(studente2.scheda_personale()) 
print(Studente.scheda_personale(studente1))
# variabile di istanza e variabile di classe 
  