"""
Realizza un programma in Python che permetta di gestire una classe. In particolare, il programma deve consentire di:

Aggiungere uno studente con il proprio nome e una serie iniziale di voti.
Rimuovere uno studente dalla classe.
Aggiornare i voti di uno studente aggiungendo nuovi voti.
Visualizzare un report della classe, mostrando per ogni studente la lista dei voti e la media dei voti.
Uscire dal programma.

"""


classe = {
    "Alice": [7, 5, 6, 8, 4],
    "Bob": [9, 8, 7, 6, 5],
    "Charlie": [6, 7, 8, 9, 10]
}

while True:
    #chiediamo all'utente di scegliere l'opzione 
    opzione = input("Digita una delle seguenti opzioni: Aggiungi studente(as), Rimuovi studente(rm), aggiungi voto studente(av), visualizza report(vr), esci\n")
    #se l'opzione è aggiungi studente allora procediamo a creare lo studente
    if opzione.lower() == "as":
        nome = input("inserisci il nome dello studente:\n")
        #chiediamo all'utente il nome del nuovo studente
        if nome in classe:
            #controlliamo che questo studente non sia già presente nella classe
            print(f"los tudente {nome} è già presente nella classe")
        else:
            voti = []
            #inizializiamo la variabile voti che verrà poi popolata
            try:
            #usiamo il try except per controllare eventuali errori
                num_voti = int(input("Quanti voti vuoi inserire inizialmente?"))
            #chiediamo all'utente quanti voti desidera registrare
            except ValueError:
            #con except controlliamo l'eventuale errore di non aver inserito un numero
                print("Devi inserire un numero valido.")
                continue
            for i in range(num_voti):
            #controlliamo la variabile num_voti e la cicliamo per quanto sia il valore del num_voti es: num_voti = 5 cilco *5
                try:
            #tramite try except controlliamo di nuovo eventuali errori e li gestiamo 
                    voto = float(input(f"inserisci il voto #{i+1}:"))
            #chiediamo all'utente ogni singolo voto
                    voti.append(voto)
            #aggiungiamo alla lista voti[] i voti inseriti dall'utente 
                except ValueError:
            #gestiamo eventuali errori
                    print("Devi inserire un numero valido.")
                    break
            else:
            #associamo alla classe il nome dello studente creato e i relativi voti
                classe[nome] = voti
            #classe[nome(studente creato)] = (associato) voti
                print(f"Studente {nome} aggiunto con voti iniziali: {voti}")
    elif opzione.lower() == "rm":
    #chiediamo all'utente di scegliere il nome dello studente da cancellare
        nome = input("Inserisci il nome dello studente che vuoi cancellare\n")
    #se l'opzione è cancella studente allora procediamo a cancellare lo studente dalla classe
        if nome in classe:
            del classe[nome]
            print(f"Studente {nome} cancellato con successo.")
        else:
            print("studente non trovato")
    elif opzione.lower() == "av":
    #chiediamo all'utente di scegliere il nome dello studente da aggiungere un voto
        nome = input("Inserisci il nome dello studente che vuoi aggiungere un voto\n")
        if nome in classe:
        #se lo studente è presente nella classe allora procediamo a aggiungere il voto
            try:
                voto = float(input(f"Inserisci il voto per {nome}:"))
            #chiediamo all'utente il voto per lo studente
                classe[nome].append(voto)
            #aggiungiamo il voto allo studente se non è già presente
                print(f"Voto aggiunto con successo per {nome}")
            except ValueError:
                print("Devi inserire un numero valido.")
        else:
            print("Studente non trovato")
    elif opzione.lower() == "vr":
        #stampiamo il report della classe per ogni studente
        for nome, voti in classe.items():
            #cicliamo il dizionario
            if voti:
                #stampiamo i voti per lo studente se sono presenti
                media = sum(voti) / len(voti)
                print(f"{nome} Voti: {voti} | Media: {media:.2f}")
                #stampiamo la media dei voti per lo studente se sono presenti 2.f (float con 2 cifre dopo la virgola)
            else:
                print(f"{nome}: Nessun voto inserito")
    elif opzione.lower == "esci":
        print("Arrivederci!")
        break
    else:
        print("Opzione non valida. Riprova")