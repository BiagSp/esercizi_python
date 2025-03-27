"""
Trovare il numero maggiore e minore

"""

numeri = [2,3,54,6,7,3,123,647,12,4,7,89,2,1235,7,58]


max = numeri[0]

# Itera attraverso tutti gli elementi della lista
for i in range(1, len(numeri)):
    print(i)
    # Se l'elemento corrente è maggiore del massimo trovato finora
    if numeri[i] > max:
        # Aggiorna il massimo
        max = numeri[i]

print(max)

#metodo ottimizzato

if not numeri: 
    print("lista vuota")
    exit()

massimo = numeri[0]
lungheza = len(numeri)
i = 1

valore_estremo = float("inf")

while i < lungheza:
    if numeri[i] == valore_estremo:
        massimo = numeri[i]
        break
    if numeri[i] > massimo:
        massimo = numeri[i]
    i += 1

print(massimo,"Massimo")