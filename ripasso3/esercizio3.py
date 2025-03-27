"""
Immaginiamo di dover creare un registro di utenti per un Casinò. Creare uno script che chieda da terminale i dati di N utenti (N è una variabile) e salvare ogni utente in un dizionario. I dizionari relativi ad ogni utente devono essere contenuti in una lista. Il programma deve rifiutare una inserizione (e terminare) se il nickname di uno degli utenti è già presente nel sistema. Non terminare il programma usando la funzione exit() ma assicurarsi che sia il flow del programma a gestire questo caso.

I dati dell'utente sono:

Nickname
Eta
Gender (per semplicità solo M o F)
Si dia per scontato che l'utente inserisca sempre dati coerenti (non sono da implementare i controlli di validità dei dati inseriti).

Si cerchi di rendere l'interfaccia testuale il più comprensibile possibile, ad esempio, anziché chiedere semplicemente Inserire nickname si chieda Inserire nickname per account i-esimo dove i sarà naturalmente compreso fra 1 ed N. Aggiungere anche stampe quali Utente i-esimo inserito! e poi procedere con il prossimo.

Terminato l'inserimento degli N utenti si stampi un resoconto. Alcuni esempi possono essere: la quantità di utenti maschi e femmine, il massimo, minimo e media di età, e la lunghezza media dei nickname. In python esistono funzioni built-in per fare queste cose: evitare di usarle e re-implementare il codice per trovare massimo, minimo e media.

Si suggerisce di utilizzare le strutture di supporto adatte alla risoluzione del problema, come ad esempio liste temporanee.

"""


# Numero di utenti da inserire
N = 2
users = []

for i in range(1, N+1):
    print(f"\nInserimento dati per utente {i}/{N}")
    
    # Richiesta nickname
    nickname = input(f"Inserisci nickname per account {i}: ")
    
    # Controllo se il nickname esiste già
    nickname_esistente = False
    for user_exist in users:
        if user_exist["nickname"] == nickname:
            print(f"Errore: il nickname '{nickname}' è già presente nel sistema!")
            nickname_esistente = True
            break
    
    # Se il nickname esiste, interrompo l'intero programma
    if nickname_esistente:
        print("Inserimento utenti terminato.")
        break
    
    # Raccolta altri dati
    eta = int(input(f"Inserisci età per account {i}: "))
    gender = input(f"Inserisci gender per account {i} (M/F): ").upper()
    
    # Creazione dizionario utente
    user = {
        "nickname": nickname,
        "eta": eta,
        "gender": gender
    }
    
    # Aggiungo l'utente alla lista
    users.append(user)
    print(f"Utente {i}-esimo inserito!")

# Statistiche finali solo se ci sono utenti
if users:
    counter_male = 0
    counter_female = 0
    somma_eta = 0
    somma_lunghezza_nickname = 0
    
    # Inizializzo max_eta e min_eta con il primo valore
    max_eta = users[0]["eta"]
    min_eta = users[0]["eta"]
    
    for u in users:
        # Conteggio genere
        if u["gender"] == "F":
            counter_female += 1
        elif u["gender"] == "M":
            counter_male += 1
        
        # Aggiorna max e min età
        if u["eta"] > max_eta:
            max_eta = u["eta"]
        if u["eta"] < min_eta:
            min_eta = u["eta"]
        
        # Somma età per la media
        somma_eta += u["eta"]
        
        # Somma lunghezza nickname
        somma_lunghezza_nickname += len(u["nickname"])
    
    # Calcolo medie
    media_eta = somma_eta / len(users)
    media_lunghezza_nickname = somma_lunghezza_nickname / len(users)
    
    # Stampa resoconto
    print("\n----- RESOCONTO -----")
    print(f"Totale utenti: {len(users)}")
    print(f"Utenti maschi: {counter_male}")
    print(f"Utenti femmine: {counter_female}")
    print(f"Età massima: {max_eta}")
    print(f"Età minima: {min_eta}")
    print(f"Età media: {media_eta:.2f}")
    print(f"Lunghezza media dei nickname: {media_lunghezza_nickname:.2f}")