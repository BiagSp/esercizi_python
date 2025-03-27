"""
Obiettivo: Creare una classe che gestisca una biblioteca di libri.
Requisiti:

Crea una classe Libro con attributi: titolo, autore, anno di pubblicazione, disponibile (booleano)
Crea una classe Biblioteca che permetta di:

Aggiungere libri
Rimuovere libri
Cercare libri per titolo o autore
Prestare un libro (cambia lo stato di disponibilità)
Restituire un libro



Suggerimenti iniziali:

Inizia definendo la classe Libro con un costruttore (init)
Per la classe Biblioteca, pensa a come memorizzare la collezione di libri (una lista?)

"""

class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione, disponibile:bool):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = disponibile
        
    def __str__(self):
        return f"Il libro con titolo: {self.titolo} autore: {self.autore} è {self.disponibile}"
    
    
    
class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        return f"Il libro {libro.titolo} aggiunto alla biblioteca"
    
    def cerca_libro(self, termine, per_autore=False):
        risultati = []
        for libro in self.libri:
            if per_autore and termine.lower() in libro.autore.lower():
                risultati.append(libro)
            elif not per_autore and termine.lower() in libro.titolo.lower():
                risultati.append(libro)
        return risultati
    
    def rimuovi_libro(self, titolo):
        for i, libro in enumerate(self.libri):
            if libro.titolo == titolo:
                del self.libri[i]
                return f"Libro '{titolo}' rimosso dalla biblioteca"
        return f"Libro '{titolo}' non trovato nella biblioteca"
    
    
    def presta_libro(self, titolo):
        for libro in self.libri:
            if libro.titolo == titolo and libro.disponibile:
                libro.disponibile = False
                return f"Libro {titolo} prestato."
            elif libro.titolo == titolo and not libro.disponibile:
                return f"Libro {titolo} non disponibile per il prestito"
        return f"Libro {titolo} non trovato in biblioteca."
    
    def restituisci_libro(self, titolo):
        for libro in self.libri:
            if libro.titolo == titolo and not libro.disponibile:
                libro.disponibile = True
                return f"Libro {titolo} restituito"
            elif libro.titolo == titolo and libro.disponibile:
                return f"Il libro {titolo} è già stato restituito"
        return f"Libro {titolo} non trovato in biblioteca"
    
    
    def visualizza_libri(self):
        if not self.libri:
            return f"La biblioteca è vuota"
         
        risultato = "Libri nella biblioteca:\n"
        for libro in self.libri:
            risultato += f"- {libro.titolo} di {libro.autore} ({libro.anno_pubblicazione}): {'disponibile' if libro.disponibile else 'non disponibile'}\n"            
        return risultato

def main():
    # Creo alcuni libri di esempio
    libro1 = Libro("prova", "giana", 2909, True)
    libro2 = Libro("test", "emingway", 1878, True)
    libro3 = Libro("Il nome della rosa", "Umberto Eco", 1980, True)
    
    biblioteca = Biblioteca()
    
    print(biblioteca.aggiungi_libro(libro1))
    print(biblioteca.aggiungi_libro(libro2))
    print(biblioteca.aggiungi_libro(libro3))
    
    # visualizzare tutti i libri
    print(biblioteca.visualizza_libri())
    
    prova_ricerca = biblioteca.cerca_libro("prova")
    
    for libro in prova_ricerca:
        print(f"- {libro.titolo} di {libro.autore}")
    
    
    prova_ricerca = biblioteca.cerca_libro("eco", per_autore=True)
    for libro in prova_ricerca:
        print(f"- {libro.titolo} di {libro.autore}")
    
    
    print(biblioteca.presta_libro("test"))
    
    print(biblioteca.restituisci_libro("test"))
    
    print(biblioteca.rimuovi_libro("prova"))
    
    
if __name__ == "__main__":
    main()