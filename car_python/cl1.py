class Persona:

    def __init__(self,nome, cognome, età, residenza):
        self.nome=nome
        self.cognome = cognome
        self.età= età
        self.residenza=residenza

    def scheda_personale(self):
        scheda= f"""
        Nome:{self.nome} 
        Cognome: {self.cognome}
        Età:{self.età}
        Residenza:{self.residenza}\n"""
        return scheda

    def modifica_scheda(self):
        print(""" modifica scheda:
        1-Nome
        2-Cognome
        3-Età
        4-Residenza"""  )
        scelta= input('cosa desideri modificare ? ')
        if scelta == "1": self.nome = input('nuovo nome --->  ')
        if scelta == "2": self.cognome = input('nuovo cognome --->  ')
        if scelta == "3": self.età = input('nuova età --->  ')
        if scelta == "4": self.residenza = input('nuova residenza --->  ')

class Studente(Persona):
    profilo= 'studente'
    def __init__(self,nome, cognome, età, residenza, corso):
        super().__init__(nome, cognome, età, residenza)
        self.corso =corso
    def scheda_personale(self):
        scheda = f"""
        profilo= {Studente.profilo}
        corso= {self.corso}
        ***"""
        return super().scheda_personale() + scheda

    def cambio_corso(self, new_corso):
        self.corso = new_corso
        print('corso aggiornato')

class Insegnante(Persona):
    profilo= 'Insegnante'
    def __init__(self,nome, cognome, età, residenza, materia=None):
        super().__init__(nome, cognome, età, residenza)
        self.materia = materia
        if materia is None : 
            self.materia = []
        else: self.materia = materia
    #overwritting per la scheda personale
    def scheda_personale(self):
        scheda = f"""
        profilo= {Insegnante.profilo}
        materia= {self.materia}
        ***"""
        return super().scheda_personale() + scheda
    def aggiungi_materia(self,new_mat):
        if new_mat not in self.materia:
            self.materia.append(new_mat)
            #self.materia= self.materia.append(new_mat)
        print('Elenco materie aggiornate')


        
    


studente_uno= Studente('Py','mike','24', 'casa dello studente','Informatica')
insegnante_uno =Insegnante('hulk','tener', '40', 'torre del cinema',['Python', 'security'])
print(studente_uno.scheda_personale())
print(insegnante_uno.scheda_personale()) # qui ho chiamato l'istanza e la funzione 
#insegnante_uno.modifica_scheda()
insegnante_uno.aggiungi_materia('Filosofia')
studente_uno.cambio_corso('Matematica')
print(studente_uno.scheda_personale())
print(insegnante_uno.scheda_personale())
#print(Studente.scheda_personale(studente_uno)) # qui ho passato il nome della classe la funzione e l'istanza che voglio stampare 
#print(Studente.scheda_personale(studente_due))



