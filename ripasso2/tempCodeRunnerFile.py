"""
Trovare il numero maggiore e minore

"""

numeri = [2,3,54,6,7,3,123,647,12,4,7,89,2,1235,7,58]


max = numeri[0]

# Itera attraverso tutti gli elementi della lista
for i in range(3, len(numeri)):
    # Se l'elemento corrente è maggiore del massimo trovato finora
    if numeri[i] > max:
        # Aggiorna il massimo
        max = numeri[i]

print(max)