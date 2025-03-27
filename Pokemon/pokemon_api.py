"""
API su pokemon
"""

import requests
import json
import csv
import os

BASE_URL = "https://pokeapi.co/api/v2/"



def get_data_from_api():
    response = requests.get(BASE_URL)
    enpoints = response.json()
    pokemon_endpoint = f"{BASE_URL}/pokemon"

# Esploriamo l'endpoin pokemon
    response1 = requests.get(pokemon_endpoint)
    pokemon_data = response1.json()
    
    print("\nStruttura dell'endpoint Pokemon")
    print(f"Count: {pokemon_data.get('count')}")
    print(f"Next: {pokemon_data.get('next')}")
    print(f"Previous: {pokemon_data.get('previous')}")
    print("\nPrimi risultati:")
    
    """for item in pokemon_data.get('results',[])[:5]:
        print(f"- {item["name"]}: {item["url"]}")"""

    # Otteniamo informazioni dettagliate su un singolo Pokémon (Bulbasaur)
    pokemon_url = "https://pokeapi.co/api/v2/pokemon/1/"
    response = requests.get(pokemon_url)
    pokemon_detail = response.json()
    #vediamo quali chaivi sono disponibili nel risultato
    print("\nChiavi disponibili per singolo pokemon:")
    print(list(pokemon_detail.keys()))
    
    #Controlliamo che alcune delle informazioni che ci interessano
    print("\nEsempio di dati disponibili:")
    if "name" in pokemon_detail:
        print(f"Nome: {pokemon_detail["name"]}")
     
    if "stats" in pokemon_detail:
        for stat in pokemon_detail["stats"]:
            print(f"Stat: {stat["stat"]["name"]}, Valore: {stat["base_stat"]}")     
    
    
    if "abilities" in pokemon_detail:
        print("\nAbilità")
        for ability in pokemon_detail["abilities"]:
            print(f"- {ability["ability"]["name"]}")
            
    if "types" in pokemon_detail:
        print("\nTipi")
        
        for type_info in pokemon_detail["types"]:
            print(f"{type_info["type"]["name"]}")
    
    
    if "weight" in pokemon_detail:
        print(f"\nPeso {pokemon_detail["weight"]}")

    
    
import requests

def get_pokemon_list(limit=20):
    """
    Recupera un elenco di Pokémon dalla PokeAPI.
    """
    base_url = "https://pokeapi.co/api/v2"
    pokemon_endpoint = f"{base_url}/pokemon?limit={limit}&offset=0"
    
    print(f"Richiesta URL: {pokemon_endpoint}")
    response = requests.get(pokemon_endpoint)
    
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        print(f"Numero di Pokémon ricevuti: {len(results)}")
        return results[:limit]
    else:
        print(f"Errore nella richiesta: {response.status_code}")
        return []

def get_pokemon_details(pokemon_url):
    """
    Recupera i dettagli specifici di un Pokémon dalla sua URL.
    """
    print(f"Richiedendo dettagli da: {pokemon_url}")  # Debug: vediamo l'URL
    
    try:
        response = requests.get(pokemon_url)
        print(f"Status code: {response.status_code}")  # Debug: vediamo lo stato della risposta
        
        if response.status_code != 200:
            print(f"Errore nella richiesta: {response.status_code}")
            return None
        
        data = response.json()
        print(f"Dati ricevuti con successo per: {data.get('name', 'sconosciuto')}")  # Debug
        
        # Inizializziamo un dizionario per i dettagli che ci interessano
        pokemon_details = {
            'name': data['name'],
            'hp': None,
            'attack': None,
            'abilities': [],
            'types': [],
            'weight': data['weight'] / 10  # Convertiamo da ettogrammi a kg
        }
        
        # Estraiamo HP e Attacco dalle statistiche
        for stat in data['stats']:
            if stat['stat']['name'] == 'hp':
                pokemon_details['hp'] = stat['base_stat']
            elif stat['stat']['name'] == 'attack':
                pokemon_details['attack'] = stat['base_stat']
        
        # Estraiamo le abilità
        for ability in data['abilities']:
            pokemon_details['abilities'].append(ability['ability']['name'])
        
        # Estraiamo i tipi
        for type_info in data['types']:
            pokemon_details['types'].append(type_info['type']['name'])
        
        return pokemon_details
    
    except Exception as e:
        print(f"Errore durante il recupero dei dettagli: {str(e)}")
        return None

# Testiamo il flusso completo
def main():
    print("Inizio del programma...")
    
    # 1. Otteniamo la lista dei Pokémon
    pokemon_list = get_pokemon_list(5)
    
    if not pokemon_list:
        print("Nessun Pokémon trovato!")
        return
    
    # 2. Testiamo con il primo Pokémon
    print("\nTEST: Recupero dettagli per il primo Pokémon...")
    first_pokemon = pokemon_list[0]
    print(f"Nome: {first_pokemon['name']}, URL: {first_pokemon['url']}")
    
    details = get_pokemon_details(first_pokemon['url'])
    
    # 3. Verifichiamo che i dettagli non siano None prima di procedere
    if details:
        print("\nDettagli del primo Pokémon:")
        for key, value in details.items():
            print(f"{key}: {value}")
    else:
        print("\nNon è stato possibile recuperare i dettagli. Verifica le informazioni di debug sopra.")
    
    # 4. Solo se il test va bene, procediamo con tutti i Pokémon
    if details:
        print("\nRecupero dettagli per tutti i Pokémon nella lista...")
        all_pokemon_details = []
        
        for i, pokemon in enumerate(pokemon_list):
            print(f"\nRecupero dettagli per {pokemon['name']} ({i+1}/{len(pokemon_list)})...")
            pokemon_details = get_pokemon_details(pokemon['url'])
            
            if pokemon_details:
                all_pokemon_details.append(pokemon_details)
        
        # 5. Stampiamo tutti i dettagli in modo ordinato
        if all_pokemon_details:
            print("\n" + "="*50)
            print("DETTAGLI DEI POKÉMON RECUPERATI")
            print("="*50)
            
            for pokemon in all_pokemon_details:
                print("\n" + "-"*40)
                print(f"Nome: {pokemon['name'].title()}")
                print(f"HP: {pokemon['hp']}")
                print(f"Forza (Attacco): {pokemon['attack']}")
                print(f"Abilità: {', '.join(pokemon['abilities'])}")
                print(f"Tipi: {', '.join(pokemon['types'])}")
                print(f"Peso: {pokemon['weight']} kg")

# Eseguiamo il programma
if __name__ == "__main__":
    main()