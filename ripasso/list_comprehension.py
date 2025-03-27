"""
Dati N numeri interi inseriti dall’utente, usa una list comprehension per generare una lista con i quadrati di tutti i numeri.

"""

numeri = [int(i)**2 for i in input("Digita una serie di numeri interi separati da spazio:\n").split()]

print(numeri)