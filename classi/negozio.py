"""
Esercizio: Sistema di Gestione Prodotti
Crea un sistema di gestione per un negozio con le seguenti caratteristiche:

Crea una classe Prodotto con:

Attributi: nome, prezzo, quantità in magazzino
Metodi per:

Visualizzare le informazioni del prodotto
Aggiornare il prezzo
Aggiornare la quantità (incrementare/decrementare)




Crea una classe Carrello che:

Permetta di aggiungere prodotti e specificare la quantità
Permetta di rimuovere prodotti
Calcoli il totale della spesa
Mostri il contenuto del carrello


Crea una classe Negozio che:

Gestisca un catalogo di prodotti
Permetta di cercare prodotti per nome
Permetta di effettuare acquisti (aggiornando le quantità in magazzino)

"""


class Prodotto:
    def __init__(self, nome, prezzo, quantità):
        self.nome = nome
        self.prezzo = prezzo
        self.quantità = quantità

    def __str__(self):
        return f"Nome prodotto: {self.nome} Prezzo: {self.prezzo} Quantità {self.quantità}"

    def aggiornare_prezzo(self, nuovo_prezzo):
        self.prezzo = nuovo_prezzo
        return f"Prezzo del prodotto: {self.nome} è di: {self.prezzo}"
    
    def aggiornare_quantità(self, variazione):
        if self.quantità + variazione >= 0:
            self.quantità += variazione
            return f"Quantità del prodotto: {self.nome} aggiornata a {self.quantità}"
        else:
            return f"Errore la quantità richiesta {(-variazione)} è maggiore da quella disponibile {self.quantità}"



class Carrello:
    def __init__(self):
        self.prodotti = {}
    

    def aggiungi_prodotto(self, prodotto, quantità):
        if prodotto in self.prodotti:
            self.prodotti[prodotto] += quantità
        else:
            self.prodotti[prodotto] = quantità
        return f"{quantità} {prodotto.nome} aggiunto al carrello"
    
    def rimuovi_prodotto(self, prodotto, quantità):
        if prodotto in self.prodotti:
            if quantità >= self.prodotti[prodotto]:
                del self.prodotti[prodotto]
                print(f"Il prodotto {prodotto.nome} è stato rimosso dal carrello")
            else:
                self.prodotti[prodotto] -= quantità
        else:
            print(f"Il prodotto {prodotto.nome} non è presente nel carrello")


    def calcolo_spesa(self):
        costo_totale = 0

        for prodotto, quantità in self.prodotti.items():
            costo_totale += quantità * prodotto.prezzo
        print(f"Il costo totale della spesa è di: {costo_totale}")
 

    def mostra_carrello(self):
        if not self.prodotti:
            print("Il carrello è vuoto")
        else:

            for prodotto, quantity in self.prodotti.items():
                print(f"i prodotti nel carrello sono i seguenti: \n Prodotto: {prodotto.nome} Quantità: {quantity}")
        
        


class Negozio: 
    def __init__(self):
        self.catalogo = {}

    def aggiungi_prodotto(self, *prodotti):
        for prodotto in prodotti:
            self.catalogo[prodotto.nome.lower()] = prodotto

    def cerca_prodotto(self, nome):
        key = nome.lower()
        if key in self.catalogo:
            return self.catalogo[key]
        else:
            print(f"Prodotto {nome} non trovato in catalogo")
            return None

    def acquisti(self, nome, quantità):
        prodotto = self.cerca_prodotto(nome)

        if prodotto:
            if prodotto.quantità >= quantità:
                prodotto.aggiornare_quantità(-quantità)
                print(f"Aquisto effettuato, Prodotto: {prodotto.nome} Quantità: {quantità}")
            else:
                print(f"quantità insufficiente per acquistare, quantità disponibile: {prodotto.quantità}")





def main():
    p1 = Prodotto("Mela",0.2,100)
    p2 = Prodotto("Pera", 0.5,50)

    print(p1,p2)

    print("\n ===Test Classe Prodotto===")
    print(p1.aggiornare_prezzo(0.7))
    print(p1.aggiornare_quantità(-20))
    print(p1)

    print("\n ===Test Classe Carrello===")
    carrello = Carrello()
    print(carrello.aggiungi_prodotto(p1,5))
    print(carrello.aggiungi_prodotto(p2,8))

    carrello.mostra_carrello()

    carrello.calcolo_spesa()

    carrello.rimuovi_prodotto(p1,4)
    carrello.mostra_carrello()
    carrello.calcolo_spesa()

    print("\n===Test Classe Negozio===")
    negozio = Negozio()

    negozio.aggiungi_prodotto(p1, p2)


    print("Acquisti")

    negozio.acquisti("Mela", 5)
    negozio.acquisti("Pera",78)

    print(p1,p2)

if __name__ == "__main__":
    main()