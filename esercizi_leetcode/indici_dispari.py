"""
Trovare gli elementi con indice dispari

"""



def ele_disp(d):
    elementi_dispari = []
    
    for i in range(1,len(d),2):
        if i % 2 != 0:
            elementi_dispari.append(d[i])
            
    return elementi_dispari


print(ele_disp([1,2,3,4]))