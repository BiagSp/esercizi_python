"""
Sviluppare una funzione chiamata genera_password che:

Accetti un parametro per la lunghezza desiderata della password
Produca una stringa casuale contenente un mix bilanciato di caratteri
Garantisca la presenza di almeno un carattere di ciascuna categoria richiesta
-----------------------
Requisiti tecnici

La funzione deve generare password con caratteri di tutte le seguenti categorie:

Lettere maiuscole (A-Z)
Lettere minuscole (a-z)
Numeri (0-9)
Caratteri speciali (ad esempio: !@#$%^&*)
L'utente deve poter specificare la lunghezza della password
La distribuzione dei caratteri deve essere sufficientemente casuale
"""

import random
import string

def generatore_pw(lun:int):
    alfabeto = ["a","b","c","d","e","f","g","h","i","y","l","m","n","o","p","q","r","s","t","u","v","w","z"]
    numeri = ["1","2","3","4","5","6","7","8","9","0"]
    special_char = ["@","#","?","'","^","]","[","$","&","€","!"]

    password = []
    
    # Aggiungiamo caratteri casuali alla password
    for _ in range(lun):
        # Scegliamo un tipo di carattere casuale (lettera, numero o speciale)
        total_char = [random.choice(alfabeto),random.choice(alfabeto).upper(), random.choice(numeri), random.choice(special_char)]
        # Aggiungiamo un carattere casuale alla password
        password.append(random.choice(total_char))
    
    # Uniamo i caratteri in una stringa
    return ''.join(password)

# Test della funzione
print(generatore_pw(16))

