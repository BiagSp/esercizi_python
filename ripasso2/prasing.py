"""
Obiettivo: Scrivere un programma che conti il numero di parole in una stringa.
Guida:

Inizia dividendo la stringa in parole usando il metodo split()
Conta gli elementi nella lista risultante
Gestisci i casi particolari (spazi multipli, punteggiatura)

"""

parole = "Sarò felice di fornirti  ?! ;:  best practice, senza darti direttamente la soluzione."

stringhe = parole.split()
punteggiatura = ",.!?;:\"'()[]{}!|-"

words_without_punct = []

for word in stringhe:
    words_without = ""
    for carattere in word:
        if carattere not in punteggiatura:
            words_without += carattere
    words_without_punct.append(words_without)
    
numero_parole = len(words_without_punct)

print("numero di parole", numero_parole)




