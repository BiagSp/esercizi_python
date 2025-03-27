"""
Chiedi all'utente una frase e un numero N. Usa una list comprehension per estrarre tutte le parole della frase che hanno 
lunghezza maggiore di N.

"""


frase = input("Digita una frase:\n")
numero = input("Inserisci un numero intero:\n")

lista_words = [w for w in frase.split() if len(w) > int(numero)]

print(lista_words)