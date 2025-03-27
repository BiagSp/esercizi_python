"""
Scrivi una funzione che, data una stringa, restituisca il numero di caratteri unici presenti.

"""
def unique():
    stringa = input("Inserisci una parola o una frase:\n")

    uniche = set() 

    for l in stringa: 
        uniche.add(l)
    print(len(uniche))


unique()