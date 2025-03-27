import time

def trova_primi_per_differenza(n):
    # Crea un insieme con tutti i numeri da 2 a n
    tutti_numeri = set(range(2, n + 1))
    
    # Crea un insieme vuoto per i numeri composti (non primi)
    composti = set()
    
    # Per ogni numero da 2 a sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        # Se i non è già stato identificato come composto
        if i not in composti:
            # Aggiunge tutti i multipli di i (eccetto i stesso) all'insieme dei composti
            multipli = set(range(i*2, n + 1, i))
            composti.update(multipli)
    
    # I numeri primi sono quelli che non sono composti
    primi = tutti_numeri - composti
    return sorted(primi)  # Ordina e restituisce i numeri primi

def mia_funzione():
    # Richiede all'utente di inserire un numero
    numero = int(input("Digita un numero intero:\n"))
    
    # Avvia il timer
    start_time = time.time()
    
    # Calcola i numeri primi fino a 'numero'
    numeri_primi = trova_primi_per_differenza(numero)
    
    # Ferma il timer
    end_time = time.time()
    
    # Stampa i numeri primi e il tempo di esecuzione
    print("Numeri primi:", numeri_primi)
    print("Tempo di esecuzione:", end_time - start_time, "secondi")

# Chiamata alla funzione che misura il tempo di esecuzione
mia_funzione()
