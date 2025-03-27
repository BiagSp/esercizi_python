"""
Problema: Data una lista di numeri con duplicati,
crea una funzione che restituisca una lista con solo i valori unici,
mantenendo l'ordine di prima apparizione.

"""

lista = [1,2,3,1,45,5,2,1,2,3,45,2,6,57,8]

def remove_duplicate(input_list): 
    seen = set()
    result = []

    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

print(remove_duplicate(lista))


