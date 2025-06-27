"""
Esercizio 2: Lista della spesa (Intermedio-Base)
Problema: Crea un programma che gestisca una lista della spesa. L'utente deve poter:

Aggiungere un elemento alla lista
Rimuovere un elemento dalla lista
Visualizzare tutti gli elementi
Uscire dal programma

Discussione dell'approccio:
Questo esercizio introduce i cicli e la gestione di strutture dati base. Possiamo:

Creare una lista vuota all'inizio
Implementare un ciclo principale che continui fino a quando l'utente non sceglie di uscire
Utilizzare condizionali per eseguire diverse azioni in base all'input dell'utente

Come gestiresti il menu delle opzioni? Quali controlli dovresti implementare per gestire casi come rimuovere un elemento che non esiste?

"""



prodotti_disponibili = {
    "Frutta": {
        "Mele": 1.20,
        "Banane": 1.50,
        "Pere": 1.80,
        "Arance": 2.00
    },
    "Verdura": {
        "Carote": 0.90,
        "Zucchine": 1.40,
        "Pomodori": 2.20,
        "Lattuga": 1.10
    },
    "Latticini": {
        "Latte": 1.60,
        "Formaggio": 3.50,
        "Yogurt": 1.00,
        "Burro": 2.30
    }
}



def spesa(item):
    carrello_spesa = {}
    
    while True:
        # Mostra il menu ad ogni iterazione
        print("\n=== MENU LISTA DELLA SPESA ===")
        print("1. Aggiungi Prodotto")
        print("2. Rimuovi prodotto")
        print("3. Visualizza totale carrello")
        print("4. Esci")


        scelta_utente = input("\nScegli l'operazione da effettuare (1-4): ")
        
        if scelta_utente == "1":
            print(f"="*20)
            print("Prodotti disponibili")
            print(f"="*20)
            # cicliamo le categorie presenti
            for i, categoria in enumerate(item.keys(),1):
                print(f"{i}. {categoria}")
                
            scelta_pcategoria= input("Inserisci la categoria che desideri:\n")
            
            try:
                scelta_pcategoria = int(scelta_pcategoria)
                if 1 <= scelta_pcategoria <= len(item):
                    categoria_selezionata = list(item.keys())[scelta_pcategoria-1]
                    
                    prodotti_categoria = item[categoria_selezionata]
                    
                    print(f"Prodotti nella presenti nella categoria: {categoria_selezionata}:")
                    for i, (prodotto, prezzo) in enumerate(prodotti_categoria.items(),1):
                        print(f"{i}. Prodotto {prodotto} - Prezzo: {prezzo:.2f}")
                        
                while True:
                    try:
                        scelta_prodotto = int(input("scegli il prodotto che vuoi inserire nel carrello:\n"))
                        if 1 <= scelta_prodotto <= len(prodotti_categoria):
                            break
                        else:
                            print("Numero non valido")
                    except ValueError:
                        print("Inserisci un numero valido")  
                        
                nome_prodotto = list(prodotti_categoria.keys())[scelta_pcategoria-1]
                prezzo_prodotto = prodotti_categoria[nome_prodotto]
                
                while True:
                    quantita = float(input(f"Inserisci la quantità del Prodotto: {nome_prodotto} che desideri aggiungere al carrelo:\n"))
                    if quantita > 0:
                        break
                    else:
                        print("la quantità deve essere maggiore di 0")
                    
                
                carrello_spesa[nome_prodotto] = {
                    "quantità" : quantita,
                    "prezzo": prezzo_prodotto,
                    "categoria": categoria_selezionata
                }
                
                print(f"Aggiunto {quantita}, {nome_prodotto} al carrello; totale: {quantita * prezzo_prodotto}")
                
                
                
            except ValueError:
                print("inserisci un numero valido")


            
            
            
        
        elif scelta_utente == "2":

            pass
        
        elif scelta_utente == "3":

            pass
        
        elif scelta_utente == "4":
            print("Grazie per aver utilizzato il programma. Arrivederci!")
            break
        
        else:
            print("Scelta non valida. Riprova.")
            
            
spesa(prodotti_disponibili)