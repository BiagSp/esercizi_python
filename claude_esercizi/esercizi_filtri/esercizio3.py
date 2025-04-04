"""
Implementare filtri con funzioni lambda complesse
Filtrare strutture di dati annidate (liste di dizionari che contengono altre liste)
Creare filtri personalizzati con decoratori o classi

"""

film = [
    {"titolo": "Inception", "regista": "Christopher Nolan", "anno": 2010, "durata": 148, "genere": ["Fantascienza", "Azione", "Thriller"], "voto_critica": 8.8, "voto_pubblico": 8.9, "incasso": 836800000, "oscar": 4},
    {"titolo": "The Shawshank Redemption", "regista": "Frank Darabont", "anno": 1994, "durata": 142, "genere": ["Drammatico"], "voto_critica": 9.3, "voto_pubblico": 9.3, "incasso": 58300000, "oscar": 0},
    {"titolo": "Pulp Fiction", "regista": "Quentin Tarantino", "anno": 1994, "durata": 154, "genere": ["Crimine", "Drammatico"], "voto_critica": 8.9, "voto_pubblico": 8.9, "incasso": 213900000, "oscar": 1},
    {"titolo": "Il Padrino", "regista": "Francis Ford Coppola", "anno": 1972, "durata": 175, "genere": ["Crimine", "Drammatico"], "voto_critica": 9.2, "voto_pubblico": 9.2, "incasso": 245100000, "oscar": 3},
    {"titolo": "La La Land", "regista": "Damien Chazelle", "anno": 2016, "durata": 128, "genere": ["Musicale", "Drammatico", "Romantico"], "voto_critica": 8.0, "voto_pubblico": 8.0, "incasso": 448900000, "oscar": 6},
    {"titolo": "Parasite", "regista": "Bong Joon-ho", "anno": 2019, "durata": 132, "genere": ["Drammatico", "Thriller"], "voto_critica": 8.6, "voto_pubblico": 8.5, "incasso": 258400000, "oscar": 4},
    {"titolo": "Interstellar", "regista": "Christopher Nolan", "anno": 2014, "durata": 169, "genere": ["Fantascienza", "Drammatico", "Avventura"], "voto_critica": 8.6, "voto_pubblico": 8.7, "incasso": 677500000, "oscar": 1},
    {"titolo": "The Dark Knight", "regista": "Christopher Nolan", "anno": 2008, "durata": 152, "genere": ["Azione", "Crimine", "Drammatico"], "voto_critica": 9.0, "voto_pubblico": 9.0, "incasso": 1004600000, "oscar": 2},
    {"titolo": "Forrest Gump", "regista": "Robert Zemeckis", "anno": 1994, "durata": 142, "genere": ["Drammatico", "Romantico", "Commedia"], "voto_critica": 8.8, "voto_pubblico": 8.8, "incasso": 678200000, "oscar": 6},
    {"titolo": "Avatar", "regista": "James Cameron", "anno": 2009, "durata": 162, "genere": ["Fantascienza", "Avventura", "Azione"], "voto_critica": 7.8, "voto_pubblico": 7.9, "incasso": 2847300000, "oscar": 3}
]


"""
Obiettivo: Vogliamo implementare filtri lambda complessi per trovare film che soddisfano combinazioni specifiche di criteri.
Ecco alcuni esempi di filtri avanzati che potremmo creare:

Film che sono "capolavori commerciali": alta valutazione sia della critica che del pubblico (>8.5), con un incasso elevato (>500 milioni)
Film "da Oscar sottovalutati": film che hanno vinto molti Oscar (>2) ma hanno avuto un incasso relativamente basso (<300 milioni)
Film del "triumvirato Nolan": film diretti da Christopher Nolan, con durata superiore a 150 minuti e che includono sia "Fantascienza" 
che "Drammatico" tra i generi
Film "equilibrati": film con la minima differenza tra voto della critica e voto del pubblico, ma entrambi superiori a 8.0
"""

def film_equilibrati(films):
    return list(filter(lambda f: (f["voto_critica"] > 8 and f["voto_pubblico"] > 8 and abs(f["voto_critica"] - f["voto_pubblico"]) < 0.1), films ))

print("Film con differeza tra voti", film_equilibrati(film))



def filter_films(films):
    return list(filter(lambda f: f["voto_critica"] > 8.5 and f["voto_pubblico"] > 8.5 and f["incasso"] > 500000000, films))


def film_oscar(films):
    return list(filter(lambda f: f["oscar"] > 2 and f["incasso"] <300000000, films ))
    
    
def triumvirato_nolan(films):
    return list(filter(lambda f: (f["regista"] == "Christopher Nolan" and 
                                 f["durata"] > 150 and 
                                 all(genere in f["genere"] for genere in ["Fantascienza", "Drammatico"])),
                      films))
    
    
    
    
print(filter_films(film))
print(film_oscar(film))
print(triumvirato_nolan(film))