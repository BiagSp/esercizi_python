# Esercizio Extra Difficile: Manipolazione avanzata di liste con list comprehension e slicing
# ------------------------------------------------------------------------------------------
# Dati tre elenchi:
# 1. Una lista di numeri interi (`numeri`).
# 2. Una lista di parole (`parole`).
# 3. Una lista di booleani (`flag`), che indica quali elementi devono essere presi dalla lista `numeri`
#    e quali dalla lista `parole`.
#
# Obiettivo:
# - Crea una nuova lista in cui:
#   - Se `flag[i]` è **True**, inserisci `numeri[i] * 2` (raddoppia il valore).
#   - Se `flag[i]` è **False**, inserisci la parola `parole[i]` ma scritta **al contrario**.
# - Dopo aver generato la lista, estrai una **sottolista** che contiene solo gli elementi agli **indici dispari**.
# - Infine, filtra dalla sottolista solo i numeri interi (escludendo le stringhe).
#
# Usa **list comprehension** e **list slicing** per ottenere il risultato in modo compatto ed efficiente.



numeri = [3, 5, 3, 4, 5, 6]
parole = ["uno", "due", "tre", "quattro", "cinque", "sei"]
flag = [True, False, True, False, True, False]

#creiamo una nuova lista usando list comprehension
#se flag[i] è True inseriamo numeri[i] * 2, altrimenti inseriamo parole[i] al contrario
new_list = [numeri[i] * 2 if flag[i] else parole[i][::-1] for i in range(len(flag))]
print(new_list)


#estraiamo una sottolista che contiene solo gli elementi agli indici dispari
sottolista = new_list[1::2]
print(sottolista)

#filtriamo dalla sottolista solo i numeri interi
numeri_interi = [elemento for elemento in new_list if isinstance(elemento, int)]
print(numeri_interi)

