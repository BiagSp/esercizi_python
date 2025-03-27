"""
Esercizio 1: Numeri primi
Scrivi un programma che chiede all'utente un numero N e stampa tutti i numeri primi da 2 a N utilizzando un ciclo while o for.

"""

numero = int(input("Digita un numero intero:\n"))
n_primo = []


for n in range(2, numero +1):
    is_prime = True
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime: 
        n_primo.append(n)

print(n_primo)


"""#Crivello di eratostene
def crivello_eratostene(n):
    # Crea un array di booleani tutti inizializzati a True
    # A[i] sarà False se i non è primo
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 e 1 non sono primi
    
    # Inizia il setaccio
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Marca tutti i multipli di i come non primi
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    # Restituisci la lista dei numeri primi
    return [i for i in range(2, n + 1) if is_prime[i]]

# Input dall'utente
numero = int(input("Digita un numero intero:\n"))
numeri_primi = crivello_eratostene(numero)
print(numeri_primi)"""