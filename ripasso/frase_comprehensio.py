"""
Chiedi all’utente una frase e usa una list comprehension per estrarre tutte le parole che iniziano con una vocale (a, e, i, o, u).

"""

frase = input("Digita una frase:\n")

vocale = [parola for parola in frase.split() if parola[0].lower() in "aeiou"]
print(vocale)
