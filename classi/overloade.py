"""
Esercizio 4: Overloading degli Operatori
Obiettivo:
Imparare a sovraccaricare operatori in una classe.

Istruzioni:

Crea una classe Rettangolo con attributi larghezza e altezza.
Definisci un metodo per calcolare l’area.
Sovraccarica l’operatore + in modo che, sommando due rettangoli, si crei un nuovo rettangolo la cui larghezza sia la somma delle larghezze e l’altezza la somma delle altezze.
Verifica la funzionalità creando due rettangoli e stampando l’area del rettangolo risultante dalla somma.

"""

class Rettangolo:
    def __init__(self, larghezza: float, lunghezza: float):
        self.larghezza = larghezza
        self.lunghezza = lunghezza
    
    def area(self):
        return self.larghezza * self.lunghezza
    
    def __add__(self, other: "Rettangolo"):
        if isinstance(other, Rettangolo):
            nuova_lunghezza =  self.lunghezza + other.lunghezza
            nuova_larghezza = self.larghezza + other.larghezza
            return Rettangolo(nuova_larghezza, nuova_lunghezza)
        return NotImplemented


rettangolo1 = Rettangolo(10, 12)
rettangolo2 = Rettangolo(2, 3)
rettangolo3 = rettangolo1 + rettangolo2

print(rettangolo3.larghezza, rettangolo3.lunghezza)
print(rettangolo3.area())