"""from sympy import symbols, sympify


equation = input("Inserisci l'equazione che desideri:\n)")
x = float(input("Inserisci il valore di x:\n"))

funzione = sympify(equation)

print(f"Risultato: {funzione.subs('x', x)}")"""

def funzione(x):
    return x**2 + 3*x + 2  # Definizione della funzione

def derivata_numerica(f, x, delta=1e-4):
    return (f(x + delta) - f(x)) / delta  # Formula per la derivata

# Input dell'utente
valore_x = float(input("Inserisci il valore di x per calcolare la derivata: "))
risultato = derivata_numerica(funzione, valore_x)
print(f"Derivata numerica in x = {valore_x}: {risultato}")
