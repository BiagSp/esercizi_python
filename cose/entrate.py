import matplotlib.pyplot as plt
# Se non l'hai installato:
# pip install prophet
from prophet import Prophet


mesi = ["Gen","Feb","Mar","Apr","Mag","Giu","Lug","Ago","Set","Ott","Nov","Dic"]
totali = [622.99, 530, 650, 720, 406, 998, 1009, 1410.27, 622.34, 1293.78, 1154.76, 1066.91]

plt.figure(figsize=(10,5))
plt.plot(mesi, totali, marker='o')
plt.title("Andamento TOTALE mensile")
plt.xlabel("Mese")
plt.ylabel("Valore (€)")
plt.grid(True)
plt.show()

model = Prophet()
model.fit(totali)

future = model.make_future_dataframe(periods=12, freq='MS')  # 12 mesi in più
forecast = model.predict(future)

# Stampa le colonne principali
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12))

model.plot(forecast);
model.plot_components(forecast);

