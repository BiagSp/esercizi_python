import pandas as pd
import numpy as np
from statsmodels.tsa.api import SimpleExpSmoothing, Holt
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# 1) Carica i dati in un DataFrame
# Supponiamo di avere un CSV o di inserire manualmente i 12 valori totali
# (uno per ciascun mese) in un array Python:

data = {
    'month':
    pd.date_range(start='2023-01', periods=12, freq='M'),
    'spese_totali': [
        356.3, 609.19, 838.33, 654.49, 559.52, 548.94, 580.32, 730.49, 377.64,
        297.09, 357.16, 242.95
    ]
}
df = pd.DataFrame(data).set_index('month')

# 2) Scegli un modello: Simple Exponential Smoothing (SES)
ses_model = SimpleExpSmoothing(df['spese_totali']).fit()
df['SES_fitted'] = ses_model.fittedvalues

# 3) Fai una previsione per i prossimi 3 mesi
forecast_ses = ses_model.forecast(3)
print("Forecast SES:", forecast_ses)

# 4) Se vuoi testare Holt per catturare un piccolo trend:
holt_model = Holt(df['spese_totali']).fit()
df['Holt_fitted'] = holt_model.fittedvalues
forecast_holt = holt_model.forecast(3)
print("Forecast Holt:", forecast_holt)

# 5) Prova anche un ARIMA semplice, per confrontare:
arima_model = ARIMA(df['spese_totali'], order=(0, 1, 1)).fit()
df['ARIMA_fitted'] = arima_model.fittedvalues
forecast_arima = arima_model.forecast(3)
print("Forecast ARIMA:", forecast_arima)

# (Facoltativo) Visualizza i risultati
df[['spese_totali', 'SES_fitted', 'Holt_fitted',
    'ARIMA_fitted']].plot(figsize=(10, 5))
plt.title("Confronto modelli di base")
plt.show()
