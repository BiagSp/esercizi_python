# visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import os

def plot_price_with_ma(df, symbol, ma_periods=[20, 50], figsize=(12, 6), save_path=None):
    """
    Crea un grafico dell'andamento dei prezzi con medie mobili
    
    Args:
        df: DataFrame con i dati (deve avere colonne 'date' e 'close')
        symbol: Simbolo dello strumento finanziario
        ma_periods: Lista di periodi per le medie mobili
        figsize: Dimensioni del grafico
        save_path: Percorso dove salvare l'immagine (opzionale)
    """
    plt.figure(figsize=figsize)
    
    # Plottiamo il prezzo di chiusura
    plt.plot(df['date'], df['close'], label=f"{symbol} Prezzo", linewidth=2)
    
    # Aggiungiamo le medie mobili
    for period in ma_periods:
        if len(df) >= period:
            ma_col = f'MA_{period}'
            if ma_col not in df.columns:
                df[ma_col] = df['close'].rolling(window=period).mean()
            plt.plot(df['date'], df[ma_col], label=f'MA {period} giorni', 
                     linestyle='--', alpha=0.7)
    
    # Formattazione
    plt.title(f"Andamento di {symbol} con Medie Mobili", fontsize=16)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Prezzo ($)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Formattazione dell'asse X per date
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        print(f"Grafico salvato in {save_path}")
    else:
        plt.show()
        
def plot_comparative_performance(data_dict, start_date=None, figsize=(12, 6), save_path=None):
    """
    Crea un grafico di confronto della performance di diversi strumenti
    normalizzati a 100 dalla data di inizio
    
    Args:
        data_dict: Dizionario con simboli come chiavi e DataFrame come valori
        start_date: Data di inizio per il confronto (default: prima data comune)
        figsize: Dimensioni del grafico
        save_path: Percorso dove salvare l'immagine (opzionale)
    """
    plt.figure(figsize=figsize)
    
    # Determina la data di inizio se non specificata
    if start_date is None:
        # Trova l'intersezione delle date disponibili in tutti i DataFrame
        common_dates = set()
        first = True
        for df in data_dict.values():
            if first:
                common_dates = set(df['date'])
                first = False
            else:
                common_dates = common_dates.intersection(set(df['date']))
        
        if not common_dates:
            print("Nessuna data comune tra i dataset")
            return
        start_date = min(common_dates)
    
    # Crea DataFrame normalizzato per ogni simbolo
    for symbol, df in data_dict.items():
        # Filtra per date dopo la data di inizio
        temp_df = df[df['date'] >= start_date].copy()
        if len(temp_df) == 0:
            continue
            
        # Normalizza a 100 alla data di inizio
        first_price = temp_df.iloc[0]['close']
        temp_df['normalized'] = (temp_df['close'] / first_price) * 100
        
        # Plotta la serie normalizzata
        plt.plot(temp_df['date'], temp_df['normalized'], label=symbol, linewidth=2)
    
    # Formattazione
    plt.title("Confronto della Performance (Base 100)", fontsize=16)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Performance relativa', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Formattazione dell'asse X per date
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        print(f"Grafico salvato in {save_path}")
    else:
        plt.show()

def plot_correlation_heatmap(data_dict, days=90, figsize=(10, 8), save_path=None):
    """
    Crea una heatmap di correlazione tra diversi strumenti finanziari
    
    Args:
        data_dict: Dizionario con simboli come chiavi e DataFrame come valori
        days: Numero di giorni recenti da considerare
        figsize: Dimensioni del grafico
        save_path: Percorso dove salvare l'immagine (opzionale)
    """
    # Prepara un DataFrame con i rendimenti giornalieri di ciascuno strumento
    returns_data = {}
    
    for symbol, df in data_dict.items():
        if len(df) > days:
            # Prendiamo solo gli ultimi 'days' giorni
            temp_df = df.tail(days).copy()
            # Assicuriamoci di avere la colonna dei rendimenti giornalieri
            if 'daily_return' not in temp_df.columns:
                temp_df['daily_return'] = temp_df['close'].pct_change()
            # Aggiungiamo i rendimenti al dizionario
            returns_data[symbol] = temp_df['daily_return']
    
    if not returns_data:
        print("Dati insufficienti per la matrice di correlazione")
        return
    
    # Crea un DataFrame con tutti i rendimenti
    returns_df = pd.DataFrame(returns_data)
    
    # Calcola la matrice di correlazione
    corr_matrix = returns_df.corr()
    
    # Crea la heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, 
                linewidths=0.5, fmt=".2f")
    
    plt.title(f"Matrice di Correlazione (ultimi {days} giorni)", fontsize=16)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        print(f"Heatmap di correlazione salvata in {save_path}")
    else:
        plt.show()

def plot_drawdown(df, symbol, figsize=(12, 6), save_path=None):
    """
    Crea un grafico del drawdown (ribasso dal picco)
    
    Args:
        df: DataFrame con i dati (deve avere colonna 'close')
        symbol: Simbolo dello strumento finanziario
        figsize: Dimensioni del grafico
        save_path: Percorso dove salvare l'immagine (opzionale)
    """
    plt.figure(figsize=figsize)
    
    # Calcola il drawdown
    rolling_max = df['close'].cummax()
    drawdown = (df['close'] - rolling_max) / rolling_max * 100
    
    # Crea il grafico
    plt.fill_between(df['date'], drawdown, 0, color='red', alpha=0.3)
    plt.plot(df['date'], drawdown, color='red', linestyle='-', linewidth=1)
    
    # Formattazione
    plt.title(f"Drawdown di {symbol}", fontsize=16)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Drawdown (%)', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Aggiungi linea orizzontale a zero
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    
    # Formattazione dell'asse X per date
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.xticks(rotation=45)
    
    # Inverti l'asse Y perché i drawdown sono negativi
    plt.gca().invert_yaxis()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        print(f"Grafico di drawdown salvato in {save_path}")
    else:
        plt.show()