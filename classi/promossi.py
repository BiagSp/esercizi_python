# Esercizio: Creazione di una lista di promozioni
#
# Hai tre liste che rappresentano:
# 1. `studenti` - I nomi degli studenti di una classe.
# 2. `voti` - I voti corrispondenti a ciascun studente.
# 3. `promossi` - Una lista vuota che conterrà i nomi degli studenti promossi.
#
# Scrivi un programma che:
# 1. Utilizzi un ciclo `while` per scorrere la lista degli `studenti` e dei loro voti.
# 2. Controlli i voti degli studenti:
#    - Se un voto è maggiore o uguale a 6, aggiungi lo studente alla lista `promossi`.
#    - Altrimenti, stampa un messaggio indicando che lo studente non è stato promosso.
# 3. Al termine, stampa la lista degli studenti promossi e di quelli non promossi.
#
# Dati iniziali:
# studenti = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
# voti = [7, 5, 6, 8, 4]
# promossi = []
#DA RIFARE CON LE CLASSI

class Student:
    def __init__(self, nome: str, voti: list[float]):
        self.nome = nome
        self.voti = voti  # Lista di voti
        self.promosso = False

    def aggiungi_voto(self, voto: float) -> None:
        """Aggiunge un voto alla lista dei voti dello studente."""
        self.voti.append(voto)

    def media(self) -> float:
        """Calcola la media dei voti. Se non ci sono voti, restituisce 0."""
        return sum(self.voti) / len(self.voti) if self.voti else 0.0

    def is_promosso(self) -> bool:
        """Verifica se la media dei voti è sufficiente per la promozione (>= 6)."""
        return self.media() >= 6

    def promuovi(self) -> str:
        """Verifica la condizione di promozione e aggiorna lo stato."""
        if self.is_promosso():
            self.promosso = True
            return f"{self.nome} è stato promosso con media {self.media():.2f}"
        else:
            return f"{self.nome} non è stato promosso con media {self.media():.2f}"

    def __str__(self) -> str:
        return f"{self.nome} - Voti: {self.voti} - Media: {self.media():.2f} - Promosso: {self.promosso}"


    

studenti = [
    Student("Alice", [7, 8, 9]),
    Student("Bob", [5, 6, 4]),
    Student("Charlie", [6, 7, 5]),
    Student("Diana", [8, 9, 7]),
    Student("Eve", [4, 5, 6])
]

promossi = []
non_promossi = []

i = 0

while i < len(studenti):
    risultato = studenti[i].promuovi()
    print(risultato)
    if studenti[i].promosso:
        promossi.append(studenti[i])
    else:
        non_promossi.append(studenti[i])
    i += 1


print("\nStudenti non promossi")
for studente in non_promossi:
    print(studente)

print("\nStudenti  promossi")
for studente in promossi:
    print(studente)




def add_voto(studenti: list[Student]) -> None:
    #stampiamo la lista studenti
    print("studenti disponibili:")
    for s in studenti:
        print(f"- {s.nome}")

    nome_input = input("Digita il nome dello studente il quale vuoi aggiungere voti:\n")

    studente_trovato = None
    for s in studenti:
        if s.nome.lower() == nome_input.lower():
            studente_trovato = s
            break

    if not studente_trovato:
        print("Studente non trovato")
        return


    marks = input("Digita i voti che desideri separati da uno spazio\n").split()
    for v in marks:
            try:
                votes = float(v)
                studente_trovato.aggiungi_voto(votes)
            except ValueError:
                print(f"Valore non valido {v} Salto questo voto")
    print(f"Voti aggiornato per {studente_trovato.nome}: {studente_trovato.voti}")


add_voto(studenti)