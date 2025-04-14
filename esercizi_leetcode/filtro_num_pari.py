"""
Filtrare i numeri pari

"""



def filtrare_pari(n):
    lista_pari = []
    lista_dispari = []
    
    for numero in n:
        if numero % 2 == 0:
            lista_pari.append(numero)
        else:
            lista_dispari.append(numero)
    return lista_pari, lista_dispari


lista1 = [1,2,3,4,5,6,7,8,9]

print(filtrare_pari(lista1))