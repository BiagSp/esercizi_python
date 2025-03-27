"""
Obiettivo:
Imparare a utilizzare metodi di classe e metodi statici.

Istruzioni:

Estendi la classe Persona aggiungendo:
Un attributo di classe numero_di_persone che tenga il conto di quante persone sono state create.
Un metodo di classe stampa_numero_persone che stampi il numero totale di istanze create.
Aggiungi un metodo statico controlla_eta(eta) che riceva un'età e ritorni True se è maggiore o uguale a 18, altrimenti False.
Verifica il corretto funzionamento creando più istanze e chiamando i metodi.

"""


class Persona:
    #Attributo di classe per contare le istanze
    numero_di_persone = 0

    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self. eta = eta
        #incrementiamo il contatore ogni volta che viene creata un'istanza 
        Persona.numero_di_persone += 1

    def saluta(self):
        return f"Ciao sono {self.nome} ed ho {self.eta} anni"
    
    @classmethod
    def stampa_numero_persone(cls):
        return f"Numero di persone create {cls.numero_di_persone}"
    
    @staticmethod
    def controlla_eta(eta):
        return eta >= 18
    


# Creazione di istanze per testare il funzionamento
persona1 = Persona("Paolo", 12)
persona2 = Persona("Anna", 30)

print(persona1.saluta(), persona2.saluta(), Persona.controlla_eta(persona1.eta))

print(Persona.numero_di_persone)
