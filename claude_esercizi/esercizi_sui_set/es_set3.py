# Esercizio 2: Operazioni Fondamentali sui Set
# Data la seguente lista di parole:

lista1 = ["mela", "pera", "banana", "arancia", "kiwi"]
lista2 = ["pera", "kiwi", "ananas", "mango", "papaya"]

# Scrivi funzioni che restituiscano:
# 1. Parole presenti in entrambe le liste
# 2. Parole presenti solo nella prima lista
# 3. Parole presenti solo nella seconda lista
# 4. Tutte le parole uniche dalle due liste

def operationSet(lista1, lista2):

    set1 = set(lista1)
    set2 = set(lista2)


    #parole presenti solo nel primo set
    #sottraiamo il primo set al secondo per ottenere solo gli elementi presenti nel primo
    primo_set = set1  - set2
    print(primo_set, "set con solo gli elementi del primo set")

    #stessa cosa la facciamo per il secondo set
    secondo_set = set2 - set1
    print(secondo_set, "set con solo gli elementi del secondo set")

    #elementi presenti in enntrambi gli elementi "INTERSEZIONE"
    intersezione = set1 & set2
    print(intersezione, "intersezione di entrambi i set")

    #elementi unici di etrambi i set
    all_elements = set1 | set2
    print(all_elements, "unione degli elementi di entrambi i set")


operationSet(lista1, lista2)