"""
Obiettivo: Creare un parser per analizzare dati in formato CSV.
Requisiti:

Crea una classe CSVParser che:

Legga un file CSV
Converta i dati in una struttura utilizzabile (lista di dizionari)
Permetta di eseguire query semplici sui dati (es. filtrare righe, calcolare medie)
Salvi i risultati delle query in un nuovo file CSV

"""
import csv

class CSVParser:
    def __init__(self, file_path):
        """
        Inizializza il parser con il percorso del file CSV.
        
        Args:
            file_path (str): percorso del file CSV da analizzare
        """
        self.file_path = file_path
        self.headers = []
        self.data = []
        
    def leggi_csv(self):
        """
        Legge il file CSV e converte i dati in una lista di dizionari.
        Ogni riga del CSV diventa un dizionario dove le chiavi sono le intestazioni.
        """
        self.data = []  # Resetta la lista dei dati
        
        with open(self.file_path, "r", encoding="utf-8") as file:
            # Legge la prima riga per ottenere le intestazioni
            header_line = file.readline().strip()
            self.headers = [h.strip() for h in header_line.split(',')]
            
            # Legge il resto delle righe per i dati
            for line in file:
                values = [v.strip() for v in line.strip().split(',')]
                if len(values) == len(self.headers):
                    row_dict = {}
                    for i, header in enumerate(self.headers):
                        row_dict[header] = values[i]
                    self.data.append(row_dict)
        
        return self.data
            
    
    
    
        
    def filtra_dati(self, colonna, valore):
        """
        Filtra i dati in base al valore di una colonna specifica.
        
        Args:
            colonna (str): nome della colonna su cui filtrare
            valore: valore da cercare nella colonna
            
        Returns:
            list: lista di dizionari contenenti solo le righe che soddisfano il filtro
        """
        # Qui implementerai il filtro sui dati
        if colonna not in self.headers:
            print(f"errore la colonna {colonna} non esiste")
            return []
        
        #filtriamo i dizionari
        risultati_filtrati = []
        
        for riga in self.data:
            if riga[colonna] == valore:
                risultati_filtrati.append(riga)
        return risultati_filtrati
        
        
    def calcola_media(self, colonna):
        """
        Calcola la media dei valori in una colonna numerica.
        
        Args:
            colonna (str): nome della colonna su cui calcolare la media
            
        Returns:
            float: media dei valori nella colonna o None se non è possibile calcolarla
        """
        # Verifica che la colonna esista
        if colonna not in self.headers:
            print(f"Errore: la colonna '{colonna}' non esiste")
            return None
        
        somma = 0
        conteggio = 0
        
        for riga in self.data:
            try:
                valore = riga[colonna]
                valore_numerico = float(valore)
                somma += valore_numerico
                conteggio += 1
            except (ValueError, TypeError):
                # Ignora valori che non possono essere convertiti in numeri
                print(f"Avviso: valore '{valore}' nella colonna '{colonna}' non è numerico e verrà ignorato")
                continue
        
        if conteggio == 0:
            print(f"Nessun valore numerico trovato nella colonna '{colonna}'")
            return None
            
        media = somma / conteggio
        return f"{media:.2f}"
        
        
        
        
        
    def salva_risultati(self, risultati, file_output):
        """
        Salva una lista di dizionari in un nuovo file CSV.
        
        Args:
            risultati (list): lista di dizionari da salvare
            file_output (str): percorso del file di output
        """
        # Qui implementerai il salvataggio dei risultati
        if not risultati:
            print("Nessun risultato da salvare")
            return
        
        
         # Apre il file in modalità scrittura
        with open(file_output, "w", encoding = "utf-8") as file:
            # Determina le intestazioni (prendiamo le chiavi dal primo dizionario)
            headers = list(risultati[0].keys())
            
            # Scrivere la riga di intestazione
            file.write(",".join(headers) + '\n')
            
            # Scrivere ogni riga di dati
            for riga in risultati:
                # Estrarre i valori nell'ordine delle intestazioni
                valori = [str(riga.get(header, "")) for header in headers]
                # Scrivere la riga nel file
                file.write(",".join(valori) + '\n')
                
            print(f"Risultati salvati con successo nel file {file_output}")
            


def main():
    # Creare un'istanza del parser
    parser = CSVParser("vendite.csv")
    
    # Leggi il csv
    parser.leggi_csv()
    print(f"Headers: {parser.headers}")
    print(f"Numero di righe caricate: {len(parser.data)}")
            
    # Mostra alcuni dati di esempio
    print("\nPrime 3 righe di dati:")
    for i, riga in enumerate(parser.data[:3]):
        print(f"riga {i+1}: {riga}")
            

    # Filtra i dati
    colonna_filtro = "prodotto" 
    valore_filtro = "Laptop"
    risultati_filtro = parser.filtra_dati(colonna_filtro, valore_filtro)
    print(f"\n Righe trovarte con {colonna_filtro} = {valore_filtro}: {len(risultati_filtro)}")   
    for i in risultati_filtro:
        print(i)        
        
    # Calcolare la media del prezzo
    colonna_media = "prezzo"
    
    media_prezzo = parser.calcola_media(colonna_media)
    print(f"\nMedia della colonna {colonna_media}: {media_prezzo}")
    
    # Calcolare media delle quantità
    colonna_media = "quantità"
    media_quantita = parser.calcola_media(colonna_media)
    print(f"\nMedia della colonna {colonna_media}: {media_quantita}")
    
    # Salviamo i risultati filtrati e calcolati
    
    parser.salva_risultati(risultati_filtro, "laptop_filtrati.csv")
    
if __name__ == "__main__":
    main()