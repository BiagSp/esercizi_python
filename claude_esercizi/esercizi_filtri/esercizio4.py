"""
Esercizio filtraggio dizionari liste
"""

dati_meteo = [
    {"città": "Roma", "temp_max": 32.5, "temp_min": 21.3, "umidità": 65, "precipitazioni": 0, "vento": 12},
    {"città": "Milano", "temp_max": 28.7, "temp_min": 18.2, "umidità": 72, "precipitazioni": 3.2, "vento": 8},
    {"città": "Napoli", "temp_max": 33.1, "temp_min": 22.5, "umidità": 68, "precipitazioni": 0, "vento": 15},
    {"città": "Torino", "temp_max": 27.5, "temp_min": 17.8, "umidità": 70, "precipitazioni": 5.1, "vento": 9},
    {"città": "Firenze", "temp_max": 31.8, "temp_min": 20.5, "umidità": 63, "precipitazioni": 0, "vento": 7},
    {"città": "Bologna", "temp_max": 30.2, "temp_min": 19.8, "umidità": 67, "precipitazioni": 1.5, "vento": 11},
    {"città": "Palermo", "temp_max": 34.2, "temp_min": 24.1, "umidità": 60, "precipitazioni": 0, "vento": 14},
    {"città": "Genova", "temp_max": 29.3, "temp_min": 21.5, "umidità": 75, "precipitazioni": 2.8, "vento": 18},
    {"città": "Bari", "temp_max": 32.7, "temp_min": 23.2, "umidità": 62, "precipitazioni": 0, "vento": 16},
    {"città": "Cagliari", "temp_max": 33.5, "temp_min": 22.8, "umidità": 58, "precipitazioni": 0, "vento": 13}
]


#Filtrare per temperatura compresa tra 28-33 e vento moderato inferiore a 15km/h

def gita(day):
    return list(filter(lambda d: d["temp_max"] < 33 and d["temp_min"] > 18 and d["vento"] < 15, day))


#print(gita(dati_meteo))


# Esercizio 2 Ecommerce



prodotti = [
    {"id": 101, "nome": "Smartphone Pro", "categoria": "Elettronica", "prezzo": 899, "disponibilità": True, "valutazione": 4.7, "caratteristiche": ["5G", "Fotocamera 48MP", "Impermeabile"]},
    {"id": 102, "nome": "Laptop Ultra", "categoria": "Elettronica", "prezzo": 1299, "disponibilità": True, "valutazione": 4.5, "caratteristiche": ["SSD 1TB", "16GB RAM", "GPU Dedicata"]},
    {"id": 103, "nome": "Auricolari Wireless", "categoria": "Accessori", "prezzo": 129, "disponibilità": False, "valutazione": 4.2, "caratteristiche": ["Bluetooth 5.0", "Cancellazione Rumore", "Impermeabile"]},
    {"id": 104, "nome": "Monitor 4K", "categoria": "Elettronica", "prezzo": 349, "disponibilità": True, "valutazione": 4.8, "caratteristiche": ["HDR", "USB-C", "Regolabile in altezza"]},
    {"id": 105, "nome": "Smartwatch Fitness", "categoria": "Wearable", "prezzo": 199, "disponibilità": True, "valutazione": 4.0, "caratteristiche": ["GPS", "Cardiofrequenzimetro", "Impermeabile"]},
    {"id": 106, "nome": "Cuffie Gaming", "categoria": "Accessori", "prezzo": 89, "disponibilità": True, "valutazione": 4.3, "caratteristiche": ["Surround 7.1", "Microfono", "Controlli Volume"]},
    {"id": 107, "nome": "Tablet Pro", "categoria": "Elettronica", "prezzo": 649, "disponibilità": False, "valutazione": 4.6, "caratteristiche": ["Pennino", "128GB", "Face Unlock"]},
    {"id": 108, "nome": "Mouse Ergonomico", "categoria": "Accessori", "prezzo": 49, "disponibilità": True, "valutazione": 3.9, "caratteristiche": ["Wireless", "Batteria lunga durata", "DPI regolabili"]},
    {"id": 109, "nome": "Altoparlante Bluetooth", "categoria": "Audio", "prezzo": 79, "disponibilità": True, "valutazione": 4.4, "caratteristiche": ["Impermeabile", "20h batteria", "Connessione multipla"]},
    {"id": 110, "nome": "E-reader", "categoria": "Elettronica", "prezzo": 129, "disponibilità": True, "valutazione": 4.5, "caratteristiche": ["E-ink", "Retroilluminazione", "Impermeabile"]}
]



