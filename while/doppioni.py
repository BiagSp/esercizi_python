#scrivere un programma che trova gli elementi doppioni

doppioni = {}

frase = input("inserisci una frase a tuo piacere:\n").split()

for el in frase:
    if el in doppioni:
        doppioni[el] += 1
    else:
        doppioni[el] = 1

print("Elementi doppioni:", [k for k, v in doppioni.items() if v > 1])