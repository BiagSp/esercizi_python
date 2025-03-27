"""
Scrivi un programma che legge un file di testo, conta quante volte appare ogni parola e salva i risultati in un nuovo file.

"""



try:
    with open('C:/Users/spabi/Desktop/cazzeggioPY/claude_esercizi/text_file.txt', 'r') as file_input:
        contenuto = file_input.read()

        import string

        for carattere in string.punctuation:
            contenuto = contenuto.replace(carattere, " ")

        contenuto = contenuto.lower()
        parole = contenuto.split()

        conteggio_parole = {}

        for parola in parole:
            if parola in conteggio_parole:
                conteggio_parole[parola] += 1
            else:
                conteggio_parole[parola] = 1

        with open('C:/Users/spabi/Desktop/cazzeggioPY/claude_esercizi/risultati_conteggio.txt', 'w') as file_output:
            for parola, conteggio in conteggio_parole.items():
                file_output.write(f"{parola}: {conteggio}\n")
            
        print("conteggio completato con successo!")



except FileNotFoundError:
    print("Il file non è stato trovato. Verificare percorso file")
except Exception as e:
    print(f"Si è verificato un errore: {str(e)}")