# Filtrare per prodotti impermeabili, disponibili, con valutazione superiore a 4.2 e prezzo inferiore a 200€


def filter_prod(prod):
    return list(filter(lambda p: p["disponibilità"] == True and p["valutazione"] > 4.2 and p["prezzo"] < 200 and all(impermeabile in p["caratteristiche"] for impermeabile in ["Impermeabile"]), prod))


print(filter_prod(prodotti))


# Filtrare dati atleti per età inferiore a 25 anni e non infortunati e che abbiamo vinto almeno una medaglia d'oro o partecipato a più olimpiadi

atleti = [
    {"nome": "Marco Rossi", "sport": "Nuoto", "età": 24, "medaglie": ["oro", "argento", "bronzo"], "record_personale": 51.2, "olimpiadi_partecipate": 2, "infortunato": False},
    {"nome": "Giulia Bianchi", "sport": "Atletica", "età": 28, "medaglie": ["oro", "oro"], "record_personale": 10.92, "olimpiadi_partecipate": 3, "infortunato": False},
    {"nome": "Alessandro Verdi", "sport": "Ciclismo", "età": 32, "medaglie": ["argento"], "record_personale": 3.45, "olimpiadi_partecipate": 4, "infortunato": True},
    {"nome": "Sofia Romano", "sport": "Nuoto", "età": 22, "medaglie": [], "record_personale": 53.1, "olimpiadi_partecipate": 1, "infortunato": False},
    {"nome": "Luca Ferrari", "sport": "Scherma", "età": 29, "medaglie": ["oro", "argento", "argento", "bronzo"], "record_personale": None, "olimpiadi_partecipate": 3, "infortunato": False},
    {"nome": "Chiara Esposito", "sport": "Ginnastica", "età": 19, "medaglie": ["oro", "bronzo"], "record_personale": 15.8, "olimpiadi_partecipate": 1, "infortunato": True},
    {"nome": "Davide Moretti", "sport": "Atletica", "età": 25, "medaglie": ["bronzo"], "record_personale": 11.03, "olimpiadi_partecipate": 2, "infortunato": False},
    {"nome": "Elena Ricci", "sport": "Scherma", "età": 27, "medaglie": ["oro", "oro", "argento"], "record_personale": None, "olimpiadi_partecipate": 2, "infortunato": False},
    {"nome": "Francesco Marino", "sport": "Ciclismo", "età": 33, "medaglie": ["argento", "bronzo"], "record_personale": 3.42, "olimpiadi_partecipate": 4, "infortunato": False},
    {"nome": "Valentina Greco", "sport": "Ginnastica", "età": 20, "medaglie": [], "record_personale": 15.2, "olimpiadi_partecipate": 1, "infortunato": False}
]

def atleties(atlete):
    return list(filter(lambda a: a["età"] <= 25 and a["infortunato"] == False and ("oro" in a["medaglie"] or a["olimpiadi_partecipate"] > 1), atlete))


print(atleties(atleti))





# Filtraggio libri bilbioteca, filtrare per libri storici o di avventura pubblicati prima del 1950 con più di 300 pagine e disponibili

biblioteca = [
    {"titolo": "Il Nome della Rosa", "autore": "Umberto Eco", "genere": ["Storico", "Giallo"], "anno": 1980, "pagine": 536, "disponibile": True, "valutazione": 4.2, "prestiti": 28},
    {"titolo": "1984", "autore": "George Orwell", "genere": ["Distopico", "Fantascienza"], "anno": 1949, "pagine": 328, "disponibile": False, "valutazione": 4.5, "prestiti": 42},
    {"titolo": "Fondazione", "autore": "Isaac Asimov", "genere": ["Fantascienza"], "anno": 1951, "pagine": 255, "disponibile": True, "valutazione": 4.3, "prestiti": 35},
    {"titolo": "Il Signore degli Anelli", "autore": "J.R.R. Tolkien", "genere": ["Fantasy", "Avventura"], "anno": 1954, "pagine": 1178, "disponibile": True, "valutazione": 4.7, "prestiti": 53},
    {"titolo": "Orgoglio e Pregiudizio", "autore": "Jane Austen", "genere": ["Romanzo", "Romantico"], "anno": 1813, "pagine": 432, "disponibile": False, "valutazione": 4.4, "prestiti": 39},
    {"titolo": "Cronache del Ghiaccio e del Fuoco", "autore": "George R.R. Martin", "genere": ["Fantasy", "Epico"], "anno": 1996, "pagine": 835, "disponibile": True, "valutazione": 4.6, "prestiti": 47},
    {"titolo": "Lo Hobbit", "autore": "J.R.R. Tolkien", "genere": ["Fantasy", "Avventura"], "anno": 1937, "pagine": 310, "disponibile": False, "valutazione": 4.5, "prestiti": 41},
    {"titolo": "Dune", "autore": "Frank Herbert", "genere": ["Fantascienza", "Avventura"], "anno": 1965, "pagine": 655, "disponibile": True, "valutazione": 4.5, "prestiti": 36},
    {"titolo": "Il Conte di Montecristo", "autore": "Alexandre Dumas", "genere": ["Avventura", "Storico"], "anno": 1844, "pagine": 1276, "disponibile": True, "valutazione": 4.3, "prestiti": 31},
    {"titolo": "Neuromante", "autore": "William Gibson", "genere": ["Fantascienza", "Cyberpunk"], "anno": 1984, "pagine": 271, "disponibile": False, "valutazione": 4.1, "prestiti": 25}
]


