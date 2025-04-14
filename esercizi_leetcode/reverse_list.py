"""
Funzione per invertire una lista

"""



def reverse(lista):
    lista_invertita = []

    indice = len(lista) - 1

    while indice >= 0:
        elemento = lista[indice]
        lista_invertita.append(elemento)
        indice -=1
    return lista_invertita

mia_lista = [1,2,3,4,5]
print(reverse(mia_lista))