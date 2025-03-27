"""
Verificare quale metodo sia migliore per impilare delle scatole (6 scatole) tra:
- impilare una fila per volta usando due braccia
- impilare due file per volta usando due braccia
tempo per manovra = 2sec
scatole totali (varibile) = 60

"""


scatole_totali = 60
tempo_per_manovra = 2  # secondi per ogni manovra

def metodo_una_fila(n_scatole, scatole_per_manovra, tempo_manovra):
    """
    Calcola il tempo per impilare scatole in una singola fila.
    
    Args:
        n_scatole: Numero totale di scatole
        scatole_per_manovra: Numero di scatole movimentate per operazione
        tempo_manovra: Tempo necessario per ogni manovra in secondi
    """
    movimenti = n_scatole / scatole_per_manovra
    tempo_totale = movimenti * tempo_manovra
    return tempo_totale

def metodo_due_file(n_scatole, scatole_per_manovra, tempo_manovra):
    """
    Calcola il tempo per impilare scatole in due file parallele.
    
    Args:
        n_scatole: Numero totale di scatole
        scatole_per_manovra: Numero di scatole movimentate per operazione
        tempo_manovra: Tempo necessario per ogni manovra in secondi
    """
    # Dividiamo le scatole equamente tra le due file
    scatole_per_fila = n_scatole / 2
    
    # Calcoliamo i movimenti necessari per una fila
    movimenti = scatole_per_fila / scatole_per_manovra
    
    # Il tempo totale è dato dai movimenti per una fila
    # (poiché le operazioni avvengono in parallelo)
    tempo_totale = movimenti * tempo_manovra
    return tempo_totale

# Confronto dei due metodi (2 scatole per manovra in entrambi i casi)
tempo_metodo_1 = metodo_una_fila(scatole_totali, 2, tempo_per_manovra)
tempo_metodo_2 = metodo_due_file(scatole_totali, 1, tempo_per_manovra)

print(f"Tempo con metodo a una fila: {tempo_metodo_1} secondi")
print(f"Tempo con metodo a due file: {tempo_metodo_2} secondi")