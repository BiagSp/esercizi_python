"""
Crea una classe Studente con i seguenti attributi:

Nome
Cognome
Voto
Aggiungi un metodo per verificare se lo studente è promosso (voto >= 6) e stampa il risultato.

"""

class Studente:
    def __init__(self, nome, cognome, voto: float):
        self.nome = nome
        self.cognome = cognome
        self.voto = voto
    
    def is_promoted(self):
        return self.voto >= 6
    
    def print_status(self):
        if self.is_promoted():
            print(f"Lo studennte {self.nome} è stato promosso con voto {self.voto}")
        else:
            print(f"lo studente {self.nome} non è stato promosso. Voto {self.voto}")

    def __str__(self):
        if self.is_promoted():
            return f"Lo studente {self.nome} {self.cognome} è stato promosso con voto: {self.voto}"
        else:
            return f"Lo studente {self.nome} {self.cognome} non è stato promosso. Voto: {self.voto}"
     
def main():
    studente1 = Studente("Prova", "test", 8.2)
    studenti = {
        "std1" : ["nome", "cognome", 5.6],
        "std2" : ["test", "test2", 8]
    }

    std = [Studente(dati[0], dati[1], dati[2]) for dati in studenti.values()]
    for stud in std:
        print(stud)


if __name__ == "__main__":
    main()
