"""
Chiedi all’utente un numero N e crea una lista contenente i quadrati dei numeri da 1 a N utilizzando la list comprehension.

"""


numero = int(input("Digita un numero:\n"))

quadrati = [n*n for n in range(1, numero + 1)]
print(quadrati)