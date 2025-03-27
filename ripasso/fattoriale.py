"""
Chiedi all'utente un numero intero N e calcola il suo fattoriale (N! = N * (N-1) * ... * 1) utilizzando un ciclo while.

"""
#dobbiamo creare una lista che arrivi al numero digitato e successivamente moltiplicarli in un ciclo


numero = int(input("inserisci un numero intero:\n"))

count = 1
fattoriale = 1

while count <= numero:
    fattoriale *= count
    count += 1

print(fattoriale)
