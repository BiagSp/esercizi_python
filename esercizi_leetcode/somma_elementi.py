"""
sommare tutti gli elementi di una lista

"""


def somma(a):
    sommati = 0
    for num in a:
        sommati += num
    return sommati


print(somma([1,2,3,4,5]))