def filtered_book(book):
    return list(filter(lambda b: ("Storico" in b["genere"] or "Avventura" in b["genere"] and b["pagine"] > 300) and b["anno"] < 1950 and b["disponibile"] == True, book))

# Usando i set:
def filtered_book(book):
    generi_target = {"Storico", "Avventura"}  # Set di generi target
    return list(filter(
        lambda b: (
            bool(set(b["genere"]) & generi_target) and  # Verifica se c'è intersezione tra i set
            b["pagine"] > 300 and 
            b["anno"] < 1950 and 
            b["disponibile"] == True
        ), 
        book
    ))

print(filtered_book(biblioteca))



# Filtrare transazioni bacarie in uscita e di importo superiore a 100€ effettuate con bonifico o carta di credito e se ci sono 
# ancora il elaborazione

transazioni = [
    {"id": "T1001", "data": "2023-01-15", "importo": 1250.50, "categoria": "Stipendio", "tipo": "Entrata", "controparte": "Azienda XYZ", "metodo": "Bonifico", "stato": "Completata"},
    {"id": "T1002", "data": "2023-01-20", "importo": 85.30, "categoria": "Alimentari", "tipo": "Uscita", "controparte": "Supermercato ABC", "metodo": "Carta di Credito", "stato": "Completata"},
    {"id": "T1003", "data": "2023-01-25", "importo": 45.00, "categoria": "Trasporti", "tipo": "Uscita", "controparte": "Distributore DEF", "metodo": "Carta di Debito", "stato": "Completata"},
    {"id": "T1004", "data": "2023-02-01", "importo": 450.00, "categoria": "Affitto", "tipo": "Uscita", "controparte": "Proprietario Casa", "metodo": "Bonifico", "stato": "Completata"},
    {"id": "T1005", "data": "2023-02-05", "importo": 120.75, "categoria": "Abbigliamento", "tipo": "Uscita", "controparte": "Negozio GHI", "metodo": "Carta di Credito", "stato": "In elaborazione"},
    {"id": "T1006", "data": "2023-02-15", "importo": 1250.50, "categoria": "Stipendio", "tipo": "Entrata", "controparte": "Azienda XYZ", "metodo": "Bonifico", "stato": "Completata"},
    {"id": "T1007", "data": "2023-02-18", "importo": 35.20, "categoria": "Intrattenimento", "tipo": "Uscita", "controparte": "Cinema JKL", "metodo": "Contanti", "stato": "Completata"},
    {"id": "T1008", "data": "2023-02-25", "importo": 68.90, "categoria": "Alimentari", "tipo": "Uscita", "controparte": "Supermercato MNO", "metodo": "Carta di Debito", "stato": "Completata"},
    {"id": "T1009", "data": "2023-03-01", "importo": 450.00, "categoria": "Affitto", "tipo": "Uscita", "controparte": "Proprietario Casa", "metodo": "Bonifico", "stato": "In elaborazione"},
    {"id": "T1010", "data": "2023-03-10", "importo": 350.00, "categoria": "Regalo", "tipo": "Uscita", "controparte": "Negozio PQR", "metodo": "Carta di Credito", "stato": "Completata"}
]


def filtered_transaction(transaction):
    return list(filter(
        lambda t: (
            t["tipo"] == "Uscita" and  # Transazioni in uscita
            t["importo"] > 100 and     # Importo superiore a 100€
            (t["metodo"] == "Bonifico" or t["metodo"] == "Carta di Credito") and  # Metodo di pagamento
            t["stato"] == "In elaborazione"  # Stato della transazione
        ),
        transaction
    ))


print(filtered_transaction(transazioni))