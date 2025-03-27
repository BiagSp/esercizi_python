"""
Gestione Biblioteca con classi e metodi

"""
from datetime import date, datetime

class Libro:
    def __init__(self, titolo:str, autore:str, anno_pubblicazione:date, disponibile:bool=True):
        # Initialize private attributes first
        self._titolo = None
        self._autore = autore
        self._anno_pubblicazione = anno_pubblicazione
        self._disponibilita = disponibile
        
        # Set titolo using setter for validation
        self.titolo = titolo  # This will call the setter
        
        # Additional validations
        if not autore or not isinstance(autore, str):
            raise ValueError("L'autore deve essere una stringa non vuota")
        if not isinstance(anno_pubblicazione, date):
            raise TypeError("L'anno di pubblicazione deve essere un oggetto date")
        if anno_pubblicazione > date.today():
            raise ValueError("L'anno di pubblicazione non può essere nel futuro")
    
    @property
    def titolo(self):
        return self._titolo
    
    @titolo.setter
    def titolo(self, nuovo_titolo):
        if not nuovo_titolo or not isinstance(nuovo_titolo, str):
            raise ValueError("Il titolo deve essere una stringa non vuota")
        self._titolo = nuovo_titolo
    
    @property
    def autore(self):
        return self._autore
    
    @property
    def anno_pubblicazione(self):
        return self._anno_pubblicazione
    
    @property
    def disponibile(self):
        return self._disponibilita
    
    def presta(self):
        if not self._disponibilita:
            raise Exception("Il libro non è disponibile")
        self._disponibilita = False
        return True
    
    def restituisci(self):
        if self._disponibilita:
            raise Exception("Il libro è già disponibile in biblioteca")
        self._disponibilita = True
        return True
    
    def __str__(self):
        stato = "disponibile" if self._disponibilita else "in prestito"
        return f"{self._titolo} di {self._autore} ({self._anno_pubblicazione.year}) - {stato}"
    
    def __eq__(self, other):
        if not isinstance(other, Libro):
            return False
        return (self._titolo == other._titolo and 
                self._autore == other._autore and 
                self._anno_pubblicazione == other._anno_pubblicazione)



class Biblioteca:
    def __init__(self, nome:str):
        if not nome or not isinstance(nome, str):
            raise ValueError("Il nome della biblioteca deve essere una stringa non vuota")
        
        self._nome = nome
        self._libri = []  # Initialize as an empty list
    
    @property
    def nome(self):
        return self._nome
    
    def aggiungi_libro(self, libro):  # Fixed spelling
        if not isinstance(libro, Libro):  # Check against Libro class, not the instance
            raise TypeError("Puoi aggiungere solo oggetti di tipo Libro")
        self._libri.append(libro)
        return True
    
    def cerca_per_titolo(self, titolo):
        return [libro for libro in self._libri if titolo.lower() in libro.titolo.lower()]
    
    def __str__(self):
        return f"Biblioteca '{self._nome}' con {len(self._libri)} libri"
    


def main():
    try:
        # Create books
        libro1 = Libro("Il Nome della Rosa", "Umberto Eco", date(1980, 9, 1), True)
        libro2 = Libro("1984", "George Orwell", date(1949, 6, 8), True) 
        
        # Create library
        biblioteca = Biblioteca("Biblioteca Comunale")
        
        # Add books to library
        biblioteca.aggiungi_libro(libro1)
        biblioteca.aggiungi_libro(libro2)
        
        # Print library info
        print(biblioteca)
        
        # Search books by title
        print("Ricerca per titolo 'Rosa':")
        libri_trovati = biblioteca.cerca_per_titolo("Rosa")
        if libri_trovati:
            for libro in libri_trovati:
                print(libro)
        else:
            print("Nessun libro trovato con questo titolo.")
    
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

if __name__ == "__main__":
    main()