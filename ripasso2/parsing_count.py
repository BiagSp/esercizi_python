"""
Obiettivo: Creare un dizionario che contenga ogni parola in un testo e la sua frequenza.
Guida:

Suddividi il testo in parole
Crea un dizionario vuoto
Per ogni parola:

Se la parola è già nel dizionario, incrementa il contatore
Altrimenti, aggiungi la parola con valore 1


Alla fine, visualizza le parole ordinate per frequenza

Best practice:

Usa collections.Counter per semplificare il codice
Normalizza le parole (minuscole)
Rimuovi la punteggiatura per ottenere risultati più accurati

"""
parole = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia"
punteggiatura = ",.!?;:\"'()[]{}!|-"

words = parole.split()

parole_count = {}

for par in words:
    parola = ""
    for carattere in par:
        if carattere not in punteggiatura:
            parola += carattere
    parole_count.append(parola)
    
print(parole_count)
