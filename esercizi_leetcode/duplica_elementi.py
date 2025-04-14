"""
Duplicare gli elementi di una lista

"""



def duplex(n):
    lista_duplicata = []
    
    for elementi in n:
        if isinstance(elementi, (int, float)):
            elementi = str(elementi)
            lista_duplicata.append(elementi * 2)
        else:
            lista_duplicata.append(elementi * 2)
            
    return lista_duplicata



lista1 = [1,2,"a"]
print(duplex(lista1))