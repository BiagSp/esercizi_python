"""
Gerarchia di Forme Geometriche

Crea una classe base Forma e classi derivate come Cerchio, Rettangolo e Triangolo.

"""

from abc import ABC, abstractmethod
import math

class Forma(ABC):
    def __init__(self):
        self.nome = "Forma geometrica"
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    def descrizione(self):
        return f"Sono una {self.nome}"
    
    def __str__(self):
        return f"{self.nome}:   Area = {self.area():.2f},  Perimetro = {self.perimetro():.2f}"



class Cerchio(Forma):
    def __init__(self, raggio):
        super().__init__()  # Initialize the parent first
        self.nome = "Cerchio"  # Override the nome attribute
        self.raggio = raggio
    
    def area(self):
        return math.pi * self.raggio**2
    
    def perimetro(self):
        return 2 * math.pi * self.raggio

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        super().__init__()
        self.nome = "Rettangolo"
        self.base = base
        self.altezza = altezza
    
    def area(self):
        return self.base * self.altezza
    
    def perimetro(self):
        return 2 * (self.base + self.altezza)



def main():
    cerchio1 = Cerchio(4)
    circonferenza = cerchio1.perimetro()

    rettangolo = Rettangolo(6,7)
    perimetro_rettangolo = rettangolo.perimetro()

    print(cerchio1,"\n", rettangolo)


if __name__ == "__main__":
    main()