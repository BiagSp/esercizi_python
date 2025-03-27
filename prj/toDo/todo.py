import json
import os

def main():
    # Funzione principale che gestisce l'interfaccia utente.

    filename = "tasks.json"

    # Carichiamo le attività dal file se esiste
    tasks = load_tasks(filename)

    print("Benvenuto nel gestore delle attività")

    while True:
        print("\n=== MENU PRINCIPALE ===") 
        print("1. Aggiungi attività")
        print("2. Visualizza attività")
        print("3. Completa attività")
        print("4. Elimina attività")
        print("5. Esci")

        choice = input("\nSeleziona un'opzione (1-5): ")

        if choice == "1":
            print("Hai selezionato: Aggiungi attività")

            # Chiediamo i dettagli della nuova attività
            description = input("Inserisci la descrizione dell'attività: ")

            # Troviamo il prossimo id
            next_id = 1
            if tasks:
                next_id = max(task["id"] for task in tasks) + 1

            # Generiamo il dizionario dell'attività
            task = {
                "id": next_id,
                "description": description,
                "completed": False
            }
            tasks.append(task)
            print(f"Attività: '{description}' aggiunta con successo!")
            # Salviamo le attività
            save_tasks(tasks, filename)

        elif choice == "2":
            print("Hai selezionato: Visualizza attività")

            # Controlliamo se ci sono attività da mostrare
            if not tasks:
                print("Non ci sono attività da mostrare")
            else:
                print("\n=== ELENCO ATTIVITÀ ===")
                print(f"{'ID':<5}{'STATO':<12}{'DESCRIZIONE':<30}")
                print("-" * 47)

                for task in tasks:
                    # Determiniamo lo stato dell'attività
                    status = "✓ Completata" if task["completed"] else "○ Da fare"

                    # Stampiamo le informazioni sull'attività
                    print(f"{task['id']:<5}{status:<12}{task['description']:<30}")
                    
        elif choice == "3":
            if not tasks:
                print("Non ci sono task nella lista!")
            else:
                print("\n=== ELENCO DELLE ATTIVITÀ ===")
                print(f"{'ID':<5}{'STATO':<12}{'DESCRIZIONE':<30}")
                print("-" * 47)

                for task in tasks:
                    status = "✓ Completata" if task["completed"] else "○ Da fare"
                    print(f"{task['id']:<5}{status:<12}{task['description']:<30}")

                try:
                    task_id = int(input("\nInserisci l'ID dell'attività da completare: "))

                    # Cerca l'attività con l'ID specificato
                    found = False
                    for task in tasks:
                        if task["id"] == task_id:
                            if task["completed"]:
                                print(f"L'attività #{task_id} è già stata completata!")
                            else:
                                task["completed"] = True
                                print(f"Attività #{task_id} segnata come completata!")
                                # Salviamo lo stato aggiornato
                                save_tasks(tasks, filename)
                            found = True
                            break
                    
                    if not found:
                        print(f"Nessuna attività trovata con ID #{task_id}!")
                
                except ValueError:
                    print("Per favore, inserisci un numero valido!")

        elif choice == "4":
            # Controlliamo se ci sono attività da eliminare
            if not tasks:
                print("Non ci sono attività da eliminare")
            else:
                print("\n=== ELENCO DELLE ATTIVITÀ ===")
                print(f"{'ID':<5}{'STATO':<12}{'DESCRIZIONE':<30}")
                print("-" * 47)

                for task in tasks: 
                    status = "✓ Completata" if task["completed"] else "○ Da fare"
                    print(f"{task['id']:<5}{status:<12}{task['description']:<30}")

                try:
                    task_id = int(input("\nInserisci l'ID dell'attività da eliminare: "))

                    found = False

                    for i, task in enumerate(tasks):
                        if task["id"] == task_id:
                            deleted_task = tasks.pop(i)
                            print(f"Attività '{deleted_task['description']}' eliminata con successo!")
                            # Salviamo lo stato aggiornato
                            save_tasks(tasks, filename)
                            found = True
                            break
                    if not found:
                        print(f"Nessuna attività trovata con ID: {task_id}")

                except ValueError:
                    print("Per favore, inserisci un numero valido!")

        elif choice == "5":
            print("Grazie per aver usato il gestore delle attività. Arrivederci!")
            break

        else:
            print("Opzione non valida")


def save_tasks(tasks, filename):
    # Salviamo le attività in un file json
    try: 
        with open(filename, "w") as file:
            json.dump(tasks, file)
        print("Attività salvate con successo")
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")


def load_tasks(filename):
    # Inizializziamo una lista vuota
    tasks = []
    
    # Carichiamo le attività dal file se esiste
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                tasks = json.load(file)
            print(f"Caricate {len(tasks)} attività dal file {filename}")
        except Exception as e:
            print(f"Errore durante il caricamento: {e}")
    else:
        print(f"Il file {filename} non esiste. Verrà creato quando aggiungerai attività")
    
    return tasks


if __name__ == "__main__":
    main()