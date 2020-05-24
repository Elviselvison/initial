class Studente:
    ore_settimanali = 36
    corpo_studentesco=0
    def __init__(self,nome,Cognome,corso ):
        self.nome= nome 
        self.cognome=Cognome
        self.corso= corso
        Studente.corpo_studentesco +=1

    def scheda_personale(self):
        return f"""scheda studente:\n Nome:{self.nome}\n cognome: {self.cognome} \n corso:{self.corso}\n ore settimanali: {self.ore_settimanali}"""

studente_uno= Studente('Py','mike','programmazione')
studente_due =Studente('hulk','tener', 'cinema')
studente_uno.ore_settimanali +=4
#print(studente_uno.scheda_personale())
#print(studente_due.scheda_personale()) # qui ho chimato l'istanza e la funzione 
#print(Studente.scheda_personale(studente_uno)) # qui ho passato il nome della classe la funzione e l'istanza che voglio stampare 
#print(Studente.scheda_personale(studente_due))
#t(Studente.__dict__)
#print(studente_uno.__dict__)
print(Studente.corpo_studentesco)
#Ereditarietà
