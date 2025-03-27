"""
Esercizio 3: Ereditarietà e Metodi Sovrascritti
Obiettivo:
Utilizzare l’ereditarietà per creare una classe derivata e sovrascrivere alcuni metodi.

Istruzioni:

Definisci una classe base Animale con attributi come nome e eta e un metodo verso che stampi un verso generico (es. "L'animale emette un suono").
Crea una classe derivata Cane che erediti da Animale e sovrascriva il metodo verso per stampare "Il cane abbaia".
Crea una classe derivata Gatto che, analogamente, sovrascriva verso per stampare "Il gatto miagola".
Crea istanze di ciascuna classe e chiama il metodo verso per verificare il polimorfismo.

"""

class Animale:
    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = eta
    
    def verso(self):
        return f"l'animale {self.nome} ememtte un suono"
    


class Cane(Animale):
    def verso(self):
        return "il cane abbaia"
    
class Gatto(Animale):
    def verso(self):
        return "il gatto miagola"
    


cane = Cane("Bob", 12)
print(cane.verso())
gatto = Gatto("tiffy", 6)
print(gatto.verso())