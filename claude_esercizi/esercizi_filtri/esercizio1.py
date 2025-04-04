"""
Filtrare una lista di numeri per ottenere solo i numeri pari
Filtrare una lista di stringhe per ottenere solo quelle che iniziano con una certa lettera
Filtrare un dizionario per mantenere solo le coppie chiave-valore dove il valore soddisfa una certa condizione

"""

numeri = [1,2,3,4,5,6,7,89,4,5,6723,756,232,12,457,98]


def filter_even_num(num):
    even_num = []
    
    for n in num: 
        if n%2 == 0 and n not in even_num:
            even_num.append(n)
    return even_num
        
        
print(filter_even_num(numeri))

lista_string = ["asibfsoidfb", "ASSDkwibf", "jhHfueb2","Kfhiebf", "Filtrare una lista di stringhe"]

def filter_string(stri):
    string_filtered = []
    
    for s in stri:
        if s[0].isupper() and s not in string_filtered:
            string_filtered.append(s)
    return string_filtered


print(filter_string(lista_string))



studenti = {
    "Marco": 85,
    "Giulia": 92,
    "Roberto": 65,
    "Francesca": 78,
    "Luca": 90,
    "Sofia": 73,
    "Paolo": 68,
    "Valentina": 95
}


#filtrare il dizionario per mantenere solo gli studenti che hanno ottenuto un voto superiore o uguale a 80.

def promossi(stud):
    promoted = {}
    for s,v in stud.items():
        if v > 80:
            if s not in promoted:
                promoted[s] = v
            
    return promoted


print(promossi(studenti))