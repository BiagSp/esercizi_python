"""
Creare una funzione che genera i primi numeri n della sequenza di fibonacci

sequenza fibonacci somma del numero n con il numero precedente
"""


def fibonacci(n):
    sequenze = [0,1]
    for i in range(2,n):
        next_num = sequenze[i-1] + sequenze[i-2]
        sequenze.append(next_num)
        
    return sequenze


print(fibonacci(12))