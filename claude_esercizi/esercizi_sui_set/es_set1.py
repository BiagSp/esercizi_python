"""
Scrivi un programma che mostra varie operazioni su set: unione, intersezione, differenza e differenza simmetrica.

"""

#set su python sono collezioni non ordinte di elementi unici. Questa definiziione contiene due aspetti fondamentali
# Non Ordinati
# Elemeti Unici
#queste caratteristiche rendonno i set perfetti per eliminnare duplicati ed eseguire operazioniu matematiche di teoria degli Insiemi


#creazione base di un set
frutti_rossi = {"mela", "ciliegia", "fragola", "melograno"}
#usando le parentesi {} si crea un set 

numeri_pari = set([2,4,6,8,10])
#oppure si può usare la funzione set

#si possono fare i set delle stringhe
lettere = set("pytnnhon")
#così ogni carattere diventa un elemento

#set vuoto 
set_vuoto = set()

print(lettere,numeri_pari)

# === OPERAZIONI CON I SET ===

#definiamo due set
A = {1,2,3,4,5,6}
B = {7,8,9,0,10,5,12,1,2,3,4}


#UNIONE
#Usando l'operatore | si ha l'Unione dei set
#può essere anche multipla
c = {12,123,45,67,876,5,6,4,1,2,3,7,8,9,0}
unione = A | B | c
print(unione, "multipla")

#oppure si può usare il metodo .union("set da unire")
union = A.union(B)
print(union)

#INTERSEZIONE

#Usando l'operatore & si ha l'intersezione tra isiemi
intersezione = A & B & c
print(intersezione, " intersezione")
#anche l'intersezione ha il metodo opportuno dedicato
intersection = A.intersection(c,B)
print(intersection, "intersezione metodo")


# DIFFERENZA
#operazione di differenza tra set, usando l'operatore -

differenza = A - B
print(differenza, "differenza")
#anche qui si può usare il metodo .difference("nnome del set")

#DIFFERENZA SIMMETRICA
#la differenza simmetrica contiene elementi presenti in uno dei due set, ma non in enntrambi
#si usa l'operatore ^
simmetric = A ^ B ^ c
print(simmetric, "differenza simmetrica")




"""
Best practice nell'uso dei set in Python

Utilizzo appropriato: Usa i set quando l'ordine non è importante e hai bisogno di elementi unici.
Performance: I set sono ottimizzati per verificare l'appartenenza di un elemento (in operator), con complessità temporale O(1).
Immutabilità degli elementi: Gli elementi di un set devono essere immutabili (es: numeri, stringhe, tuple). Non puoi inserire liste o dizionari.
Creazione efficiente: Se devi creare un set a partire da una sequenza con molti duplicati, usa set(sequenza) per maggiore efficienza.
Scegli la sintassi più leggibile: Per le operazioni sui set, usa gli operatori (|, &, -, ^) quando rende il codice più chiaro.
Operazioni in-place: Usa i metodi che modificano il set originale (.update(), .intersection_update(), ecc.) per risparmiare memoria.
Comprensione dei set: Puoi usare le set comprehension per creare set in modo conciso:

"""

#COMPREHENSION SET

quadrati_pari = {x**2 for x in range(10) if x % 2 == 0}
print(quadrati_pari)