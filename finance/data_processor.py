# data_processor.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def calculate_metrics(df, risk_free_rate=0.02):
    """
    Calcola le principali metriche finanziarie per uno strumento
    
    Args:
        df: DataFrame con i dati storici (deve contenere 'close')
        risk_free_rate: Tasso privo di rischio annualizzato
    
    Returns:
        Dizionario con le metriche calcolate
    """
    metrics = {}
    
    # Assicurati che ci siano abbastanza dati
    if len(df) < 2:
        return metrics
    
    # Ordina per data crescente se necessario
    if 'date' in df.columns:
        df = df.sort_values('date')
    
    # Calcola rendimenti giornalieri
    df['daily_return'] = df['close'].pct_change()
    
    # --- Performance ---
    
    # Ultimo prezzo
    metrics['Ultimo Prezzo ($)'] = round(df['close'].iloc[-1], 2)
    
    # Rendimento YTD
    current_year = datetime.now().year
    start_of_year = df[df['date'].dt.year == current_year].iloc[0] if 'date' in df.columns else None
    if start_of_year is not None:
        ytd_return = (df['close'].iloc[-1] / start_of_year['close']) - 1
        metrics['Rendimento YTD (%)'] = round(ytd_return * 100, 2)
    
    # Rendimenti a vari orizzonti temporali
    for days, label in [(30, '1M'), (90, '3M'), (180, '6M'), (365, '1Y')]:
        if len(df) > days:
            period_return = (df['close'].iloc[-1] / df['close'].iloc[-days]) - 1
            metrics[f'Rendimento {label} (%)'] = round(period_return * 100, 2)
    
    # --- Rischio ---
    
    # Volatilità (annualizzata)
    if len(df) >= 20:  # Almeno 20 giorni di dati
        volatility = df['daily_return'].std() * np.sqrt(252)  # Annualizzata assumendo 252 giorni di trading
        metrics['Volatilità (%)'] = round(volatility * 100, 2)
    
    # Maximum Drawdown
    rolling_max = df['close'].cummax()
    drawdown = (df['close'] - rolling_max) / rolling_max
    max_drawdown = drawdown.min()
    metrics['Maximum Drawdown (%)'] = round(max_drawdown * 100, 2)
    
    # Sharpe Ratio (annualizzato)
    if 'Volatilità (%)' in metrics and len(df) >= 252:  # Almeno un anno di dati
        annual_return = df['daily_return'].mean() * 252
        sharpe = (annual_return - risk_free_rate) / (metrics['Volatilità (%)'] / 100)
        metrics['Sharpe Ratio'] = round(sharpe, 2)
    
    # Beta (se abbiamo un benchmark)
    # Il calcolo del Beta richiederebbe dati di un indice di riferimento
    
    return metrics

def process_time_series(raw_data):
    """
    Converte i dati grezzi dell'API Alpha Vantage in un DataFrame di pandas.
    
    Args:
        raw_data: Dizionario JSON dalla risposta dell'API Alpha Vantage
    
    Returns:
        DataFrame di pandas con i dati strutturati o None se ci sono errori
    """
    # Verifica che i dati contengano la serie temporale
    if "Time Series (Daily)" not in raw_data:
        print("Formato dati non valido: 'Time Series (Daily)' non trovato")
        return None
    
    # Estrai la serie temporale
    time_series = raw_data["Time Series (Daily)"]
    
    # Converti in DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')
    
    # Rinomina le colonne (rimuovi i prefissi numerici)
    df.columns = [col.split('. ')[1] for col in df.columns]
    
    # Converti i valori in numeri
    for col in df.columns:
        df[col] = pd.to_numeric(df[col])
    
    # Aggiungi la data come colonna (non solo indice)
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'date'}, inplace=True)
    
    # Converti la colonna data in datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Ordina per data crescente
    df = df.sort_values('date')
    
    # Calcola alcune metriche aggiuntive
    # Media mobile a 20 giorni
    df['MA_20'] = df['close'].rolling(window=20).mean()
    
    # Media mobile a 50 giorni
    df['MA_50'] = df['close'].rolling(window=50).mean()
    
    # Variazione percentuale giornaliera
    df['daily_return'] = df['close'].pct_change()
    
    return df