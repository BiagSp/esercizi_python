import random
import collections
import string

def analizza_generatore(funzione_generatrice, lunghezza, test_num=100):
    """Analizza statisticamente le password generate."""
    passwords = [funzione_generatrice(lunghezza) for _ in range(test_num)]
    
    # Analisi per caratteri
    tutti_caratteri = ''.join(passwords)
    frequenze = collections.Counter(tutti_caratteri)
    
    print(f"Analisi su {test_num} password di lunghezza {lunghezza}:")
    print(f"Caratteri più comuni: {frequenze.most_common(5)}")
    
    # Analisi per tipi di caratteri
    maiuscole = sum(1 for c in tutti_caratteri if c.isupper())
    minuscole = sum(1 for c in tutti_caratteri if c.islower())
    numeri = sum(1 for c in tutti_caratteri if c.isdigit())
    speciali = len(tutti_caratteri) - maiuscole - minuscole - numeri
    
    print(f"Distribuzione per tipo:")
    print(f"- Maiuscole: {maiuscole / len(tutti_caratteri):.2%}")
    print(f"- Minuscole: {minuscole / len(tutti_caratteri):.2%}")
    print(f"- Numeri: {numeri / len(tutti_caratteri):.2%}")
    print(f"- Speciali: {speciali / len(tutti_caratteri):.2%}")
    
    return passwords

def generatore_pw_migliorato(lunghezza):
    """Generatore di password con distribuzione bilanciata e alta entropia."""
    # Set di caratteri completi
    minuscole = string.ascii_lowercase
    maiuscole = string.ascii_uppercase
    numeri = string.digits
    speciali = "!@#$%^&*()-_=+[]{}|;:,.<>?/~"
    
    # Garantiamo almeno un carattere di ogni tipo
    password = [
        random.choice(minuscole),
        random.choice(maiuscole),
        random.choice(numeri),
        random.choice(speciali)
    ]
    
    # Riempiamo il resto della password con caratteri casuali da tutti i set
    tutti_caratteri = minuscole + maiuscole + numeri + speciali
    password.extend(random.choice(tutti_caratteri) for _ in range(lunghezza - 4))
    
    # Mescoliamo più volte per garantire casualità nell'ordine
    for _ in range(3):
        random.shuffle(password)
    
    return ''.join(password)

# Test e analisi
passwords = analizza_generatore(generatore_pw_migliorato, 16)
print("\nEsempi di password generate:")
for i in range(5):
    print(passwords[i])