# STATICS AND CLASS METHODS 
# DEFINISCO UNA CLASSE

class person(object):
    # definisco una variabile di classe 
    population = 50 
    def __init__(self, name, age ):
        self.age = age 
        self.name = name 
    @classmethod # NON DEVO CREARE UN OGGETTO O UN ISTANZA PRIMA DI USARE QUESTO METODO
    #HA accesso a tutte le variabili public della classe 

    def getpopulation(tms):
        return tms.population  

    @staticmethod # non devo creare un'istanza prima di gestirlo ma non ha acesso alle varibili public deve
    # tramite le variabili di inizializzazione. puoi non usare un parametro 

    def getage(age):
        return age  >= 18 

    def display(self):
        print( self.name, 'IS' , self.age, 'years old')  

newperson = person('tim', 18)
print(newperson.display())
print(person.getpopulation()) 
                    # perché scrive none


        
