"""
Sistema di Dipendenti

Progetta un sistema con una classe base Dipendente e classi derivate specializzate.

"""

from datetime import date, datetime

class Dipendente: 
    def __init__(self, stipendio:float, nome:str, cognome:str, ID:int, data_assunzione:date):
        self.stipendio = stipendio
        self.nome = nome
        self.cognome = cognome
        self.ID = ID

        if isinstance(data_assunzione, date):
            self.data_assunzione = data_assunzione
        elif isinstance(data_assunzione, str):
            self.data_assunzione = datetime.strptime(data_assunzione, "%Y-%m-%d").date()
        else:
            raise TypeError("data_assunzione deve essere un oggetto o una stringa nel formato YYYY-MM-DD ")
        

    def calcola_stipediO(self, ore_lavorate:float, ore_mensili_stadard:float = 160) -> float:

        if ore_lavorate <= ore_mensili_stadard:
            fattore_proporzionale = ore_lavorate / ore_mensili_stadard
            return self.stipendio * fattore_proporzionale
        else:
            tariffa_oraria = self.stipendio / ore_mensili_stadard
            ore_straordinario = ore_lavorate - ore_mensili_stadard

            compenso_straordinario = ore_straordinario * tariffa_oraria * 1.3

            return self.stipendio + compenso_straordinario


class Impiegato(Dipendente):
    def __init__(self, stipendio:float, nome:str, cognome:str, ID:int, data_assunzione:date, dipartimento:str):
        super().__init__(stipendio, nome, cognome, ID, data_assunzione)
        self.dipartimento = dipartimento