"""
Funzione Palindromo

Descrizione: Crea una funzione che determina se una parola è un palindromo (si legge ugualmente da sinistra a destra e viceversa).

"""
def is_palindrome(testo:str):
    start = 0
    end = len(testo) - 1

    while start < end:
        if testo[start] != testo[end]:
            return False
        start += 1
        end -= 1
    return True 


print(is_palindrome("tenet"))

#versione claude

def palindroma(text):
    #puliamo il testo
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

print(palindroma("tenet"))