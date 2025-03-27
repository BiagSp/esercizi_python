# Questo programma implementa un sistema di rubrica telefonica che:
# 1. Legge contatti da un file di testo
# 2. Elimina eventuali duplicati (basati sul numero di telefono)
# 3. Consente di aggiungere e rimuovere contatti
# 4. Visualizza tutti i contatti presenti nella rubrica

class Contatto:
    """
    Classe che rappresenta un singolo contatto nella rubrica.
    Ogni contatto è caratterizzato da nome, cognome e numero di telefono.
    """
    def __init__(self, nome, cognome, numero:int):
        # Inizializzazione degli attributi del contatto
        self.nome = nome      # Nome del contatto
        self.cognome = cognome # Cognome del contatto 
        self.numero = numero   # Numero di telefono (deve essere un intero)
        

class Rubrica:
    """
    Classe che gestisce l'intera rubrica telefonica.
    Fornisce metodi per leggere, aggiungere, rimuovere e visualizzare contatti.
    """
    def __init__(self, file_path):
        # Inizializzazione della rubrica
        self.file_path = file_path  # Percorso del file da cui leggere i contatti
        self.contatti = []          # Lista vuota che conterrà tutti i contatti
        
    
    def leggi_contatto(self):
        """
        Legge i contatti dal file specificato e li aggiunge alla lista contatti.
        Ogni riga del file deve essere nel formato: nome,cognome,numero
        Gestisce anche possibili errori di lettura o di formato.
        """
        try:
            # Apre il file in modalità lettura
            with open(self.file_path, "r") as file:    
                count = 0            # Contatore per tenere traccia del numero di contatti letti
                for cont in file:    # Iterazione su ogni riga del file
                    line = cont.strip().split(',')  # Rimuove spazi extra e divide la riga usando la virgola
                    if len(line) >= 3:              # Verifica che ci siano almeno tre elementi
                        nome = line[0]              # Primo elemento: nome
                        cognome = line[1]           # Secondo elemento: cognome
                        numero = int(line[2])       # Terzo elemento: numero (convertito in intero)
                        contatto = (nome, cognome, numero)  # Crea una tupla con i dati del contatto
                        self.contatti.append(contatto)      # Aggiunge la tupla alla lista contatti
                        count += 1                         # Incrementa il contatore
            print(f"Letti {count} contatti dal file {self.file_path}")
            return self.contatti
        except FileNotFoundError:
            # Gestisce l'errore se il file non esiste
            print(f"File {self.file_path} non esiste")
            return []
            
        except ValueError as e:
            # Gestisce l'errore se ci sono problemi nella conversione dei dati
            print(f"Errore nella conversione dei dati {e}")
            return []
        
    def get_contatto(self):
        """
        Rimuove i contatti duplicati dalla lista e converte le tuple in dizionari.
        Un contatto è considerato duplicato se ha lo stesso numero di telefono di un altro.
        Restituisce una lista di dizionari che rappresentano i contatti unici.
        """
        duplicati = 0                # Contatore per i contatti duplicati
        contatti_unici = {}          # Dizionario per memorizzare i contatti unici (chiave: numero)
        
        # Iterazione su tutti i contatti nella lista
        for contatto in self.contatti:
            numero = contatto[2]     # Estrae il numero di telefono (terzo elemento della tupla)
            
            # Se il numero non è già presente nel dizionario, lo aggiunge
            if numero not in contatti_unici:
                contatti_unici[numero] = contatto
            else:
                # Se il numero è già presente, incrementa il contatore dei duplicati
                duplicati += 1
        
        # Crea una lista di dizionari per i contatti unici
        risultato = []
        for contatto in contatti_unici.values():
            # Converte la tupla in un dizionario per una visualizzazione più chiara
            contact_dic = {
                "Nome": contatto[0],
                "Cognome": contatto[1],
                "Numero": contatto[2]
            }
            
            risultato.append(contact_dic)  # Aggiunge il dizionario alla lista risultato
            
        # Stampa il numero di duplicati trovati (se presenti)
        if duplicati > 0:
            print(f"Trovati {duplicati} contatti duplicati")
            
        self.risultato = risultato  # Memorizza la lista di contatti unici come attributo
        return risultato
        
 
    def stampa_rubrica(self):
        """
        Stampa tutti i contatti presenti nella rubrica in un formato leggibile.
        Se la lista dei contatti unici non esiste, la genera prima di stampare.
        """
        # Verifica se la lista dei contatti unici esiste già; se non esiste, la crea
        if not hasattr(self, "risultato") or self.risultato is None:
            self.get_contatto()
        
        # Stampa il numero totale di contatti
        print(f"Numero totale di contatti: {len(self.risultato)}")
        print("=" * 40)  # Linea separatrice per migliorare la leggibilità
        
        # Stampa i dettagli di ogni contatto
        for el in self.risultato:
            print(f"Nome: {el['Nome']}")
            print(f"Cognome: {el['Cognome']}")
            print(f"Numero: {el['Numero']}")
            print("-" * 30)  # Separatore tra contatti
            
            
    def aggiungi_contatto(self, contatto):
        """
        Aggiunge un nuovo contatto alla rubrica, verificando che non sia già presente.
        Il contatto viene considerato duplicato se ha lo stesso numero di un contatto esistente.
        
        Args:
            contatto: Un'istanza della classe Contatto da aggiungere
        
        Returns:
            bool: True se il contatto è stato aggiunto, False altrimenti
        """
        # Verifica che il parametro sia un'istanza della classe Contatto
        if not isinstance(contatto, Contatto):
            raise TypeError("Il parametro deve essere un'istanza della classe Contatto")        

        # Verifica se esiste già un contatto con lo stesso numero di telefono
        for contatto_esistente in self.contatti:
            if contatto_esistente[2] == contatto.numero:
                print(f"Errore il contatto con numero: {contatto.numero} è già presente")
                return False
            
        # Crea una tupla con i dati del nuovo contatto
        nuovo_contatto = (contatto.nome, contatto.cognome, contatto.numero)
        self.contatti.append(nuovo_contatto)  # Aggiunge la tupla alla lista contatti
        
        # Gestione della coerenza dati: se esiste già una lista di risultati,
        # la imposta a None per forzare la rigenerazione alla prossima chiamata
        if hasattr(self, "risultato"):
            self.risultato = None
            
        print(f"Contatto {contatto.nome} è stato aggiunto con successo")
        return True
        
        
    def rimuovi_contatto(self, contatto):
        """
        Rimuove un contatto dalla rubrica in base al numero di telefono.
        
        Args:
            contatto: Un'istanza della classe Contatto da rimuovere
            
        Returns:
            bool: True se il contatto è stato rimosso, False se non è stato trovato
        """
        # Verifica che il parametro sia un'istanza della classe Contatto
        if not isinstance(contatto, Contatto):
            raise TypeError("Errore  parametro deve essere un'istanza della classe Contatto")
        
        # Estrae il numero di telefono dal contatto
        numero = contatto.numero
        trovato = False
        
        # Itera attraverso la lista dei contatti per trovare quello da rimuovere
        for i in range(len(self.contatti)):
            if self.contatti[i][2] == numero:  # Confronta i numeri di telefono
                del self.contatti[i]  # Rimuove il contatto dalla lista
                trovato = True
                break  # Esce dal ciclo dopo aver rimosso il contatto
        
        # Stampa un messaggio appropriato in base al risultato
        if trovato:
            print(f"[ok] Contatto con numero {numero} rimosso con successo")
        else:
            print(f"[ok] Attenzione: nessun contatto trovato con il numero {numero}")
            
        # Gestione della coerenza dati: se esiste già una lista di risultati,
        # la imposta a None per forzare la rigenerazione alla prossima chiamata
        if hasattr(self, "risultato"):
            self.risultato = None
        
        return trovato
    

