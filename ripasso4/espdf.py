# Inizializzazione di un sistema per memorizzare informazioni dei studenti

# 1. Crea una tupla per rappresentare uno studente con: nome, età, voto 
# 2. Crea una tupla contenente 3 studenti diversi 
studenti = (("Mario", 19, 27), ("Luca", 18, 29), ("Giulia", 19, 30))

print("Sistema studenti:", studenti)


# 3. Accedi alle informazioni del secondo studente 
print("Secondo studente:", studenti[1])


# 4. Trova un modo per modificare alcuni studenti che potrebbero avere voti in sospeso
print("=== MODIFICA VOTI IN SOSPESO ===")


#Dato che la tupla puo' contenere anche delle liste lo studente con il voto in sospeso lo mettiamo dentro una lista, in modo tale da poterlo modificare
studenti = (["Mario", 19, 27], ("Luca", 18, 29), ("Giulia", 19, 30))

#In questo modo ora possiamo accedere allo studente e modificare il voto
    #Osserviamo che lo studente [0] risulta essere una lista
print(type(studenti[0]))

studenti[0][2]= 30

print(studenti[0])


