"""
Crea un programma che legge un file CSV contenente dati di vendita e calcola il totale delle vendite per ogni prodotto.

"""

import csv

def leggi_file_vendite(nome_file):
    vendite_per_prodotto = {}

    try:
        with open(nome_file, 'r', encoding='utf-8') as file:
            lettore_csv = csv.DictReader(file)
            
            # Debug: stampa i nomi delle colonne
            print(f"Colonne trovate nel CSV: {lettore_csv.fieldnames}")
            
            for riga in lettore_csv:
                # Stampa la prima riga per debug
                if vendite_per_prodotto == {}:  # Solo per la prima riga
                    print(f"Prima riga del CSV: {dict(riga)}")
                
                prodotto = riga.get('prodotto')
                
                # Gestione della colonna quantità
                try:
                    quantita = int(riga['quantità'])
                except KeyError:
                    # Prova senza accento
                    try:
                        quantita = int(riga['quantita'])
                    except KeyError:
                        print(f"Chiavi disponibili: {riga.keys()}")
                        raise KeyError("Colonna 'quantità' o 'quantita' non trovata")
                
                # Gestione della colonna prezzo
                try:
                    prezzo = float(riga['prezzo'])
                except KeyError:
                    print(f"Chiavi disponibili: {riga.keys()}")
                    raise KeyError("Colonna 'prezzo' non trovata")
                
                valore = quantita * prezzo
                
                if prodotto in vendite_per_prodotto:
                    vendite_per_prodotto[prodotto] += valore
                else:
                    vendite_per_prodotto[prodotto] = valore
                    
        return vendite_per_prodotto
    
    except UnicodeDecodeError:
        print("Errore di codifica nel file. Provo con una codifica diversa...")
        # Prova con una codifica alternativa
        with open(nome_file, 'r', encoding='latin-1') as file:
            # Ripeti il codice di lettura qui...
            pass

def mostra_risultati(vendite_per_prodotto):
    print("\nTotale vendite per prodotto:")
    print("------------------------")
    for prodotto, totale in vendite_per_prodotto.items():
        print(f"{prodotto}: €{totale:.2f}")

def main():
    nome_file = 'vendite.csv'
    try:
        vendite = leggi_file_vendite(nome_file)
        mostra_risultati(vendite)
    except FileNotFoundError:
        print(f"Il file '{nome_file}' non è stato trovato. Verificare il percorso del file.")
    except Exception as e:
        print(f"Si è verificato un errore: {str(e)}")

if __name__ == '__main__':
    main()