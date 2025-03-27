"""
Creare uno script di python che simuli il login ad un sito di casino.

si chieda all'utente: nome, cognome, ed età
si verifichi che il nome e il cognome siano più lunghi di un carattere e che l'età sia maggiore o uguale di 18 anni
se tutto è corretto stampare una string di conferma altrimenti comunicare l'errore all'utente
si consideri che l'utente fornirà sempre dati di tipo corretto
BONUS: stampare resoconto dei dati assicurandosi che nome e cognome inizino con la maiuscola

"""

"""while True:
    nome = input("Inserisci il tuo nome:\n").strip()
    cognome = input("Inserisci il tuo cognome:\n").strip()
    eta  = int(input("Inserisci la tua eta:\n"))
    
    error = []
    
    if len(nome) <= 1 and len(cognome) <= 1 and eta < 18:
        print(f"Non puoi accedere perchè il {nome} o il tuo {cognome} sono troppo corti e la tua eta è di {eta}")
    else:
        print(f"Benvenuto {nome.capitalize()} {cognome.capitalize()} {eta}")
        break

"""

"""
Dichiarare due liste di numeri con cinque elementi ciascuna e creare una lista concatenata che le includa entrambe.

BONUS: prendere gli elementi delle due liste dall'utente chiedendoli uno per uno

"""

prima_lista = []

for n in range(5):
    n = input("inserisci un numero:\n")
    prima_lista.append(n)

seconda_lista = []

for x in range(5):
    x = input("inserisci altri numeri:\n")
    seconda_lista.append(x)
    
    
lista_finale = prima_lista + seconda_lista
print(lista_finale)