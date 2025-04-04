"""
Gestore di Note Testuali
Crea un'applicazione che permetta di aggiungere, visualizzare, 
modificare ed eliminare note. Questo progetto ti farà praticare
la manipolazione dei file, la persistenza dei dati e la creazione 
di un'interfaccia utente testuale più sofisticata.

"""
from datetime import date, datetime
import json



class Note:
    def __init__(self, titolo, description, data:date):
        self.titolo = titolo
        self.description = description
        self.data = data

    def __str__(self):
        return f"La nota con titolo: {self.titolo}\n Descrizione: {self.description}\n Generata il: {self.data.strftime('%d/%m/%Y')}"
    
    

class GestoreNote:
    def __init__(self, percorso_file="note.json"):
        self.note = {}
        
        self.percorso_file = percorso_file
        
        if percorso_file:
            try:
                self.carica_note()
            except FileNotFoundError:
                print(f"Nessun file di note trovati in {self.percorso_file} verrà creato un nuovo file")
                
    def carica_note(self):
        
        try:
            with open(self.percorso_file, "r") as file:
                data_json = json.load(file)
                
                self.note = {}
                
                for titolo, dettagli in data_json.items():
                    data_str = dettagli["data"]
                    data_obj = datetime.strptime(data_str, "%Y-%m-%d").date()
                    
                    nota = Note(titolo, dettagli["descrizione"], data_obj)
                    
                    self.note[titolo] = nota
                    
        except FileNotFoundError:
            with open(self.percorso_file, "w") as file:
                json.dump({}, file)
                self.note = {}
                return 
                
                
    def salva_note(self):
        dati_per_json = {}
        
        for titolo, nota_obj in self.note.items():
            # Convertiamo la data in stringa
            data_str = nota_obj.data.strftime("%Y-%m-%d")
            
            # Creiamo un dizionario per questa nota
            dati_nota = {
                "descrizione": nota_obj.description,
                "data": data_str
            }
            
            # Aggiungiamo questa nota al dizionario principale
            dati_per_json[titolo] = dati_nota
        
        # Scriviamo il dizionario nel file
        with open(self.percorso_file, "w") as file:
            json.dump(dati_per_json, file, indent=4)  # indent=4 rende il file più leggibile
            
    
    def aggiungi_nota(self, titolo, descrizione, data=None):
        
        
        if data is None:
            data = date.today()
        elif isinstance(data, str):
            data = datetime.strptime(data, "%Y-%m-%d").date()
                    
        
        if titolo in self.note:
            raise ValueError(f"Esiste già una nota con il titolo: {titolo}")

        nuova_nota = Note(titolo, descrizione, data)
        
        
        self.note[titolo] = nuova_nota
        
        self.salva_note()
        
        return nuova_nota
    
    def cerca_note(self, titolo=None, data=None):
        risultati = {}
        
        # Se entrambi i parametri sono None, restituiamo un dizionario vuoto
        if titolo is None and data is None:
            return {}
        
        # Iteriamo su tutte le note
        for chiave_nota, nota in self.note.items():
            
            # Flag per tenere traccia se la nota corrisponde ai criteri
            corrisponde = True
            
            # Controllo sul titolo (se specificato)
            if titolo is not None:
                # Ricerca case-insensitive e parziale
                if titolo.lower() not in chiave_nota.lower():
                    corrisponde = False
            
            # Controllo sulla data (se specificata)
            if data is not None:
                # Assicuriamoci che data sia un oggetto date
                if isinstance(data, str):
                    data = datetime.strptime(data, "%Y-%m-%d").date()
                    
                # Verifichiamo se le date corrispondono
                if nota.data != data:
                    corrisponde = False
            
            # Se la nota corrisponde a tutti i criteri specificati, la aggiungiamo ai risultati
            if corrisponde:
                risultati[chiave_nota] = nota
    
        return risultati
    
    def modifica_note(self, titolo_originale, nuovo_titolo=None, nuova_descrizione=None):
        if titolo_originale not in self.note:
            raise ValueError(f"Nessuna nota trovata con il titolo {titolo_originale}")
        
        nota = self.note[titolo_originale]
        
        if nuovo_titolo is not None and nuovo_titolo != titolo_originale:
            if nuovo_titolo in self.note:
                raise ValueError(f"Hai già sostituito questo titolo con quello nuovo {nuovo_titolo}")
            
            self.note[nuovo_titolo] = nota
            del self.note[titolo_originale]
            
        if nuova_descrizione is not None:
            chiave_nota = nuovo_titolo if nuovo_titolo is not None else titolo_originale
            self.note[chiave_nota].description = nuova_descrizione
            
        
        self.salva_note()
        
        return self.note[nuovo_titolo if nuovo_titolo is not None else titolo_originale]
    
    def elimina_nota(self, titolo):
        if titolo not in self.note:
            raise ValueError(f"Nessuna nota trovata con il titolo {titolo}")
        
        nota_eliminata = self.note.pop(titolo)
        
        self.salva_note()
        
        return nota_eliminata
    
    
    
    def visualizza_tutte_note(self):
        # Se non ci sono note, restituisci un dizionario vuoto
        if not self.note:
            return {}
        
        # Altrimenti restituisci tutte le note
        return self.note
    
    
    
