# Dato un dizionario con alcuni nomi di persone come chiavi e le loro età come valori.
# Stampare i nomi delle persone con età maggiore di 18.
eta_persone = {
    "Alice": 25,
    "Bob": 17,
    "Carla": 30,
    "Davide": 15,
    "Elena": 22,
    "Franco": 19
}

# cicliamo il dizionario
for i in eta_persone:
    # se l'età della persona è maggiore di 18 stampiamo
    if eta_persone[i] > 18:
        print(i)
