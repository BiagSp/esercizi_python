"""
Chiedi all'utente un numero N e stampa la tabellina del N fino a N x 10 utilizzando un ciclo for.

"""


# Chiedi all'utente un numero N e stampa la tabellina del N fino a N x 10 utilizzando un ciclo for.

numero = int(input("Digita un numero intero:\n"))

# Utilizziamo un ciclo for per iterare da 1 a 10
for n in range(1, 11):
    risultato = numero * n
    print(f"{numero} × {n} = {risultato}")