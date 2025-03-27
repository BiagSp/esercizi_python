# Esercizio Python: Caccia al Tesoro
#
# Consegna:
# Crea un semplice gioco di caccia al tesoro che utilizzi:
# 1. Un ciclo while per mantenere il gioco in esecuzione
# 2. Un ciclo for per iterare tra le posizioni
# 3. Slicing di stringhe per mostrare l'inizio del nome delle posizioni nel menù di selezione
# 4. Condizioni if per controllare le mosse e verificare le condizioni di vittoria
#
# Il giocatore deve visitare le posizioni per trovare la chiave e la corda,
# poi trovare il tesoro. Le posizioni degli oggetti sono generate casualmente
# all'inizio del gioco.import random

import random

# Creiamo nomi per le 10 posizioni
posizioni = ["spiaggia", "foresta", "grotta", "montagna", "villaggio", "castello", "fiume", "deserto", "palude", "collina"]

posizione_chiave = posizioni[0]
posizione_corda = posizioni[3]
posizione_tesoro = posizioni[6]


energia = 8
inventario = []
gioco_finito = False 

posizione_attuale = random.randint(0, len(posizioni) -1)
print(f"Ti trovi in: {posizioni[posizione_attuale]} e la tua energia è di:{energia}")

while energia > 0 and not gioco_finito:

    if posizioni[posizione_attuale] == posizione_chiave and "chiave" not in inventario:
        print("Hai trovato la chiave")
        inventario.append("chiave")
    elif posizioni[posizione_attuale] == posizione_corda and "corda" not in inventario:
        print("Hai trovato la corda")
        inventario.append("corda")
    elif posizioni[posizione_attuale] == posizione_tesoro:
        if "chiave" in inventario and "corda" in inventario:
            print("Congratulazioni hai finito il gioco")
            gioco_finito = True
            continue
        else:
            print("ti serve la corda e la chiave per aprire il tesoro")

    print("Dove deesideri spostarti ora?")

    for i in range(len(posizioni)):
        if i == posizione_attuale:
            print(f"{i+1} {posizioni[i]} sei qui")
        else:
            indizio = posizioni[i][:3] + "..."
            print(f"{i+1} {indizio}")
    print("0. Esci dal gioco")


    scelta = input("Inserisci il numero della posizione che desideri raggiungere")

    if scelta == "0":
        print("Coglion@ hai abbandonato la ricerca e sei uscito dal gioco")
        break
    elif scelta.isdigit() and 1 <= int(scelta) <= len(posizioni):
        nuova_posizione = int(scelta) -1 

        if nuova_posizione != posizione_attuale:
            posizione_attuale = nuova_posizione
            energia -= 1
            print(f"Ti sei spostato in: {posizioni[posizione_attuale]}")
        else:
            print("sei già qui")
    else:
        print("Scelta non valida! Inserisci un numero tra 0 e", len(posizioni))


if energia <= 0:
    print("Hai esaurito tutta l'energia! MasterChef per te finisce qui")
    if len(inventario) > 0:
        print(f"Sei riuscito a trovare {"," .join(inventario)}")
    else:
        print("Non hai trovato manco un cazzo, brav@")
elif gioco_finito:
    print(f"hai completato il gioco con energia rimasta: {energia}")



