"""
Chiedi all’utente una parola e costruisci un dizionario in cui le chiavi sono le lettere della parola
 e i valori sono il numero di volte che appaiono nella parola.

"""

parola = input("Digita una parola:\n")

count = {}

#versione didattica
for carattere in parola:
    if carattere in count:
        count[carattere] += 1
    else: 
        count[carattere] = 1


print(count)


#versione elgante
conteggio = {}

for carattere in parola:
    conteggio[carattere] = conteggio.get(carattere, 0) + 1

print(conteggio)