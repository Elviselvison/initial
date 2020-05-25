class Persona:# altro modo di gestire le classi
    #costruttore alternativo ad init
    # aggiunto a git 

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

    @classmethod # è un decoratore che mi permette di alterare il comportamento della clase almio piacimento 
    def from_string(cls, stringa_persona,*args): # i metodi di classe sono legati alla classe e non alle istanze
        nome, cognome, età, residenza = stringa_persona.split('-')
        return cls(nome, cognome, età , residenza,*args) # con *args gestisco i parametri aggiuntivi che possono essere in zero o in più

    @classmethod
    def occupazione(cls):
        if cls.__name__ =='Studente':
            return 'Studente'
        else:
            return 'Insegnante'
        
    @staticmethod
    def info_prog():
        info = """
        Nome: Persona
        Cognome: Famosa
        COmmenti: questo è un metodo statistico"""
        return info



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

    
   
        
#iron_man ='Tony-stark-40-torre stark'  
#zuck = 'mark-zuckenberg-33-California'
#persona1=Persona.from_string(iron_man)
#insg1 =Insegnante.from_string(iron_man, 'Ingegneria')
#stud1=Studente.from_string(zuck,'SEO')
#print(insg1.scheda_personale())
#print(stud1.scheda_personale())
#print(insg1.occupazione())
#print(stud1.occupazione())
print(Persona.info_prog())



