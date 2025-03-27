#Da una lista data cercare quale sia il numero più grande

lista_num = [20, 4, 5, 86, 98, 56]

#creiamo un contatore per tenere conto dei numeri controllati

index = 0
#creiamo una lista massimo che tiene come elemento l'index della lista_num
massimo = lista_num[index]

#iteriamo la lista

while index < len(lista_num):
    #se il numero corrente è maggiore del numero massimo trovato finora, lo aggiorniamo
    if lista_num[index] > massimo:
        massimo = lista_num[index]
        #aggiorniamo l'indice
    index += 1

print(f"Il numero più grande è: {massimo}")