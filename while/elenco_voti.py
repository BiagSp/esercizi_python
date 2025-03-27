"""
Traccia:

Chiedi all’utente di inserire un elenco di voti (numeri interi) separati da spazio.
Converti ciascun voto a intero.
Usando un ciclo while, calcola la media (media aritmetica: somma dei voti / numero dei voti).
Stampa la media finale. Se la lista dei voti è vuota (ad esempio, se l’utente non inserisce nulla), gestisci il caso e stampa un messaggio adeguato.
Indicazioni:

Per evitare l’errore di divisione per zero, controlla se la lunghezza della lista è 0.
(somma / numero_di_voti) dà la media (in Python 3, è un numero in virgola mobile).

"""


voti = input("Inserisci i voti separati da uno spazio:\n").split()

#convertiamo i voti in interi
i = 0
somma = 0
while i < len(voti):
    voti[i] =  int(voti[i])
    if len(voti) == 0:
        print("Lista vuota!")
    else:
        somma += voti[i]
        media = somma/(len(voti))
    i += 1
    
    
print("La media dei voti è:", media, "\n")