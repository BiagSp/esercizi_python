'''Chiedere all'utente di inserire una serie di numeri il programma troverà il numero mancante nella serie'''

numeri = input("inserisci una lista di numeri:\n").split()

lista_num = list(map(int, numeri))

indice = 0
massimo = lista_num[indice]

while indice < len(lista_num):
  if lista_num[indice] > massimo:
    massimo = lista_num[indice]
  indice += 1

print("Massimo:", massimo)

indice = 0
minimo = lista_num[indice]

while indice < len(lista_num):
  if lista_num[indice] < minimo:
    minimo = lista_num[indice]
  indice += 1

print("il minimo è", minimo)

somma_attesa = sum(range(minimo, massimo + 1))
print(somma_attesa)

numero_mancante = somma_attesa - sum(lista_num)
print("il numero mancante è", numero_mancante)

# Set di tutti i numeri attesi
range_completo = set(range(minimo, massimo + 1))
numeri_presenti = set(lista_num)  # Set di numeri forniti

numeri_mancanti = range_completo - numeri_presenti  # Differenza tra i due set

print("Numeri mancanti:", sorted(numeri_mancanti))  # Ordina e stampa