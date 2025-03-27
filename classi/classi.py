"""
Obiettivo: Creare una classe base e utilizzarne metodi e attributi.

Istruzioni:

Crea una classe Automobile con gli attributi marca, modello e anno.
Implementa un metodo info() che stampi le informazioni complete dell'automobile.
Crea un'istanza della classe e chiama il metodo info().
Suggerimento: Usa il costruttore __init__ per inizializzare gli attributi.
"""

class Automobile:
    #Aggiunto il parametro "self" per riferirsi all'istanza corrente
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno    
    def info(self):
         # Il metodo info() viene definito all'interno della classe e utilizza "self" per accedere agli attributi
        print(f"Marca: {self.marca}\n Modello: {self.modello}\n anno: {self.anno}")

# Creiamo un'istanza della classe Automobile
auto = Automobile("tesla", "x", 2020)

auto.info()
# Chiamiamo il metodo info() sull'istanza auto






"""
Obiettivo: Comprendere come nascondere i dati e gestire l'accesso tramite metodi.

Istruzioni:

Crea una classe ContoBancario con un attributo privato __saldo.
Implementa metodi:
deposita(importo): aggiunge l'importo al saldo.
preleva(importo): sottrae l'importo dal saldo solo se sufficiente.
mostra_saldo(): restituisce il saldo attuale.
Prova a depositare e prelevare somme e mostra il saldo finale.
Suggerimento: Utilizza il prefisso __ per rendere l'attributo saldo privato.

"""

class ContoBancario:
    def __init__(self, saldo):
        self.__saldo = saldo

    def deposita(self, importo):
        self.__saldo += importo
    
    def preleva(self, importo):
        if self.__saldo >= importo:
            self.__saldo -= importo
        else: 
            print("Saldo insufficiente!")
    
    def mostra_saldo(self):
        return self.__saldo
    

conto = ContoBancario(1000)
operazione = input("digita una tra le seguenti opeazioni che vuoi effettuare: Deposita(dp), Preleva(pl), Saldo(sd)\n")

if operazione.lower() == "dp":
    importo = float(input("Quanto desideri depositare?\n"))
    conto.deposita(importo)
    print(f"Saldo aggiornato: {conto.mostra_saldo()}")

elif operazione.lower() == "pl":
    prelievo =  float(input("Quanto desideri prelevare?\n"))
    conto.preleva(prelievo)
    print(f"Saldo aggiornato: {conto.mostra_saldo()}")
    print(f"Saldo aggiornato: {conto.mostra_saldo() - prelievo}")

elif operazione.lower() == "sd":
    print(f"Il tuo saldo attuale è: {conto.mostra_saldo()}")
else:
    print(f"Operazione non valida!")

