# Usando due input:
# - Chiedere ad un utente di inserire tre parole separate da spazio (chiamiamole p1, p2, p3)
# - e tre numeri separati da spazio (chiamiamoli n1, n2, n3)
# Costruire una lista di parole che contenga n1 volte p1, n2 volte p2 e n3 volte p3 e stamparla.

# Esempio output:
# Inserisci tre parole separate da spazio (es: cane gatto topo): cane gatto topo
# Inserisci tre numeri separati da spazio (es: 2 3 1): 2 3 1
# Lista risultante: ['cane', 'cane', 'gatto', 'gatto', 'gatto', 'topo']


parole = input("Inserisci tre parole separate da spazio (es: cane gatto topo): ").split()
numeri = input("Inserisci tre numeri separati da spazio (es: 2 3 1): ").split()

#convertiamo i numeri in interi
i = 0
while i < len(numeri):
    #per ogni iterazione di numeri[i] convertiamo il valore in intero
    numeri[i] = int(numeri[i])
    i += 1

#inizializziamo la lista vuota
lista_parole = []
print(numeri)
#aggiungiamo n1 volte parola[0], n2 volte parola[1] e n3 volte parola[2] alla lista_parole
i = 0
while i < len(numeri):
    #per ogni iterazione di numeri[i] aggiungiamo parola[i] alla lista_parole num volte
    # come funziona, praticamente l'indice numeri viene messo al i-esimo valore di numeri[i] cosi j < numeri[i] fin quando j non 
    # è iterato al valore di numeri[i] 
    j = 0
    while j < numeri[i]:
        #aggiungiamo parola[i] alla lista_parole num volte
        lista_parole.append(parole[i])
        j += 1
    i += 1

print(f"Lista risultante: {lista_parole}")