def main():
    """
    Funzione principale che dimostra come utilizzare la classe Rubrica.
    Crea una rubrica, legge i contatti da un file, rimuove un contatto specifico,
    e visualizza il risultato.
    """
    # Crea un'istanza della classe Rubrica specificando il percorso del file
    rubrica = Rubrica("contatti.txt")
    rubrica.leggi_contatto()  # Legge i contatti dal file
    
    # Mostra tutti i contatti per verificare quelli disponibili
    #rubrica.stampa_rubrica()
    
    # Crea un contatto con il numero che vuoi rimuovere (nome e cognome vuoti)
    numero_da_rimuovere = 7276723137  # Il numero specifico da rimuovere
    contatto_da_rimuovere = Contatto("", "", numero_da_rimuovere)
    
    # Rimuove il contatto dalla rubrica
    rimosso = rubrica.rimuovi_contatto(contatto_da_rimuovere)
    
    # Verifica e comunica il risultato dell'operazione di rimozione
    if rimosso:
        print("Contatto rimosso con successo!")
    else:
        print("Impossibile rimuovere il contatto. Verifica che il numero sia corretto.")
    
    # Mostra la rubrica aggiornata dopo la rimozione
    rubrica.stampa_rubrica()

# Punto di ingresso del programma: esegue la funzione main solo se questo file
# viene eseguito direttamente (non quando viene importato come modulo)
if __name__ == "__main__":
    main()