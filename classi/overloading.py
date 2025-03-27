"""
Esercizio 5: Overloading degli Operatori
Obiettivo: Imparare a sovraccaricare gli operatori in una classe.

Istruzioni:

Crea una classe Punto che rappresenta un punto nel piano con coordinate x e y.
Sovraccarica l'operatore + (definendo il metodo __add__) in modo che la somma di due oggetti Punto restituisca un nuovo Punto con coordinate sommate.
Implementa anche il metodo __str__ per visualizzare in modo chiaro il punto.
Crea un paio di istanze di Punto e prova ad sommarle.

"""



class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Punto"):
        if isinstance(other, Punto):
            return Punto(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
p1 = Punto(2, 3)

p2 = Punto(4, 5)

p3 = p1 + p2

print(p3)  # Output: (6, 8)