"""
Trovare il massivo valore

"""


def trova_massimo(lista_numeri):
    if not lista_numeri:
        return None
    
    massimo_attuale = lista_numeri[0]
    
    for numero in lista_numeri:
        if numero > massimo_attuale:
            massimo_attuale = numero
            
    return massimo_attuale

print(trova_massimo([1,2,45,12,6568,12,5678]))