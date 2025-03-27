"""
Descrizione: Crea un dizionario con le conversioni da euro ad altre valute (es. {"USD": 1.1, "GBP": 0.85, "JPY": 130}).
Chiedi all'utente quanti euro vuole convertire e in quale valuta.
Stampa il valore convertito.

"""
valuta = {"USD": 1.1, "GBP": 0.85, "JPY":130}

conversion = input("Digita in quale moneta vuoi convertire tra le seguenti USD\n GBP\n JPY\n")
euro = input("Quanti euro vuoi convertire?\n")
converted_value = float(euro)

if conversion.lower() == "usd":
    con = converted_value * valuta["USD"]
    print(con)
elif conversion.lower() == "gbp":
    con = converted_value * valuta["GBP"]
    print(con)
elif conversion.lower() == "jpy":
    con = converted_value * valuta["JPY"]
    print(con)
else:
    print("Valuta non valida")

