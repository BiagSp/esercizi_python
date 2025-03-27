"""
Esercizio 2: Lettura e Scrittura File di Log
Obiettivo: Creare un sistema di logging che legga e scriva su file.
Requisiti:

Crea una classe Logger che:

Scriva messaggi di log su un file con data, ora e livello (INFO, WARNING, ERROR)
Permetta di leggere i log esistenti
Permetta di filtrare i log per livello o data

"""
import datetime

class Logger:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def log(self, messaggio, livello= "INFO"):
        self.messaggio = messaggio
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        log_entry = f"{timestamp} [{livello}] {messaggio}\n"
        
        with open(self.file_path, "a") as file:
            file.write(log_entry)
            
        print(log_entry, end="")
    
    def leggi_logs(self):
        """
        Legge e restituisce tutti i log dal file.
        
        Returns:
            list: lista di stringhe, ciascuna rappresentante una riga di log
        """
        # Qui implementerai la lettura dei log dal file
        try:
            with open(self.file_path, 'r') as file:
                logs = file.readlines()
            return logs
        except FileNotFoundError:
            print(f"Attenzione: il file {self.file_path} non esiste")
            return []

    def filtra_per_livello(self, livello):
        """
        Filtra i log per livello.
        
        Args:
            livello (str): il livello per cui filtrare (INFO, WARNING, ERROR)
            
        Returns:
            list: lista di stringhe contenenti solo i log del livello specificato
        """
        # Qui implementerai il filtro per livello
        logs = self.leggi_logs()
        logs_filtrati = []
        
        for log in logs:
            if f"{livello}" in log:
                logs_filtrati.append(log)
                
        return logs_filtrati
    
        
    def filtra_per_data(self, data):
        logs = self.leggi_logs()
        logs_filtrati = []
        
        for log in logs:
            if log.startswith(f"[{data}"):  # Verifica solo se la stringa inizia con [data
                logs_filtrati.append(log)
        
        return logs_filtrati
        
        
        
def main():
    
    logger = Logger("File_log.log")
    
    
    logger.log("Applicazione avviata", "INFO")
    logger.log("Utente ha effettuato il login", "INFO")
    logger.log("Tentativo di accesso a risorse non autorizzate", "WARNING")
    logger.log("Connessione al database non riuscita", "ERROR")
    logger.log("Operazione completata con successo", "INFO")
        
        
    print("\nTutti i log")
    #filtro per livello
    logs_warning = logger.filtra_per_livello("WARNING")
    logs_info = logger.filtra_per_livello("INFO")
    logs_errore = logger.filtra_per_livello("ERROR")

    logs = logger.leggi_logs()
    for log in logs:
        print(log, end="")
        
    #filtraggio per data
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"\nLog di oggi {today}")
    logs_oggi = logger.filtra_per_data(today)
    for log in logs_oggi:
        print(log, end="")
        
        
if __name__ == "__main__":
    main()