def main():
    gestore = GestoreNote()
    
    while True:
        print("\n=== Gestore Note ===")
        print("1. Visualizza tutte le note")
        print("2. Cerca note")
        print("3. Aggiungi nota")
        print("4. Modifica nota")
        print("5. Elimina nota")
        print("0. Esci")
        
        scelta = input("\nSeleziona un'opzione: ")
        
        if scelta == "1":
            # Visualizza tutte le note
            note = gestore.visualizza_tutte_note()
            if not note:
                print("Non ci sono note salvate.")
            else:
                print("\n=== Tutte le Note ===")
                for titolo, nota in note.items():
                    print(f"\n{nota}")
                    print("-" * 30)
        
        elif scelta == "2":
            # Cerca note
            print("\n=== Cerca Note ===")
            print("Lascia vuoto se non vuoi filtrare per quel campo")
            
            titolo = input("Cerca per titolo: ")
            data_str = input("Cerca per data (YYYY-MM-DD): ")
            
            # Conversione dei parametri vuoti in None
            titolo = titolo if titolo else None
            data_str = data_str if data_str else None
            
            risultati = gestore.cerca_note(titolo, data_str)
            
            if not risultati:
                print("Nessuna nota trovata con i criteri specificati.")
            else:
                print(f"\nTrovate {len(risultati)} note:")
                for titolo, nota in risultati.items():
                    print(f"\n{nota}")
                    print("-" * 30)
        
        elif scelta == "3":
            # Aggiungi nota
            print("\n=== Aggiungi Nota ===")
            
            titolo = input("Titolo: ")
            descrizione = input("Descrizione: ")
            data_str = input("Data (YYYY-MM-DD, lascia vuoto per oggi): ")
            
            # Conversione dei parametri vuoti
            data = None if not data_str else data_str
            
            try:
                nuova_nota = gestore.aggiungi_nota(titolo, descrizione, data)
                print(f"\nNota aggiunta con successo:\n{nuova_nota}")
            except ValueError as e:
                print(f"Errore: {e}")
        
        elif scelta == "4":
            # Modifica nota
            print("\n=== Modifica Nota ===")
            
            titolo_originale = input("Titolo della nota da modificare: ")
            
            if titolo_originale not in gestore.note:
                print(f"Errore: Nessuna nota trovata con il titolo '{titolo_originale}'")
                continue
            
            print("\nInserisci i nuovi dati (lascia vuoto per mantenere i valori attuali)")
            
            nuovo_titolo = input("Nuovo titolo: ")
            nuova_descrizione = input("Nuova descrizione: ")
            
            # Conversione dei parametri vuoti in None
            nuovo_titolo = nuovo_titolo if nuovo_titolo else None
            nuova_descrizione = nuova_descrizione if nuova_descrizione else None
            
            try:
                nota_modificata = gestore.modifica_nota(titolo_originale, nuovo_titolo, nuova_descrizione)
                print(f"\nNota modificata con successo:\n{nota_modificata}")
            except ValueError as e:
                print(f"Errore: {e}")
        
        elif scelta == "5":
            # Elimina nota
            print("\n=== Elimina Nota ===")
            
            titolo = input("Titolo della nota da eliminare: ")
            
            try:
                nota_eliminata = gestore.elimina_nota(titolo)
                print(f"\nNota eliminata con successo:\n{nota_eliminata}")
            except ValueError as e:
                print(f"Errore: {e}")
        
        elif scelta == "0":
            # Esci
            print("\nArrivederci!")
            break
        
        else:
            print("\nOpzione non valida. Riprova.")

if __name__ == "__main__":
    main()