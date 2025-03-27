# Esercizio: Creazione di una lista di promozioni
#
# Hai tre liste che rappresentano:
# 1. `studenti` - I nomi degli studenti di una classe.
# 2. `voti` - I voti corrispondenti a ciascun studente.
# 3. `promossi` - Una lista vuota che conterrà i nomi degli studenti promossi.
#
# Scrivi un programma che:
# 1. Utilizzi un ciclo `while` per scorrere la lista degli `studenti` e dei loro voti.
# 2. Controlli i voti degli studenti:
#    - Se un voto è maggiore o uguale a 6, aggiungi lo studente alla lista `promossi`.
#    - Altrimenti, stampa un messaggio indicando che lo studente non è stato promosso.
# 3. Al termine, stampa la lista degli studenti promossi e di quelli non promossi.
#
# Dati iniziali:
# studenti = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
# voti = [7, 5, 6, 8, 4]
# promossi = []


studenti = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
voti = [7, 5, 6, 8, 4]
promossi = []
nonPromossi = []

i = 0

while i < len(studenti): 
    #cicliamo la lista studenti
    if voti[i] < 6:
        #se il voto è minore di 6, lo aggiungiamo alla lista nonPromossi
        print(f"studente {studenti[i]} Non ammesso, voto: {voti[i]}")
        nonPromossi.append(studenti[i])
        #aggiungiamo alla lista nonPromossi
    else:
        #se il voto è maggiore o uguale a 6, lo aggiungiamo alla lista promossi
        print(f"studente {studenti[i]} Ammesso, voto: {voti[i]}")
        promossi.append(studenti[i])
    i += 1

print(promossi, nonPromossi)