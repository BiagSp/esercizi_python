"""
Esercizio 5
Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
La classe dovrà avere i seguenti metodi:
Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.

"""

class Prodotto:
    def __init__(self, nome, prezzo, scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta

    def __str__(self):
        return f"Prodott: {self.nome}, Prezzo: {self.prezzo}, Scorta: {self.scorta}"
    


class GestoreMagazzino:
    def __init__(self, costo_magazzinaggio):
        self.prodotti = {}
        self.costo_magazzinaggio = costo_magazzinaggio

    def aggiungi_prodotto(self, prodotto):
        if prodotto.nome in self.prodotti:
            print(f"Il prodotto: {prodotto.nome} è già presente in magazzino, aggiornamento scorta")
            self.prodotti[prodotto.nome].scorta += prodotto.scorta
        else:
            self.prodotti[prodotto.nome] = prodotto

    def rimuovi_prodotti(self, nome_prodotto):
        if nome_prodotto in self.prodotti:
            del self.prodotti[nome_prodotto]
            print(f"Prodotto {nome_prodotto} rimosso dal magazzino")
        else:
            print(f"Il prodotto {nome_prodotto} non è presente nel magazzino")


    def calcolo_costi_magazinaggio(self):
        costo_totale = 0
        for prodotto in self.prodotti.values():
            costo_totale += prodotto.scorta * self.costo_magazzinaggio
        return costo_totale
    


if __name__ == "__main__":
    magazzino = GestoreMagazzino(costo_magazzinaggio = 0.2)

    mela = Prodotto("Mela", 0.3, 100)
    banana = Prodotto("Banana", 0.7, 45)

    magazzino.aggiungi_prodotto(mela)
    magazzino.aggiungi_prodotto(banana)

    print("Costo di magazzinaggio totale", magazzino.calcolo_costi_magazinaggio())


    magazzino.rimuovi_prodotti("Mela")
    print("Costo magazinaggio dopo la rimozione del prodotto:", magazzino.calcolo_costi_magazinaggio())
