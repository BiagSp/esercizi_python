"""
Scrivi un programma che stampi i numeri da 1 a 50. Se un numero è multiplo di 3 stampa "Fizz", se è multiplo di 5 stampa "Buzz",
 e se è multiplo di entrambi stampa "FizzBuzz".

"""

for n in range(1,50 +1):
    if n % 15 == 0:
        print("fizbuzz",n)
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")