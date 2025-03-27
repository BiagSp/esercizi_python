"""
Traccia:

Chiedi all’utente un numero intero N.
Con un ciclo while, stampa una “scaletta” di asterischi, dove la prima riga ha 1 asterisco, la seconda ne ha 2, ecc., fino alla riga numero N.

"""


numero = int(input("inserisci un numero intero\n"))

i = 1

while i <= numero:
    # stampa spazi per la scelta di posizione
    print(" " * (numero -i), "*" * (2 * i-1))
    # incrementa il numero di asterischi per la successiva riga
    i += 1