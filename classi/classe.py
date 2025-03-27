"""
Esercizio 4: Polimorfismo
Obiettivo: Comprendere il concetto di polimorfismo attraverso metodi comuni in classi diverse.

Istruzioni:

Crea una classe base Animale con un metodo verso() (può essere vuoto o lanciare un messaggio generico).
Crea due sottoclassi: Cane e Gatto, ciascuna con la propria implementazione del metodo verso() (es. "Bau" per il cane e "Miao" per il gatto).
Scrivi una funzione fai_verso(animale) che, dato un oggetto di tipo Animale, chiama il metodo verso().
Crea una lista di animali (istanze di Cane e Gatto) e usa la funzione per stampare il verso di ciascun animale.

"""


class Animale:
    def verso(self):
        pass

class Cane(Animale):
    def verso(self):
        print("Bau")


class Gatto(Animale):
    def verso(self):
        print("Miao")


def fai_verso(animal):
    animal.verso()



cane = Cane()
gatto = Gatto()

animali = [cane, gatto] 

for animal in animali:
    fai_verso(animal)


