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


# Definizione della classe Prodotto
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

# Classe Prodotto: rappresenta un prodotto con nome, prezzo e quantità (scorta).
class Prodotto:
    def __init__(self, nome: str, prezzo: float, scorta: int):
        # Inizializza l'attributo 'nome' con il valore passato.
        self.nome = nome  
        # Inizializza l'attributo 'prezzo' con il valore passato.
        self.prezzo = prezzo  
        # Inizializza l'attributo 'scorta' con il valore passato.
        self.scorta = scorta  
    
    # Metodo speciale che restituisce una stringa rappresentativa dell'oggetto.
    def __str__(self):
        return f"Prodotto: {self.nome}, Prezzo: {self.prezzo} Scorta: {self.scorta}"


# Classe GestoreMagazzino: gestisce il magazzino dei prodotti.
class GestoreMagazzino:
    def __init__(self, costo_magazinaggio):
        # Inizializza un dizionario vuoto per contenere i prodotti.
        # Le chiavi saranno i nomi dei prodotti e i valori saranno gli oggetti Prodotto.
        self.prodotti = {}  
        # Salva il costo per unità prodotto per il magazzinaggio.
        self.costo_magazinaggio = costo_magazinaggio  

    # Metodo per aggiungere uno o più prodotti al magazzino.
    # L'uso di *prodotti permette di passare un numero variabile di argomenti.
    def aggiungi_prodotto(self, *prodotti):
        # Itera su ciascun prodotto passato come argomento.
        for prodotto in prodotti:
            # Se il prodotto è già presente (identificato dal nome) nel dizionario:
            if prodotto.nome in self.prodotti:
                # Stampa un messaggio informativo.
                print(f"il prodotto: {prodotto.nome} è già presente in magazzino")
                # Aggiorna la scorta sommando quella esistente a quella del nuovo prodotto.
                self.prodotti[prodotto.nome].scorta += prodotto.scorta
            else:
                # Se il prodotto non è presente, lo aggiunge al dizionario.
                self.prodotti[prodotto.nome] = prodotto

    # Metodo per rimuovere un prodotto dal magazzino in base al suo nome.
    def rimuovi_prodotti(self, nome_prodotto):
        # Verifica se il prodotto esiste nel dizionario.
        if nome_prodotto in self.prodotti:
            # Se esiste, lo elimina dal dizionario.
            del self.prodotti[nome_prodotto]
            # Stampa un messaggio di conferma.
            print(f"Prodotto: {nome_prodotto} rimosso dal magazzino")
        else:
            # Se non esiste, informa che il prodotto non è presente.
            print(f"il prodotto {nome_prodotto} non presente in magazzino")

    # Metodo per calcolare il costo totale di magazzinaggio per tutti i prodotti presenti.
    def calcolo_costi_magazinaggio(self):
        costo_totale = 0  # Inizializza il costo totale a 0.
        # Per ogni prodotto presente nel dizionario:
        for prodotto in self.prodotti.values():
            # Calcola il costo per il prodotto moltiplicando la quantità (scorta)
            # per il costo unitario di magazzinaggio.
            # NOTA: Attenzione, l'uso di "=" sovrascrive il valore ad ogni iterazione.
            # Se si vuole sommare il costo di tutti i prodotti, occorrerebbe usare "+=".
            costo_totale = prodotto.scorta * self.costo_magazinaggio
        # Restituisce il costo totale calcolato.
        return costo_totale


# Blocco principale: viene eseguito solo se il file è eseguito direttamente.
if __name__ == "__main__":
    # Crea un'istanza di GestoreMagazzino con un costo di magazzinaggio pari a 0.2.
    magazzino = GestoreMagazzino(costo_magazinaggio=0.2)

    # Crea un oggetto Prodotto per "mela" con prezzo 0.3 e scorta 199.
    mela = Prodotto("mela", 0.3, 199)
    # Crea un oggetto Prodotto per "pera" con prezzo 0.5 e scorta 60.
    pera = Prodotto("pera", 0.5, 60)

    # Aggiunge entrambi i prodotti al magazzino.
    magazzino.aggiungi_prodotto(mela, pera)

    # Stampa il costo totale di magazzinaggio calcolato.
    print(f"Costo magazinaggio totale {magazzino.calcolo_costi_magazinaggio()}")

    # Rimuove il prodotto "pera" dal magazzino.
    magazzino.rimuovi_prodotti("pera")
    # Stampa il costo di magazzinaggio dopo la rimozione del prodotto.
    print(f"costo magazinaggio dopo la rimozione del prodotto, costo: {magazzino.calcolo_costi_magazinaggio()}")
