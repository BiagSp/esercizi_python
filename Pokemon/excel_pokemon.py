import pandas as pd
import requests
import xlsxwriter
from Pokemon.pokemon_api import get_pokemon_list, get_pokemon_details



#Generazione del file excel per pokemon



def collect_pokemon_data(num_pokemon = 20):
    #raccogliamo dati per un numero specifico di pokemon
    #e restituiamo una listaa di dizionari con i dettagli
    print(f"Raccolta dati per {num_pokemon} Pokemon")
    
    pokemon_list = get_pokemon_list(num_pokemon)
    
    if not pokemon_list:
        print("Nessun pokemon in lista")
        return []
    
    #raccogliaamo i dettagli per ogni pokemon
    all_pokemon_details = []
    for i, pokemon in enumerate(pokemon_list):
        print(f"Recupero dettagli per {pokemon['name']}  ({i+1}/{len(pokemon_list)})...")
        pokemon_details =  get_pokemon_details(pokemon["url"])
        
        if pokemon_details:
            all_pokemon_details.append(pokemon_details)
            
    print(f"Raccolti dati per {len(all_pokemon_details)} Pokemon")
    return all_pokemon_details


def create_pokemon_excel(pokemon_data, filename= "pokemon_data.xlsx"):
    #creaiamo il file excel
    #e ordiniamo i dati per attacco (ordine crescente)
    
    if not pokemon_data:
        print("Nessun dato da salvare")
        return False
    
    try:
        #convertiamo la lista di dizionari in un DataFrame di pandas
        df = pd.DataFrame(pokemon_data)
        
        #Formattazione dei nomi dei pokemon Prima lettera maiuscola
        df["name"] = df["name"].str.capitalize()
        
        # Convertiamo le liste in stringhe ben formattate
        df["abilities"] = df["abilities"].apply(lambda x: ", ".join(x))
        df["types"] = df["types"].apply(lambda x: ", ".join(x))
        
        #ordiniamo il DataFrame per attacco (ordine crescente)
        df_sorted = df.sort_values(by= "attack")
        
        # Creazione del weiter excel con xlsxwriter come engine
        with pd.ExcelWriter(filename, engine="xlsxwriter") as writer:
            # Salviamo il DataFrame nel foglio Pokemon Data
            df_sorted.to_excel(writer, sheet_name="Pokemon Data", index=False)
            
            # Otteniamo il workbook e il worksheet per la formattazione
            workbook = writer.book
            worksheet = writer.sheets["Pokemon Data"]
            
            # Formattazione del titolo
            header_format = workbook.add_format({
                "bold": True,
                "font_color": "white",
                "bg_color": "#4F81BD",
                "align": "center",
                "valign": "vcenter",
                "border": 1                
            })
            
            # Applicazione del formato alle intestazioni
            for col_num, value in enumerate(df_sorted.columns.values):
                worksheet.write(0, col_num, value, header_format)
                
            num_format = workbook.add_format({"num_format": "0"})
            
            # Auto-fit larghezza colonne
            #Lunghezza del valore più lungo
            for i, col in enumerate(df_sorted.columns):
                column_width = max(df_sorted[col].astype(str).map(len).max(), len(col)) + 2
                worksheet.set_column(i,i, column_width)
            
            
            # Formattazione condizonale per l'attacco
            # Coloriamo gli attacchi alti in verde e quelli bassi in rosso
            
            worksheet.conditional_format(1, df_sorted.columns.get_loc("attack"), len(df_sorted) + 1,
                                         df_sorted.columns.get_loc("attack"), {
                                             'type': '3_color_scale',
                'min_color': '#FF9999',  # Rosso chiaro
                'mid_color': '#FFFF99',  # Giallo chiaro
                'max_color': '#99CC99'   # Verde chiaro
                                         })
                
            # Formattazione condizionale per l'HP
            worksheet.conditional_format(1, df_sorted.columns.get_loc('hp'), len(df_sorted) + 1, 
                                       df_sorted.columns.get_loc('hp'), {
                'type': '3_color_scale',
                'min_color': '#FF9999',  # Rosso chiaro
                'mid_color': '#FFFF99',  # Giallo chiaro
                'max_color': '#99CC99'   # Verde chiaro
            })

            # Aggiunta di filtri
            worksheet.autofilter(0,0,len(df_sorted), len(df_sorted.columns) - 1)
            
            # Congelamento della prima riga (intestazioni)
            worksheet.freeze_panes(1,0)
            
            # Aggiunta di un foglio con statistiche riassuntive
            stats_df = pd.DataFrame({
                "Statistica": [
                     "Media HP", "HP Massimo", "Media Attacco", "Attacco massimo",
                     "Peso Medio (Kg)", "Peso massimo (Kg)", "Numero totale di pokemon"
                ],
                "Valore": [
                    df["hp"].mean(), df["hp"].max(), df["attack"].mean(),  df['attack'].max(),
                    df['weight'].mean(), df['weight'].max(), len(df)
                ]
            })
            
            stats_df.to_excel(writer, sheet_name="Statistiche", index=False)
            stats_worksheet = writer.sheets["Statistiche"]
            
            # Formattazione intestazioni statistiche
            stats_worksheet.set_column(0, 0, 20)
            stats_worksheet.set_column(1, 1, 15)
            
            
            # Creiamo un foglio aggiuntivo per i grafici
            top_attackers = df_sorted.sort_values(by="attack", ascending=False).head(10)
            top_attackers.to_excel(writer, sheet_name="Top 10 Attaccanti", index=False)
            chart_sheet = writer.sheets["Top 10 Attaccanti"]
            
            
            # Formattaazione delle intestazioni
            for col_num, value in enumerate(top_attackers.columns.values):
                chart_sheet.write(0, col_num, value, header_format)
                
            # Creiamo un grafico a barre per i top attacanti
            chart = workbook.add_chart({"type": "column"})
            
            # Configuriamo il grafico
            chart.add_series({
                'name': 'Attacco',
                'categories': ['Top 10 Attaccanti', 1, df_sorted.columns.get_loc('name'), 10, df_sorted.columns.get_loc('name')],
                'values': ['Top 10 Attaccanti', 1, df_sorted.columns.get_loc('attack'), 10, df_sorted.columns.get_loc('attack')],
                'data_labels': {'value': True}
            })
            
            # Personalizziamo il grafico
            chart.set_title({"name": "Top 10 Pokemon per Attacco"})
            chart.set_x_axis({'name': 'Pokémon'})
            chart.set_y_axis({'name': 'Valore Attacco'})
            chart.set_style(11)  # Stile grafico
            
            chart_sheet.insert_chart("H2", chart, {"x_scale": 1.5, "y_scale": 1.5})
            
        print(f"File excel {filename} creato con successo!")
        return True
            
            
            
            
    except Exception as e:
        print(f"Errore durante la creazione del file Excel: {str(e)}")
        return False
    
    
def main():
    #Funzione pricipale per la coordinazione del programma
    
    num_pokemon = 100
    
    print("inizio raccolta dati...")
    pokemon_data = collect_pokemon_data(num_pokemon)
    
    if not pokemon_data:
        print("Impossibile procedere: nessun dato raccolto")
        return False
    
    #Creiamo il file Excel
    create_pokemon_excel(pokemon_data, "pokemon_stats.xlsx")
    print("Operazione completata")
    
if __name__ == "__main__":
    main()