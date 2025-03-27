"""
Dato un elenco di temperature giornaliere, identifica e rimuovi i valori anomali (outlier). Definisci come outlier i valori che:

Compaiono una sola volta nell'elenco (sono unici)
Sono distanti più di 10 gradi dalla media delle altre temperature

"""
temperature = [22, 24, 23, 22, 24, 45, 23, 21, 22]

def remove_outliers(temperature):
    # FASE 1: CONTEGGIO DELLE OCCORRENZE
    # Creiamo un dizionario vuoto per contare quante volte appare ogni temperatura
    count_dict = {}

    # Iteriamo su tutte le temperature e incrementiamo il contatore per ciascuna
    for temp in temperature:
        if temp in count_dict:
            count_dict[temp] += 1  # Se già presente, incrementiamo il conteggio
        else:
            count_dict[temp] = 1   # Altrimenti, inizializziamo il conteggio a 1
    
    # A questo punto count_dict contiene {22: 3, 24: 2, 23: 2, 45: 1, 21: 1}

    # FASE 2: IDENTIFICAZIONE DELLE TEMPERATURE UNICHE
    # Creiamo un set vuoto per memorizzare le temperature che appaiono una sola volta
    unique_temps = set() 

    # Iteriamo sulle coppie (temperatura, conteggio) del dizionario
    for temp, count in count_dict.items():
        if count == 1:  # Se la temperatura appare esattamente una volta
            unique_temps.add(temp)  # La aggiungiamo al set delle temperature uniche
    
    # Ora unique_temps contiene {45, 21} - le temperature che appaiono una sola volta

    # FASE 3: CALCOLO DELLA MEDIA "NORMALE"
    # Creiamo una lista con solo le temperature che NON sono uniche (esclusi i potenziali outlier)
    non_unique_temps = [temp for temp in temperature if temp not in unique_temps]
    # non_unique_temps = [22, 24, 23, 22, 24, 23, 22]

    # Calcoliamo la media delle temperature non uniche
    avg_temp = sum(non_unique_temps) / len(non_unique_temps)
    # La media è circa 22.86

    # FASE 4: IDENTIFICAZIONE DEGLI OUTLIER VERI E PROPRI
    # Creiamo un set per memorizzare gli outlier definitivi
    outliers = set()
    
    # Per ogni temperatura unica, verifichiamo se è distante più di 10 gradi dalla media
    for temp in unique_temps:
        if abs(temp - avg_temp) > 10:  # Se la differenza assoluta è maggiore di 10
            outliers.add(temp)  # La temperatura è un outlier
    
    # Ora outliers contiene {45} - solo 45 è un vero outlier (21 è abbastanza vicino alla media)

    # FASE 5: CREAZIONE DEL RISULTATO FINALE
    # Creiamo la lista risultato escludendo gli outlier
    result = [temp for temp in temperature if temp not in outliers]
    # result = [22, 24, 23, 22, 24, 23, 21, 22]

    return result

print(remove_outliers(temperature))