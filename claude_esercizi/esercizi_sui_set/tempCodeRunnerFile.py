"""
Problema
Scrivi una funzione che, dato un elenco di dizionari
 rappresentanti persone (con nome, età e città), restituisca l'insieme (set) 
 delle città uniche in cui vivono le persone con più di 30 anni.

"""

persone = [
    {"nome": "Mario", "età": 35, "città": "Roma"},
    {"nome": "Giulia", "età": 28, "città": "Milano"},
    {"nome": "Paolo", "età": 42, "città": "Roma"},
    {"nome": "Anna", "età": 31, "città": "Napoli"}
]

# Output atteso: {"Roma", "Napoli"}
# (perché Mario, Paolo e Anna hanno più di 30 anni, e vivono a Roma e Napoli)


def filterSet(dictionary_input):
    citta = set() 

    for persona in dictionary_input:
        if persona["età"] > 30:
            citta.add(persona["città"])
    return citta
    

print(filterSet(persone))
