# Scrivere un programma che simuli il carrello di Amazon.
# Il programma presenta queste funzionalità:
# - Aggiungi un prodotto al carrello
# - Rimuovi un prodotto dal carrello
# - Stampa un resoconto dell attuale carrello con il costo totale.
# - Esci dal programma

# Il programma è gestito con un while principale che continua a iterare finché non si sceglie l'opzione 'esci'.
# Determinare la migliore strategia per memorizzare il carrello, ricordando che un utente può aggiungere più
# volte lo stesso prodotto. 

prodotti_amazon = {
    "Kindle Paperwhite": 129.99,
    "Echo Dot (4ª generazione)": 49.99,
    "Fire TV Stick 4K": 59.99,
    "Cuffie Bluetooth Sony WH-1000XM4": 299.99,
    "Monitor LG UltraFine 27'' 4K": 549.99,
    "Tastiera Meccanica Logitech G PRO": 129.99,
    "Hard Disk Esterno WD 2TB": 69.99,
    "Smartwatch Amazfit GTR 3": 159.99,
    "Lampadina Smart Philips Hue": 29.99,
    "Zaino per Laptop Samsonite": 89.99
}


carrello = {}

while True:
    comando = input("Digita l'operazione che desideri effettuare, tra i seguenti: Add, Remove, SubTotal, Esci\n")
    if comando.lower() == "add":
        #se l'utente digita add allora aggiungiamo il prodotto nel carrello...
        for prodotto, prezzo in prodotti_amazon.items():
            #cicliamo i prodotti per prodotto e prezzo
            print(f" - {prodotto} ({prezzo} €)")
            #stampiamo i prodotti per far scegliere all'utente quale prodotto vuole aggiungere al carrello
        prod_chosen = input("Digita il prodotto che desideri aggiungere al carrelo\n")
            
        if prod_chosen in prodotti_amazon:
            #se il prodotto scelto dall'utente è presente nei prodotti_amazon allora aggiorniamo il carrello
            if prod_chosen in carrello:
                    #se già esisteva questo prodotto nel carrello allora aumentiamo la quantità
                    carrello[prod_chosen] += 1
            else:
                #altrimenti lo aggiugniamo per la prima volta 
                    carrello[prod_chosen] = 1
                    print(f"Il prodotto '{prod_chosen}' è stato aggiunto al carrello.")
        else:
            print("Prodotto non trovato.")

    elif comando.lower() == "remove":
        #se il comando è remove rimuoviamo il prodotto dal carrello
        if not carrello:
            #se non c'è nessun prodotto nel carrello allora stampiamo il messaggio
            print("il carrello è vuoto non ci sono item da eliminare.")
            continue
        print(f"Prodotti presenti nel carrello: {carrello}")
        #stampiamo il carrello per far scegliere all'utente cosa eliminare
        prod_to_remove = input("Digita il prodotto che desideri rimuovere dal carrello\n")
        #digitiamo il prodotto che vogliamo eliminare
        if prod_to_remove in carrello:
            #se il prodotto è presente nel carrello allora lo rimuoviamo
            del carrello[prod_to_remove]
            #usiamo la funzione del di python per rimuovere il prodotto
            print(f"Il prodotto '{prod_to_remove}' è stato rimosso dal carrello.")
            #mandiamo in stampa il prodotto eliminato
    elif comando.lower() == "subtotal":
        if not carrello:
        #se non c'è nessun prodotto nel carrello allora stampiamo il messaggio
            print("il carrello è vuoto")
            continue
        print(f"Prodotti presenti nel carrello: {carrello}")
        #stampiamo il carrello per far scegliere all'utente cosa calcolare
        for prodotti, quantità in carrello.items():
        #stampiamo i prodotti per far scegliere all'utente cosa calcolare
            print(f" - {prodotti}: {quantità} x {prodotti_amazon[prodotti]} ��� = {quantità * prodotti_amazon[prodotti]} ���")
            #calcoliamo il prezzo totale del carrello
    elif comando.lower() == "esci":
        print("Arrivederci!")
        break






"""# Il carrello sarà un dizionario con il nome del prodotto come chiave e la quantità come valore
carrello = {}

while True:
    # Rimuoviamo spazi e rendiamo minuscolo l'input per evitare errori di formattazione
    comando = input("Digita una delle seguenti parole: Add, Remove, Total, Esci: ").strip().lower()

    if comando == "add":
        print("Prodotti disponibili:")
        for prodotto, prezzo in prodotti_amazon.items():
            print(f" - {prodotto} ({prezzo} €)")
        prodotto_scelto = input("Inserisci il nome del prodotto da aggiungere: ").strip()
        if prodotto_scelto in prodotti_amazon:
            if prodotto_scelto in carrello:
                carrello[prodotto_scelto] += 1
            else:
                carrello[prodotto_scelto] = 1
            print(f"Il prodotto '{prodotto_scelto}' è stato aggiunto al carrello.")
        else:
            print("Prodotto non trovato.")
  
    elif comando == "remove":
        if not carrello:
            print("Il carrello è vuoto, niente da rimuovere.")
        else:
            print("Prodotti attualmente nel carrello:")
            for prodotto, quantita in carrello.items():
                print(f" - {prodotto}: {quantita}")
            prodotto_da_rimuovere = input("Inserisci il nome del prodotto da rimuovere: ").strip()
            if prodotto_da_rimuovere in carrello:
                if carrello[prodotto_da_rimuovere] > 1:
                    carrello[prodotto_da_rimuovere] -= 1
                else:
                    del carrello[prodotto_da_rimuovere]
                print(f"Il prodotto '{prodotto_da_rimuovere}' è stato rimosso dal carrello.")
            else:
                print("Il prodotto non è presente nel carrello.")

    elif comando == "total":
        if not carrello:
            print("Il carrello è vuoto.")
        else:
            totale = 0
            print("Resoconto del carrello:")
            for prodotto, quantita in carrello.items():
                prezzo = prodotti_amazon[prodotto]
                sottototale = prezzo * quantita
                totale += sottototale
                print(f" - {prodotto}: {quantita} x {prezzo} € = {sottototale} €")
            print(f"Totale carrello: {totale} €")

    elif comando == "esci":
        print("Programma terminato. Arrivederci!")
        break

    else:
        print("Comando non valido. Riprova.")
"""