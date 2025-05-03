"""
Esercizio 1: Manipolazione di stringhe (Base)
Problema: Scrivi un programma che prenda una stringa inserita dall'utente e conti quante vocali e consonanti contiene.
Il programma deve ignorare spazi e caratteri speciali.
Discussione dell'approccio:
Per risolvere questo problema, dovremmo:

Acquisire l'input dell'utente
Definire quali caratteri sono vocali
Iterare attraverso ogni carattere della stringa
Contare separatamente vocali e consonanti
Ignorare caratteri che non sono lettere

Quali strutture dati pensi sarebbero utili qui? Come potremmo verificare se un carattere è una lettera?

"""

stringa_utente = input("inserisci una stringa a piacere: \n")

def conta_caratteri(stringa):
    vocali = "aeiou"
    conteggio_vocali = 0
    conteggio_consonanti = 0
    
    for carattere in stringa:
        if carattere.isalpha():
            if carattere.lower() in vocali:
                conteggio_vocali += 1
            else: 
                conteggio_consonanti += 1
    
    return conteggio_consonanti, conteggio_vocali


num_vocali, num_consonanti = conta_caratteri(stringa_utente)

print(f"Nella stringa ci sono {num_consonanti} consonanti e {num_vocali} di vocali")





def dizionario_conta_lettere(stringa):
    vocali = "aeiouAEIOU"  # Includo maiuscole per comodità
    
    # Inizializzazione dei dizionari
    lettere_vocali = {}
    lettere_consonanti = {}
    
    for carattere in stringa:
        if carattere.isalpha():  # Verifica se è una lettera
            carattere_lower = carattere.lower()  # Converto in minuscolo
            
            if carattere_lower in vocali:
                # È una vocale
                if carattere_lower in lettere_vocali:
                    lettere_vocali[carattere_lower] += 1
                else:
                    lettere_vocali[carattere_lower] = 1
            else:
                # È una consonante
                if carattere_lower in lettere_consonanti:
                    lettere_consonanti[carattere_lower] += 1
                else:
                    lettere_consonanti[carattere_lower] = 1
    
    # Calcolo totali
    conteggio_vocali = sum(lettere_vocali.values())
    conteggio_consonanti = sum(lettere_consonanti.values())
    
    return conteggio_vocali, conteggio_consonanti, lettere_vocali, lettere_consonanti



num_vocali, num_consonanti, dettaglio_vocali, dettaglio_consonanti = dizionario_conta_lettere(stringa_utente)

# Visualizzazione dei risultati
print(f"Nella stringa ci sono {num_vocali} vocali e {num_consonanti} consonanti")

print("\nDettaglio vocali:")
for vocale, conteggio in dettaglio_vocali.items():
    print(f"  {vocale}: {conteggio}")

print("\nDettaglio consonanti:")
for consonante, conteggio in dettaglio_consonanti.items():
    print(f"  {consonante}: {conteggio}")