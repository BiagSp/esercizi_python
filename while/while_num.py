"""
Traccia:

Chiedi all’utente di inserire N numeri separati da spazio (es.: “10 3 -5 4 2”).
Converti ogni numero in intero (usando un while per scorrere e int() per convertire).
Tramite un altro while, calcola la somma di tutti i numeri positivi (ignora i negativi).
Stampa la somma risultante.
Indicazioni:

Dividi l’input con .split(), ottieni una lista di stringhe.
Converti in interi con un ciclo while i < len(numeri_str): ....
Fai un secondo while che scorre i numeri: se il numero è >= 0, lo aggiungi alla somma.

"""

numeri = input("inserisci N numeri separati da spazio\n").split()

#convertiamo i numeri in interi
i = 0 
num_positivi= []
somma= 0

while i < len(numeri):
    if int(numeri[i]) > 0:
        num_positivi.append(int(numeri[i]))
        somma += int(numeri[i])
    i += 1


print(f"la somma dei numeri positivi è {somma}")
