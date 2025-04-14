"""
Contare quante vocali sono presenti in una frase

"""


def contatore(stringa:str):
    vocali = "aeiou"
    count = {}
    
    for carattere in stringa:
        carattere_lower = carattere.lower()
        if carattere_lower in vocali:
            if carattere_lower in count:
                count[carattere_lower] += 1
            else:
                count[carattere_lower] = 1
    return count



print(contatore("vocabolario"))