"""
Strutturare la classe cinema

"""

class Cinema:
    def __init__(self, nome, indirizzo, sale_disponibili, film_proiettato, films:dict,):
        self.nome = nome
        self.indirizzo = indirizzo
        self.sale_disponibili = sale_disponibili
        self.film_proiettato = film_proiettato
        self.films = films
        
    
    
class Film:
    def __init__(self, titolo, durata, genere, regista, anno_uscita, stato, orari_proiezione=None):
        self.titolo = titolo
        self.durata = durata
        self.genere = genere
        self.regista = regista
        self.anno_uscita = anno_uscita
        self.stato = stato  # "in arrivo", "in proiezione", "prossima proiezione"
        self.orari_proiezione = orari_proiezione if orari_proiezione else []
        
    def __str__(self):
        """Rappresentazione in stringa del film"""
        return f"{self.titolo} ({self.anno_uscita}) - {self.durata} min - {self.stato}"
        
    def aggiungi_orario(self, orario):
        """Aggiunge un orario di proiezione per questo film"""
        self.orari_proiezione.append(orario)
        
    def cambia_stato(self, nuovo_stato):
        """Cambia lo stato del film"""
        stati_validi = ["in arrivo", "in proiezione", "prossima proiezione"]
        if nuovo_stato in stati_validi:
            self.stato = nuovo_stato
        else:
            print(f"Stato non valido. Gli stati possibili sono: {', '.join(stati_validi)}")