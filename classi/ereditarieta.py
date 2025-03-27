"""
Esercizio 3: Ereditarietà e Override
Obiettivo: Imparare a creare classi derivate ed eseguire l'override dei metodi.

Istruzioni:

Crea una classe Persona con attributi nome e eta e un metodo saluta() che stampa un saluto.
Crea una sottoclasse Studente che eredita da Persona e aggiunge l'attributo matricola.
Nella classe Studente sovrascrivi il metodo saluta() in modo da includere anche la matricola nel saluto.
Crea istanze di Persona e Studente e prova a chiamare il metodo saluta() su entrambe.

"""

class Persona:
    def __init__(self, nome, eta: int):
        self.nome = nome
        self.eta = eta
    def saluta(self):
        print(f"Ciao io sono {self.nome} ed ho {self.eta} anni")

    
class Studente(Persona):
    def __init__(self, nome, eta, matricola):
        super().__init__(nome, eta)
        self.matricola = matricola

    def saluta(self):
        super().saluta()
        print(f", Matricola: {self.matricola}")


p = Persona("Mario", 23)
p.saluta()
s = Studente("Luca",23, "A123")
s.saluta()