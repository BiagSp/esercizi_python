"""
Troviamo i numeri primi

"""

def prime_num(n):
    if n < 2:
        return []  # Non ci sono numeri primi sotto 2
    
    # Inizializza una lista dove ogni elemento indica se l'indice è un numero primo
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False  # 0 e 1 non sono primi
    
    # Itera fino alla radice quadrata di n (ottimizzazione)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:  # Se i è primo, elimina tutti i suoi multipli
            # Imposta a False i multipli di i, partendo da i^2
            sieve[i*i : n+1 : i] = [False] * len(sieve[i*i : n+1 : i])
    
    # Ritorna gli indici degli elementi ancora True
    return [num for num, is_prime in enumerate(sieve) if is_prime]

print(prime_num(199))
    