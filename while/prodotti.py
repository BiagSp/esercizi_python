"""
Creare una lista prodotti ed implemetare le seguenti funzioni:
- aggiunta e rimozione prodotti
-  Ordinazione multipla e raggruppamento
    Descrizione:
    Hai una lista di ordini in cui alcuni prodotti possono apparire più volte. Raggruppa gli ordini per prodotto e 
    conta quante volte ciascun prodotto è stato ordinato. Poi confronta il totale con le             
    quantità in inventario e stampa quali ordini possono essere soddisfatti e quali no.
- Simulazione di cassa automatica
- Rifornimento automatico
  Descrizione:
  Estendi l'esercizio dell'inventario aggiungendo una funzione di rifornimento: quando la quantità di un prodotto scende 
  sotto una certa soglia, il programma avvisa che è necessario ordinare altro stock.
"""

prodotti = ["mela", "banana", "arancia", "pera"]
quantità = [10, 12, 14, 15]
prezzo = [1.3, 3, 4, 5.5]


#Inizializziamo il metodo per aggiugnere un nuovo prodotto
while True:
    add_prod = input("Digita il prodotto che desiredi aggiungere, altrimenti digita fine per uscire:\n")
    #Aggiungiamo il nuovo prodotto o nel caso usciamo dal metodo
    if add_prod == "fine":
        break
    #Controlliamo se il prodotto è già presente nella lista
    elif add_prod in prodotti:
        continue
    #Se il prodotto non è presente nella lista, lo aggiungiamo
    else:
        prodotti.append(add_prod)
        quantity =  float(input("Digita la quantità del prodotto che stai aggiungendo:\n"))
        quantità.append(quantity)
        price = float(input("Digita il prezzo del prodotto che stai aggiungendo:\n"))
        prezzo.append(price)
        print("Prodotto aggiunto correttamente!\n", prodotti, quantità, prezzo)
        #oltre al prodotto aggiunto aggiungiamo anche la quantità e il suo prezzo



#inizializziamo il metodo per eliminare un prodotto specifico
while True:
    delete_prod = input("Digita il prodotto che desideri rimuovere, altrimenti digita fine per uscire:\n")
    #anche qui se vogliamo uscire dal metodo controlliamo la digitura e usciamo dal metodo
    if delete_prod == "fine":
        break
    #se il prodotto è presente nella lista, lo eliminiamo
    elif delete_prod in prodotti:
        #ciclo per trovare il prodotto da eliminare
        #il ciclo usa una variabile falsa (poteva anche essere inizializzata a -1)
        #il ciclo itera fin quando la variabile delete_prod è uguale all'indice prodotti[x]
        #se è uguale la variabile find diventa True e partono le altre istruzioni
        find = False
        x = 0
        while x < len(prodotti):
            if delete_prod == prodotti[x]:
                find = True
                del prodotti[x]
                del quantità[x]
                del prezzo[x]
                break
            x += 1
    else:
        print("Prodotto non trovato!")
        continue
    if find:
        print("Prodotto rimosso correttamente!\n", prodotti, quantità, prezzo)
        #oltre al prodotto rimosso aggiungiamo anche la quantità e il suo prezzo
        

#inizializziamo il metodo per ordinare i prodotti
while True:
    order = input("Digitail prodotto che desideri ordinare, altrimenti digita fine per uscire:\n").strip()
    #Se vogliamo uscire dal metodo controlliamo la digitura e usciamo dal metodo
    if order == "fine":
        break
    else:
        find = False
        # Ciclo per trovare il prodotto da ordinare
        # il ciclo usa una variabile falsa (poteva anche essere inizializzata a -1)
        # il ciclo itera fin quando la variabile order è uguale all'indice prodotti[x]
        # se è uguale la variabile find diventa True e partono le altre istruzioni       
        x = 0
        while x < len(prodotti):
            if order == prodotti[x]:
                find = True
                quantity = int(input("Digita la quantità del prodotto che desideri ordinare:\n"))
                # se la quantità del prodotto è minore della quantità richiesta, il programma avvisa che la quantità non è disponibile e si ferma
                if quantity > quantità[x]:
                    print(f"Quantità non disponibile! Quantità disponibile: {quantità[x]}")
                    break
                else:
                    # se la quantità del prodotto è maggiore della quantità richiesta, il programma sottrae la quantità richiesta dalla quantità del prodotto
                    quantità[x] -= quantity
                    price = prezzo[x] * quantity
                    # stampa la quantità rimanente e il prezzo totale
                    print("Prodotto ordinato correttamente! Quantità rimanente:", quantità[x], "Prezzo totale:", price)
                    break
            x += 1
        if not find:
            print("Prodotto non trovato!")
            continue


# Supponendo che le liste 'prodotti' e 'quantità' siano già definite

soglia = 3  # Definiamo la soglia sotto cui avvisare il riordino

# Ciclo per controllare e riordinare i prodotti con quantità bassa
i = 0
while i < len(prodotti):
    if quantità[i] <= soglia:
        print(f"Il prodotto {prodotti[i]} sta per terminare: quantità attuale {quantità[i]}. Devi ordinarne di più.")
        new_quantity = int(input("Digita la quantità che vuoi riordinare:\n"))
        quantità[i] += new_quantity
        print(f"Quantità aggiornata: la quantità del {prodotti[i]} è stata modificata correttamente a {quantità[i]}.")
    i += 1


