# api_client.py
import time
import requests
from config import API_KEY, BASE_URL

def fetch_with_rate_limit(symbol, function, **params):
    """
    Esegue una chiamata API con gestione del rate limit
    
    Args:
        symbol: Simbolo dello strumento finanziario
        function: Funzione API di Alpha Vantage
        **params: Parametri aggiuntivi per la chiamata
    
    Returns:
        Dizionario con i dati della risposta o None in caso di errore
    """
    url = BASE_URL
    
    # Parametri di base per tutte le chiamate
    params_dict = {
        'function': function,
        'symbol': symbol,
        'apikey': API_KEY
    }
    
    # Aggiungiamo eventuali parametri extra
    params_dict.update(params)
    
    try:
        # Effettua la richiesta HTTP
        response = requests.get(url, params=params_dict)
        
        # Controlla se la risposta è valida
        if response.status_code == 200:
            data = response.json()
            
            # Verifica se ci sono messaggi di errore nell'API
            if "Error Message" in data:
                print(f"Errore API: {data['Error Message']}")
                return None
                
            print(f"Dati recuperati con successo per {symbol}")
            
            # Attesa di 12 secondi per rispettare il limite di 5 chiamate al minuto
            time.sleep(12)
            
            return data
        else:
            print(f"Errore nella richiesta: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Eccezione durante la chiamata API: {str(e)}")
        return None