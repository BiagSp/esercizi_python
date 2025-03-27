"""
Date due liste: una lista di numeri interi (numeri) e una lista di parole (parole), crea una lista combinata in cui:

Se la lunghezza della parola all’indice i è maggiore del valore numerico in numeri[i], inserisci la parola ripetuta numeri[i] volte.
Altrimenti, inserisci il prodotto tra il numero e il numero di caratteri della parola (ossia: numeri[i] * len(parole[i])).
Successivamente:

Estrai una sottolista con gli elementi agli indici dispari.
Dalla sottolista, filtra solo gli elementi che sono stringhe.

"""
numeri = [3, 5, 3, 4, 5, 6]
parole = ["uno", "due", "tre", "quattro", "cinque", "sei"]
#creiamo una nuova lista usando list comprehension
#se numeri[i] > di parole[i] allora numeri[i] * len(parole[i]), altrimenti parole[i] * numeri[i]
new_list = [numeri[i] * len(parole[i]) if len(parole[i]) <= numeri[i] else parole[i] * numeri[i] for i in range(len(numeri))]
#estraiamo una sottolista che contiene solo gli elementi agli indici dispari
sottolista = new_list[1::2]
#proviamo ad esercitarci sulla list comprehension con nuovi parametri
list2 = [numeri[i] * numeri[i] - 1 if len(parole[i]) == numeri[i] else parole[i] * numeri[i] for i in range(len(numeri))]
print(list2)
#print(new_list)
#print(sottolista)
