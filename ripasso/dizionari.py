"""
Crea un dizionario in cui le chiavi sono nomi di prodotti e i valori sono le quantità disponibili. Poi:

Permetti all'utente di aggiungere nuovi prodotti.
Permetti di aggiornare le quantità.
Stampa il dizionario aggiornato.

"""
prodotti = {}


while True:
    agg_prod = input("Digita il nome del prodotto che vuoi aggiugnere:\n")

    if agg_prod in prodotti:
        print(f"Il prodotto: {agg_prod} è già presentee nella lista")
        update_quantity = input("Vuoi aggiornare la quantita? Digita Si o No:\n")
        if update_quantity.lower() == "si":
            up_qua = input("inserisci la quantità:\n")
            prodotti[agg_prod] = int(up_qua)
        else:
            print("Grazie arrivederci")
    else:
        prodotti[agg_prod] = 1
    print(prodotti)


#da migliorare (anche usando try except)
  
        