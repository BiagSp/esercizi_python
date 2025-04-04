"""
Filtrare una lista di dizionari in base a proprietà specifiche
Creare un nuovo dizionario applicando un filtro sia alle chiavi che ai valori
Combinare filtri con map o reduce per trasformare dati

"""

#esercizio con map
prodotti = [
    {"id": 1, "nome": "Laptop Pro", "categoria": "Elettronica", "prezzo": 1200, "disponibilità": 10, "valutazione": 4.5},
    {"id": 2, "nome": "Smartphone X", "categoria": "Elettronica", "prezzo": 800, "disponibilità": 15, "valutazione": 4.2},
    {"id": 3, "nome": "Auricolari Wireless", "categoria": "Accessori", "prezzo": 150, "disponibilità": 30, "valutazione": 4.0},
    {"id": 4, "nome": "Monitor 4K", "categoria": "Elettronica", "prezzo": 350, "disponibilità": 5, "valutazione": 4.7},
    {"id": 5, "nome": "Tastiera Meccanica", "categoria": "Accessori", "prezzo": 100, "disponibilità": 20, "valutazione": 4.3},
    {"id": 6, "nome": "Mouse Ergonomico", "categoria": "Accessori", "prezzo": 50, "disponibilità": 25, "valutazione": 3.9},
    {"id": 7, "nome": "Stampante Laser", "categoria": "Elettronica", "prezzo": 200, "disponibilità": 8, "valutazione": 4.1},
    {"id": 8, "nome": "Webcam HD", "categoria": "Accessori", "prezzo": 80, "disponibilità": 12, "valutazione": 4.4},
    {"id": 9, "nome": "Tablet Mini", "categoria": "Elettronica", "prezzo": 300, "disponibilità": 7, "valutazione": 4.0},
    {"id": 10, "nome": "Cuffie Noise-Canceling", "categoria": "Accessori", "prezzo": 180, "disponibilità": 18, "valutazione": 4.6}
]




"""
Filtrare solo i prodotti con valutazione ≥ 4.3
Trasformare (map) ogni prodotto in un valore che rappresenta il suo valore totale di inventario (prezzo × disponibilità)
Aggregare (reduce) questi valori per categoria

"""


from functools import reduce
from collections import defaultdict

def filter_product(prod):
    prod_filter_values = []
    
    for p in prod:
        if p["valutazione"] >= 4.3:
            prod_filter_values.append(p)
    return prod_filter_values

# Or 
def filter_product(prod):
    return list(filter(lambda p: p["valutazione"] >= 4.3, prod))


def mapping_result(prod):
    return list(map(lambda product : {
        "id": product["id"],
        "categoria": product["categoria"],
        "valore_inventario": product["prezzo"] * product["disponibilità"]
    },
        prod
    ))


def analyze_inventory(mapped_products):
    def reducer(acc, product):
        acc[product["categoria"]] += product["prezzo"]
        return acc
    return reduce(reducer, mapped_products, defaultdict(int))

#print(filter_product(prodotti), "filter per valori >= 4.3", mapping_result(prodotti), "Mappinng prodotti")
print(analyze_inventory(prodotti))













voti_studenti = {
    "Marco": {"Matematica": 85, "Storia": 72, "Fisica": 90, "Inglese": 78},
    "Giulia": {"Matematica": 92, "Storia": 88, "Chimica": 95, "Inglese": 89},
    "Luca": {"Matematica": 65, "Storia": 70, "Fisica": 68, "Arte": 93},
    "Sofia": {"Matematica": 88, "Letteratura": 94, "Chimica": 76, "Inglese": 81},
    "Andrea": {"Matematica": 74, "Storia": 65, "Fisica": 62, "Inglese": 70}
}


def filtra_strudenti_materie(lista_studenti, media_minima = 80, voto_minimo = 85):
    risultato = {}
    
    for studente, materie in lista_studenti.items():
        voti = list(materie.values())
        media_sudente = sum(voti) / len(voti)
        
        if media_sudente > media_minima:
            materie_filtrate = {}
            
            for materia, voto in materie.items():
                if voto >= voto_minimo:
                    materie_filtrate[materia] = voto
                    
                    
            if materie_filtrate:
                risultato[studente] = materie_filtrate
    return risultato


#print(filtra_strudenti_materie(voti_studenti))
















libri = [
    {
        "titolo": "Il nome della rosa",
        "autore": "Umberto Eco",
        "anno": 1980,
        "genere": "Storico",
        "pagine": 536,
        "disponibile": True
    },
    {
        "titolo": "1984",
        "autore": "George Orwell",
        "anno": 1949,
        "genere": "Distopico",
        "pagine": 328,
        "disponibile": False
    },
    {
        "titolo": "Il Signore degli Anelli",
        "autore": "J.R.R. Tolkien",
        "anno": 1954,
        "genere": "Fantasy",
        "pagine": 1216,
        "disponibile": True
    },
    {
        "titolo": "Harry Potter e la pietra filosofale",
        "autore": "J.K. Rowling",
        "anno": 1997,
        "genere": "Fantasy",
        "pagine": 332,
        "disponibile": True
    },
    {
        "titolo": "Orgoglio e pregiudizio",
        "autore": "Jane Austen",
        "anno": 1813,
        "genere": "Romanzo",
        "pagine": 432,
        "disponibile": False
    },
    {
        "titolo": "La Divina Commedia",
        "autore": "Dante Alighieri",
        "anno": 1320,
        "genere": "Poema",
        "pagine": 798,
        "disponibile": True
    },
    {
        "titolo": "Il piccolo principe",
        "autore": "Antoine de Saint-Exupéry",
        "anno": 1943,
        "genere": "Fiaba",
        "pagine": 96,
        "disponibile": True
    }
]



#Libri che sono di genere "Fantasy"
#Libri che sono stati pubblicati dopo il 1950
#Libri che sono attualmente disponibili per il prestito (disponibile = True)


def filter_books(book):
    libri_filtrati = []
    
    for libri in book:
        if libri["genere"] == "Fantasy" and libri["anno"] > 1950 and libri["disponibile"] == True:
            libri_filtrati.append(libri)
            
    return libri_filtrati


#print(filter_books(libri))