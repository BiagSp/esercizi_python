# main.py
import os
import pandas as pd
from datetime import datetime
from config import API_KEY, BASE_URL
from api_client import fetch_with_rate_limit
from data_processor import process_time_series, calculate_metrics
from visualizer import plot_price_with_ma, plot_comparative_performance, plot_correlation_heatmap, plot_drawdown
from excel_exporter import export_to_excel

# Lista di ETF e obbligazioni da analizzare
SYMBOLS = {
    'SPY': 'SPDR S&P 500 ETF',
    'AGG': 'iShares Core U.S. Aggregate Bond',
    'VTI': 'Vanguard Total Stock Market ETF',
    'BND': 'Vanguard Total Bond Market ETF',
    'TLT': 'iShares 20+ Year Treasury Bond ETF',
    'LQD': 'iShares iBoxx $ Investment Grade Corporate Bond ETF'
}

def main():
    """Funzione principale del programma"""
    print("Avvio dell'analisi di ETF e Obbligazioni...")
    
    # Dizionari per memorizzare dati e metriche
    data_dict = {}
    metrics_dict = {}
    
    # Directory per i grafici
    charts_dir = "charts"
    os.makedirs(charts_dir, exist_ok=True)
    
    # 1. Recupera e processa i dati per ogni simbolo
    for symbol, name in SYMBOLS.items():
        print(f"Elaborazione di {symbol} ({name})...")
        
        # Recupera dati dalla API
        raw_data = fetch_with_rate_limit(
            symbol=symbol,
            function='TIME_SERIES_DAILY',
            outputsize='full'  # Per avere più dati storici
        )
        
        if not raw_data or "Time Series (Daily)" not in raw_data:
            print(f"Impossibile recuperare dati per {symbol}. Salto al prossimo.")
            continue
        
        # Processa i dati grezzi in un DataFrame
        df = process_time_series(raw_data)
        
        if df is not None and not df.empty:
            # Calcola metriche
            metrics = calculate_metrics(df)
            
            # Salva dati e metriche
            data_dict[symbol] = df
            metrics_dict[symbol] = metrics
            
            # Crea visualizzazione individuale
            save_path = os.path.join(charts_dir, f"{symbol}_price_chart.png")
            plot_price_with_ma(df, symbol, save_path=save_path)
            
            print(f"Elaborazione completata per {symbol}.")
        else:
            print(f"DataFrame vuoto per {symbol}. Salto al prossimo.")
    
    # 2. Crea visualizzazione comparativa
    if len(data_dict) >= 2:
        compare_path = os.path.join(charts_dir, "comparative_performance.png")
        plot_comparative_performance(data_dict, save_path=compare_path)
        
        # Crea heatmap di correlazione
        print("Creazione heatmap di correlazione...")
        corr_path = os.path.join(charts_dir, "correlation_heatmap.png")
        plot_correlation_heatmap(data_dict, save_path=corr_path)
    
    # Crea grafici di drawdown per ogni simbolo
    for symbol, df in data_dict.items():
        print(f"Creazione grafico drawdown per {symbol}...")
        drawdown_path = os.path.join(charts_dir, f"{symbol}_drawdown.png")
        plot_drawdown(df, symbol, save_path=drawdown_path)
    
    # 3. Esporta tutto in Excel
    if data_dict:
        export_to_excel(data_dict, metrics_dict, "etf_bond_analysis.xlsx")
        print("File Excel creato con successo!")
    else:
        print("Nessun dato da esportare in Excel.")
    
    print("Analisi completata!")

if __name__ == "__main__":
    main()