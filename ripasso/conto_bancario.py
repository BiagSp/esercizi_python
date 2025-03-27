"""
Crea una classe ContoBancario con i seguenti metodi:

deposito(somma): aggiunge una somma al conto.
prelievo(somma): sottrae una somma dal conto (se sufficiente).
saldo(): stampa il saldo attuale.

"""

class ContoBancario:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def __deposito(self, somma: float):
        self.saldo += somma
        print(f"Somma depositata {somma}, saldo attuale: {self.saldo}")

    def deposito(self, somma):
        return self.__deposito(somma)
    
    def __prelievo(self, importo):
        self.saldo -= importo
        print(f"Somma prelevata: {importo}, saldo attuale: {self.saldo}")

    def prelievo(self, importo):
        if importo > self.saldo:
            print("Saldo insufficiente")
        else:
            self.saldo -= importo
            print(f"Somma prelevata: {importo}, saldo attuale: {self.saldo}")
    
    def __stampa_saldo(self):
        print(f"Saldo corrennte: {self.saldo}")

    def stamapa_saldo(self):
        return self.__stampa_saldo()

    

def main():
    conto1 = ContoBancario(500)
    conto1.deposito(300)
    conto1.prelievo(200)
    conto1.stamapa_saldo()


if __name__ == "__main__":
    main()