"""
Dati due elenchi:

Una lista di numeri
Una lista di parole
Crea una nuova lista che contenga:

Il quadrato dei numeri se sono pari
Le parole in maiuscolo se la loro lunghezza è maggiore di 4

"""

numeri = [1, 2, 5, 7, 8, 12, 24]
parole = ["uno", "parola", "test"]

lista = [
    x**2 if isinstance(x, int) else x.upper()  for x in numeri + parole
    if (isinstance(x, int) and x % 2 == 0) or (isinstance(x, str) and len(x) > 4)
]

print(lista)
