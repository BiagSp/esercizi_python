"""
Traccia:

Chiedi all’utente una frase (input di tipo stringa).
Dividi la frase in parole (puoi usare .split() per dividere sugli spazi).
Chiedi poi all’utente un numero intero N.
Tramite un ciclo while, conta quante parole hanno lunghezza maggiore di N.
Stampa quante sono e, se vuoi, anche quali sono.
Indicazioni:

Ricorda che len(parola) ti dice la lunghezza della singola parola.
Tieni una variabile contatore inizializzata a 0.
Scorri l’indice da 0 a len(lista_parole) e, se len(lista_parole[i]) > N, incrementa il contatore.

"""

frase = input("inserisci una frase:\n").split()
numero = int(input("inserisci un numero intero:\n"))

i = 0
counter = 0
parole = []

while i < len(frase):
    #cicliamo le parole della frase inserita dall'utente
    if len(frase[i]) > numero:
        #se la parola ha una len maggiore del numero inserito dall'utente allore aggiorniamo il contatore
        counter += 1
        #aggiungiamo la parole alla lista parole
        parole.append(frase[i])
    i += 1

print(f"Le parole con lunghezza maggiore di {numero} sono {counter} e sono: {parole}")