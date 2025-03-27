"""
Obiettivo:
Definire una classe Persona che rappresenti una persona con attributi come nome ed età.

Istruzioni:

Crea la classe Persona con un costruttore (__init__) che inizializza i due attributi.
Definisci un metodo saluta che stampi un messaggio di saluto, ad esempio:
php-template
Copia
Ciao, mi chiamo <nome> e ho <età> anni.
Crea due istanze della classe e chiama il metodo saluta per ciascuna.

"""

class Persona:
    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = eta
    def saluta(self):
        return f"Ciao sono {self.nome} ed ho {self.eta}"
    

persona1 = Persona("Paolo", 22)
print(persona1.saluta())