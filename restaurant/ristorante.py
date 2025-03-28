"""
Progetta e implementa un sistema di gestione per un ristorante utilizzando le classi Python. 
Il sistema dovrà gestire menu, ordinazioni, personale e clienti.

"""
from enum import Enum
from datetime import datetime, timedelta, time




class StatoOrdine(Enum):
    RICEVUTO = "ricevuto"
    IN_PREPARAZIONE = "in preparazione"
    SERVITO = "servito"
    PAGATO = "pagato"
    

class RuoloDipendente(Enum):
    CHEF = "CHEF"
    SOUSCHEF = "SOUSCHEF"
    MAITRE = "MAITRE"
    CAMERIERE = "CAMERIERE"
    SOMMELIER = "SOMMELIER"
    HOSTESS = "HOSTESS"
    BARISTA = "BARISTA"
    CASSIERE = "CASSIERE"
    MENAGER = "MENAGER"
    
    
    
class LivelloChef(Enum):
    COMMIS = "Commis"  # Apprendista
    CHEF_DE_PARTIE = "Chef de Partie"  # Capo partita
    SOUS_CHEF = "Sous Chef"  # Vice capo
    CHEF_DE_CUISINE = "Chef de Cuisine"  # Capo chef
    EXECUTIVE_CHEF = "Executive Chef"  # Chef esecutivo
    
    
    
    
class CategoriaEnum(Enum):
    ANTIPASTO = "Antipasto"
    PRIMO = "Primo"
    SECONDO = "Secondo"
    DESSERT = "Dessert"


class Piatto:
    def __init__(self, nome, descrizione, prezzo, categoria:CategoriaEnum, ingredienti:list, tempo):
        self.nome = nome
        self.descrizione = descrizione
        self.prezzo = prezzo
        self.categoria = categoria
        self.ingredienti = ingredienti
        self.tempo = tempo
        
        


class Menu:
    def __init__(self):
        self.piatti = []
        # Creiamo una lista di piatti per Ingredienti
        self.indice_ingredienti = {}
        self.modifiche = []
        
        
        
    # Implementiamo il metodo per salvare le modifiche degli chef
    def modifiche_menu(self, vecchio_item, nuovo_item, id_dipendente, piatto_modificato):
        self.modifiche.append({
            "time_stamp": datetime.now(),
            "id_dipendente": id_dipendente,
            "vecchio_item": vecchio_item,
            "nuovo_item": nuovo_item,
            "piatto_modificato": piatto_modificato
        }) 
        
    
    def aggiungi_piatto(self, piatto):
        if isinstance(piatto, Piatto):
            # Verifichiamo se esiste già un piatto con lo stesso nome
            for p in self.piatti:
                if p.nome == piatto.nome:
                    print(f"Il piatto: {piatto.nome} esiste già nel menu")
                    return
            self.piatti.append(piatto)
            # Aggiorniamo l'indice degli ingredienti
            for ingrediente in piatto.ingredienti:
                if ingrediente not in self.indice_ingredienti:
                    self.indice_ingredienti[ingrediente] = []
                self.indice_ingredienti[ingrediente].append(piatto)
        else:
            raise TypeError("L'oggetto deve essere un'istanza della classe Piatto")


    def rimuovi_piatto(self, piatto):
        if isinstance(piatto, Piatto):
            for i, p in enumerate(self.piatti):
                if p.nome == piatto.nome:
                    del self.piatti[i]
                    return f"Il piatto {piatto.nome} è stato rimosso dal menu"
            return f"Il piatto {piatto.nome} non è stato trovato nel menu"
        else:
            raise TypeError("L'oggetto deve essre un'istanza della classe Piatto")
        
                     
    def cerca_piatto_per_nome(self, nome_piatto):
        risultati = []
        for p in self.piatti:
            if nome_piatto.lower() in p.nome.lower():
                risultati.append(p)
        if not risultati:
           return f"Piatto {nome_piatto} non trovato nel menu"
        return risultati


    def cerca_piatto_per_ingrediente(self, ingrediente):
        
        risultati = []
        ingrediente_lower = ingrediente.lower()
        
        # Cerchiamo corrispondenze parziali
        for ingr, piatti in self.indice_ingredienti.items():
            if ingrediente_lower in ingr.lower():
                # Aggiugniamo tutti i piatti che contengono questo ingrediente
                risultati.extend(piatti)

        # Controlliamo i duplicati (piatti che contengo più ingredienti)
        # che corrispondono alla ricerca che va filtrata
        
        piatti_unici = []
        piatti_visti = set()

        for piatto in risultati:
            if piatto.nome not in piatti_visti:
                piatti_unici.append(piatto)
                piatti_visti.add(piatto.nome)
                
        if not piatti_unici:
            return f"Nessun piatto contiene l'ingrediente {ingrediente}"
        
        return piatti_unici



    def visualizza_piatti_per_categoria(self, categoria_input):
        piatti_categoria = []
        
        # Convertiamo la stringa in un oggetto CategoriaEnum
        categoria_enum = None
        
        # Se è già un CategoriaEnum, lo usiamo direttamente
        if isinstance(categoria_input, CategoriaEnum):
            categoria_enum = categoria_input
        # Altrimenti, cerchiamo di convertire la stringa in un enum
        else:
            # Convertiamo in minuscolo per rendere la ricerca non sensibile alle maiuscole
            categoria_str = categoria_input.lower()
            
            # Cerchiamo l'enum corrispondente
            for enum_cat in CategoriaEnum:
                if enum_cat.value.lower() == categoria_str:
                    categoria_enum = enum_cat
                    break
        
        # Se non abbiamo trovato un enum corrispondente
        if categoria_enum is None:
            return f"Categoria '{categoria_input}' non valida. Le categorie disponibili sono: {', '.join([cat.value for cat in CategoriaEnum])}"
        
        # Cerchiamo i piatti nella categoria
        for piatto in self.piatti:
            if piatto.categoria == categoria_enum:
                piatti_categoria.append(piatto)
        
        if not piatti_categoria:
            return f"Nessun piatto trovato nella categoria '{categoria_enum.value}'"
        
        return piatti_categoria








    
class Ordine:
    def __init__(self, numero_tavolo, piatti_ordinati = None):
        self.numero_tavolo = numero_tavolo
        self.piatti_ordinati = piatti_ordinati if piatti_ordinati is not None else {}
        self.stato = StatoOrdine.RICEVUTO # lo impostiamo come stato iniziale
        self.orario_creazione = datetime.now()

    
    
    def aggiunngi_piatti_ordine(self, piatto, quantita):
        if isinstance(piatto, Piatto):
            nome = piatto.nome # Usiamo il nome come chiave
            
            if nome in self.piatti_ordinati:
                # Aggiorniamo la quantità 
                self.piatti_ordinati[nome]["quantità"] += quantita
            else:
                # Aggiugniamo sia il piatto che la quantità
                self.piatti_ordinati[nome] = {'piatto' : piatto, 'quantità' : quantita}
            return f"Aggiornato ordine: {quantita} e piatto: {nome}"
        
        else:
            raise TypeError("L'oggetto deve essere un'istanza della classe Piatto")
        
    
    def rimuovi_piatto_ordine(self, piatto, quantita):
        if isinstance(piatto, Piatto):
            nome = piatto.nome
            if nome in self.piatti_ordinati:
                # Controlliamo la quantità
                quantita_attuale = self.piatti_ordinati[nome]["quantità"]
                
                if quantita > quantita_attuale:
                    return f"La quantità che desideri rimuovere: {quantita} è maggiore di quella ordinata {quantita_attuale}"
                elif quantita == quantita_attuale:
                    del self.piatti_ordinati[nome]
                    return f"Piatto {nome} ordinato rimosso dall'ordinazione"
                else:
                    # Ridurre quantità
                    self.piatti_ordinati[nome]["quantità"] -= quantita
                    return f"La quantità ordinata aggiornata: {self.piatti_ordinati[nome]["quantità"]}"
                
            else:
                raise TypeError("L'oggetto deve essere un'istanza della classe Piatto")
            
        
    
    
    
    
    
    
    
    
    
class Dipendente:
    _ultimo_id = 1000 # Contatore per la parte numerica dell'id
    
    def __init__(self, nome, cognome, stipendio, ruolo):
        # Attributi base
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio
        self.contatti = {}  # Dizionario per email, telefono, ecc.
        
        if not isinstance(ruolo, RuoloDipendente):
            raise TypeError("Il ruovo deve essere un'istanza della classe RuoloDipendente")
        
        self.ruolo = ruolo
        self.id_dipendente = self._genera_id()
        
    def _genera_id(self):
        # Otteniamo il valore del ruolo 
        ruolo_valore = self.ruolo.value
        
        # Estraiamo le prime due lettere dal ruolo
        prime_due = ruolo_valore[:2]
        
        # Estraiamo l'ultima lettera
        ultima = ruolo_valore[-1]
        
        # Incrementiamo il contatore
        Dipendente._ultimo_id += 1
        
        # Combiniamo l'id
        return f"{prime_due}{ultima}{Dipendente._ultimo_id}"
    
    
    def mostra_info(self):
        
        info = f"=== INFORMAZIONI DIPENDENTE ===\n"
        info += f"ID: {self.id_dipendente}\n"
        info += f"Nome: {self.nome} {self.cognome}\n"
        info += f"Ruolo: {self.ruolo.value}\n"
        info += f"Stipendio: {self.stipendio} €\n"
        
        
        # Sezione contatti
        info += f"\nContatti:\n"
        if self.contatti: 
            for tipo, valore in self.contatti.items():
                info += f"{tipo.capitalize()}: {valore}"
            return info
        else:
            info += " Nessun contatto disponibile"
        

    def calcola_stipendio(self, ore_lavorate:float, ore_mensili_standard:float = 160, ) -> float:
        if ore_lavorate < ore_mensili_standard:
            fattore_proporzionale = ore_lavorate / ore_mensili_standard
            return self.stipendio * fattore_proporzionale
        else:
            tariffa_oraria = self.stipendio / ore_mensili_standard
            ore_straordinario = ore_lavorate - ore_mensili_standard
            compenso_straordinario = ore_straordinario * tariffa_oraria * 1.3
            return self.stipendio + compenso_straordinario
        
        
        


class Chef(Dipendente):
    def __init__(self, nome, cognome, stipendio, livello):
        super().__init__(nome, cognome, stipendio, RuoloDipendente.CHEF)
        
        
        if not isinstance(livello, LivelloChef):
            raise TypeError("Il livello deve essere un'istanza della classe LivelloChef")
        
        self.livello = livello
        
        
    def calcola_stipendio(self, ore_lavorate, ore_mensili_standard= 160):
        stipendio_base = super().calcola_stipendio(ore_lavorate, ore_mensili_standard)
        

        
    # Maggioriamo lo stipendio a seconda della carica che ricopre
    
        bonus = 0
        
        if hasattr(self, 'livello'):
            if self.livello == LivelloChef.COMMIS:
                bonus += 0
            elif self.livello == LivelloChef.CHEF_DE_PARTIE:
                bonus += 50
            elif self.livello == LivelloChef.SOUS_CHEF:
                bonus += 70
            elif self.livello == LivelloChef.CHEF_DE_CUISINE:
                bonus += 90
            elif self.livello == LivelloChef.EXECUTIVE_CHEF:
                bonus += 100
        
        return stipendio_base + bonus
    
    def autorizzazione_chef(self):
        autorizzato = False

        
        # Verifichiamo se esiste l'attributo livello
        if hasattr(self, "livello"):
            # Controlliamo se il livello è tra quelli autorizzati
            if self.livello in  [LivelloChef.SOUS_CHEF, LivelloChef.CHEF_DE_CUISINE, LivelloChef.EXECUTIVE_CHEF]:
                autorizzato = True
                
        return autorizzato
    
    def aggiungi_piatto_al_menu(self, menu:Menu, piatto):
        if self.autorizzazione_chef():
            menu.aggiungi_piatto(piatto)
            return True
        else:
            print(f"Lo chef {self.nome} {self.livello} / {self.ruolo} non ha l'autorizzazioe necessaria")
            return False
        
        
        
    def rimuovi_piatto_dal_menu(self, menu:Menu, nome_piatto):
        if self.autorizzazione_chef():
            menu.modifiche_menu(
                vecchio_item=None,
                nuovo_item={"piatto": nome_piatto},
                id_dipendente=self.id_dipendente
            )
            menu.rimuovi_piatto(nome_piatto)      
            return True
        else:
            print(f"Lo chef {self.nome} {self.livello} / {self.ruolo} non ha l'autorizzazioe necessaria")
            return False
    
    def modifica_ingrediente_piatto(self, menu:Menu, ingrediente_vecchio, ingrediente_nuovo, nome_piatto):
        if self.autorizzazione_chef():
            piatti_trovati = menu.cerca_piatto_per_ingrediente(ingrediente_vecchio)
            
            # Controlliamo se abbiamo una lista di piatti
            if isinstance(piatti_trovati, list):
                # Cerchiamo il piatto per nome
                for piatto in piatti_trovati:
                    if piatto.nome == nome_piatto:
                        # Modifichiamo gli ingredienti del piatto
                        if ingrediente_vecchio in menu.indice_ingredienti:
                            if piatto in menu.indice_ingredienti[ingrediente_vecchio]:
                                menu.indice_ingredienti[ingrediente_vecchio].remove(piatto)    
                                
                                 
                        
                        # Aggiorniamo la lista degli ingredienti del piatto
                        if ingrediente_vecchio in piatto.ingredienti:
                            piatto.ingredienti.remove(ingrediente_vecchio)
                        piatto.ingredienti.append(ingrediente_nuovo)
                        
                        # Aggiungiamo il piatto all'indice del nuovo ingrediente
                        if ingrediente_nuovo not in menu.indice_ingredienti:
                            menu.indice_ingredienti[ingrediente_nuovo] = []
                        menu.indice_ingredienti[ingrediente_nuovo].append(piatto)
                        
                        
                        
                        menu.modifiche_menu(
                                    vecchio_item = {"vecchio_ingrediente": ingrediente_vecchio, "piatto_nome": nome_piatto},
                                    nuovo_item = {"nuovo_ingrediente": ingrediente_nuovo, "piatto_nome": nome_piatto},
                                    id_dipendente = self.id_dipendente,
                                    piatto_modificato = piatto                             
                                )
                        
                        
                        return True
            
                # Messaggio perché non abbiamo trovato il piatto
                print(f"Nessun piatto trovato con il nome {nome_piatto} contenente l'ingrediente {ingrediente_vecchio}")
                return False
            else:
                # Questo else si riferisce al caso in cui piatti_trovati NON è una lista
                print(piatti_trovati)  # Stampa il messaggio di errore restituito dalla ricerca
                return False
        else:
            # Questo else si riferisce alla mancanza di autorizzazione
            print(f"Lo chef {self.nome} {self.cognome} non ha l'autorizzazione necessaria")
            return False                     
    
    
    
    
class Cameriere(Dipendente):
    def __init__(self, nome, cognome, stipendio):
        super().__init__(nome, cognome, stipendio, RuoloDipendente.CAMERIERE)
        self.tavoli_assegnati = []
        self.tips = 0.0
        
    def assegna_tavoli(self, numero_tavolo):
        # Assegniamo i tavoli al cameriere
        if numero_tavolo not in self.tavoli_assegnati:
            self.tavoli_assegnati.append(numero_tavolo)
            return f"Tavolo/i {numero_tavolo} asegnato a {self.id_dipendente}"
        return f"Tavolo {numero_tavolo} già asseggnato a {self.id_dipendente}"
    # Si potrebbe implementare un metodo di ricerca a chi è stato assegnato il tavolo, forse?
    
    def rimuovi_tavolo(self, numero_tavolo):
        if numero_tavolo in self.tavoli_assegnati:
            self.tavoli_assegnati.remove(numero_tavolo)
            return f"Tavolo {numero_tavolo} rimosso dagli incarichi di {self.nome} {self.cognome}"
        return f"Tavolo {numero_tavolo} non assegnato a questo cameriere"
    
    
    
    def prendi_ordine(self, numero_tavolo, menu:Menu, piatti_richiesti):
        if numero_tavolo in self.tavoli_assegnati:
            ordine = Ordine(numero_tavolo)
            for nome_piatto, quantita in piatti_richiesti.items():
                piatto_trovato = False
                for piatto in menu.piatti:
                    if piatto.nome == nome_piatto:
                        ordine.aggiunngi_piatti_ordine(piatto, quantita)
                        piatto_trovato = True
                        break
                if not piatto_trovato:
                    print(f"Piatto {nome_piatto} non trovato nel menu")
            
            return ordine
        else:
            return f"Tavolo {numero_tavolo} non assegnato a questo cameriere"
                    
    def aggiorna_stato_ordine(self, ordine:Ordine, nuovo_stato):
        if ordine.numero_tavolo in self.tavoli_assegnati:
            if not isinstance(nuovo_stato, StatoOrdine):
                raise TypeError("Lo stato d'ordine deve essere un'istanza di StatoOrdine")
            
            stato_attuale = ordine.stato
            
            transizioni_valide ={
                StatoOrdine.RICEVUTO: [StatoOrdine.IN_PREPARAZIONE],
                StatoOrdine.IN_PREPARAZIONE: [StatoOrdine.SERVITO],
                StatoOrdine.SERVITO: [StatoOrdine.PAGATO],
                StatoOrdine.PAGATO: []
            }
            
            if nuovo_stato in transizioni_valide[stato_attuale]:
                ordine.stato = nuovo_stato
                return f"Stato dell'ordine aggiornato a {nuovo_stato.value}"
            else:
                return f"Transizione non valida da {stato_attuale.value} a {nuovo_stato.value}"
        else:
            return f"Tavolo {ordine.numero_tavolo} non assegnato a questo cameriere"
                           
    def aggiungi_mancia(self, importo):
        if importo > 0:
            self.tips += importo
            return f"Mancia di {importo}€ registrata"
        return "importo mancia > di 0"
    
    
    def calcola_stipendio(self, ore_lavorate, ore_mensili_standard = 160):
        stipendio_base =  super().calcola_stipendio(ore_lavorate, ore_mensili_standard)
        return stipendio_base + self.tips
    
    
    
    

class Ristorante:
    def __init__(self, nome, indirizzo, telefono, orari_apertura = None):
        self.nome = nome
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.menu = Menu()
        self.dipendenti = []
        self.tavoli = {}
        self.ordini_attivi = []
        self.storico_ordini = []
        
        
        if orari_apertura is None:
            self.orari_apertura = {
            'lunedì': {'pranzo': ('12:00', '15:00'), 'cena': ('19:00', '23:00')},
            'martedì': {'pranzo': ('12:00', '15:00'), 'cena': ('19:00', '23:00')},
            'mercoledì': {'pranzo': ('12:00', '15:00'), 'cena': ('19:00', '23:00')},
            'giovedì': {'pranzo': ('12:00', '15:00'), 'cena': ('19:00', '23:00')},
            'venerdì': {'pranzo': ('12:00', '15:00'), 'cena': ('19:00', '23:00')},
            'sabato': {'pranzo': ('12:00', '15:00'), 'cena': ('19:00', '23:30')},
            'domenica': {'pranzo': ('12:00', '16:00'), 'cena': ('19:00', '23:00')}
        }
        else:
            self.orari_apertura = orari_apertura
        
    
    def assumi_dipendente(self, dipendente):
        if isinstance(dipendente, Dipendente):
            for dip in self.dipendenti:
                if dip.id_dipendente == dipendente.id_dipendente:
                    return f"dipendente: {dipendente} già assunto"
                
            self.dipendenti.append(dipendente)
            return f"Dipendente {dipendente.nome} {dipendente.cognome} / {dipendente.id_dipendente} assunto."

        else:
            raise TypeError("L'oggetto fornito deve essere un'istanza della classe Dipendente")
        
        
    def licenzia_dipendente(self, dipendente):
        if isinstance(dipendente, Dipendente):
            for dip in self.dipendenti:
                if dip.id_dipendente == dipendente.id_dipendente:
                    self.dipendenti.remove(dip) 
                    return f"Il dipendente {dipendente.id_dipendente} / {dipendente.nome} {dipendente.cognome} è stato licenziato"
                
            return f"Dipendente con ID {dipendente.id_dipendente} ({dipendente.nome} {dipendente.cognome}) non trovato"
        else:
            raise TypeError("L'oggetto deve essere un'istanza della classe Dipendente")      
        
        
    def aggiungi_tavolo(self, numero_tavolo, posti):
        # Verifichiamo che il numero_tavolo sia un valore valito
        if not isinstance(numero_tavolo, (int, str)):
            raise TypeError("Il numero del tavolo deve essere un intero o una stringa")
        
        # Controlliamo che non sia già presente nella lista
        if numero_tavolo in self.tavoli:
            return f"Il tavolo {numero_tavolo} è già presente nel ristorante"
        
        if not isinstance(posti, int) or posti <= 0:
            raise TypeError("Il numero di posti deve essere un intero positivo")
        
        # Aggiungiamo il tavolo al dizionario
        self.tavoli[numero_tavolo] = {
            'posti': posti,
            'occupato': False,
            'cameriere_assegnato': None
        }
        
        return f"Il tavolo {numero_tavolo} con {posti} posti a sedere, è stato aggiunto"
    
    
    def rimuovi_tavolo(self, numero_tavolo):
        if numero_tavolo in self.tavoli:
        # Controlliamo se il tavolo è attualmente in uso
            if self.tavoli[numero_tavolo].get('occupato', False):
                return f"Impossibile rimuovere il tavolo {numero_tavolo} perché è attualmente occupato"
            
            
            for dipendente in self.dipendenti:
                if isinstance(dipendente, Cameriere):
                    if numero_tavolo in dipendente.tavoli_assegnati:
                        dipendente.tavoli_assegnati.remove(numero_tavolo)
                        
                        
            del self.tavoli[numero_tavolo]
            return f"Tavolo {numero_tavolo} rimosso con successo"
        else:
            return f"Tavolo {numero_tavolo} non trovato nel ristorante"
        
    def assegna_tavolo_a_cameriere(self, numero_tavolo, dipendente):
        # Verifichiamo che il tavolo esista
        if numero_tavolo not in self.tavoli:
            return f"Tavolo {numero_tavolo} non presente nel ristorante"
        
        # Verifichiamo che il dipendente sia un cameriere
        if not isinstance(dipendente, Cameriere):
            raise TypeError("L'oggetto deve essere un'istanza della classe Cameriere")
        
        # Controlliamo se il tavolo è già assegnato a un altro cameriere
        for dip in self.dipendenti:
            if isinstance(dip, Cameriere) and dip != dipendente and numero_tavolo in dip.tavoli_assegnati:
                return f"Tavolo {numero_tavolo} già assegnato al cameriere {dip.nome} {dip.cognome}"
        
        # Aggiorniamo le informazioni del tavolo
        self.tavoli[numero_tavolo]['cameriere_assegnato'] = dipendente.id_dipendente
        
        # Aggiorniamo la lista dei tavoli del cameriere
        risultato = dipendente.assegna_tavoli(numero_tavolo)
        
        return f"Al cameriere {dipendente.nome} {dipendente.cognome} è stato assegnato il tavolo {numero_tavolo}"
    
    
    def calcola_totale_stipendi(self, ore_lavorate, ore_mensili_standard=160):
        totale_stipendi = 0
        
        for dipendente in self.dipendenti:
            try:
                stipendio_dipendente = dipendente.calcola_stipendio(ore_lavorate, ore_mensili_standard)
                totale_stipendi += stipendio_dipendente
            except (AttributeError, TypeError):
                print(f"Avviso: Impossibile calcolare lo stipendio per: {dipendente}")
        
        return totale_stipendi
    
    def calcola_incasso_per_servizio(self, data_inizio, data_fine):
        
        risultati = {
            'pranzo': 0,
            'cena': 0,
            'fuori_servizio': 0
        }
        
        for ordine in self.storico_ordini:
            if not (ordine.stato == StatoOrdine.PAGATO and data_inizio <= ordine.orario_creazione <= data_fine):
                continue
            giorno = ordine.orario_creazione.strftime('%A').lower()
            if giorno == 'monday': giorno = 'lunedì'
            elif giorno == 'tuesday': giorno = 'martedì'
            elif giorno == 'wednesday': giorno = 'mercoledì'
            elif giorno == 'thursday': giorno = 'giovedì'
            elif giorno == 'friday': giorno = 'venerdì'
            elif giorno == 'saturday': giorno = 'sabato'
            elif giorno == 'sunday': giorno = 'domenica'
            
            # Calcoliamo il totale ordine
            totale_ordine = 0
            for _, dettagli in ordine.piatti_ordinati.items():
                piatto = dettagli['piatto']
                quantita = dettagli['quantità']
                
                totale_ordine += piatto.prezzo * quantita
                
            ora_ordine = ordine.orario_creazione.time()
            servizio_trovato = False
            # Controlliamo in quale servizio rientra l'ordine
            for servizio, (inizio_str, fine_str) in self.orari_apertura[giorno].items():
                # Convertiamo le stringhe di orario in oggetti time
                h_inizio, m_inizio = map(int, inizio_str.split(':'))
                h_fine, m_fine = map(int, fine_str.split(':'))
                
                ora_inizio = time(h_inizio, m_inizio)
                ora_fine = time(h_fine, h_fine)
                
                if ora_inizio <= ora_ordine <=ora_fine:
                    risultati[servizio] += totale_ordine
                    servizio_trovato = True
                    break
                
                if not servizio_trovato:
                    risultati['fuori_servizio'] += totale_ordine
                    
        return risultati
                
            
            
            


# ====== TESTING DEL SISTEMA ====== #

# Import delle librerie necessarie
from datetime import datetime, timedelta
from enum import Enum
# Import delle nostre classi (assumendo che siano definite in altri file)
# from ristorante import Ristorante
# from dipendente import Dipendente, Chef, Cameriere
# from menu import Menu, Piatto, CategoriaEnum
# from ordine import Ordine, StatoOrdine

def main():
    """Funzione principale per testare il sistema di gestione ristorante."""
    print("Avvio del test del sistema di gestione ristorante...")
    
    # 1. Creazione del ristorante
    ristorante = Ristorante("La Buona Cucina", "Via Roma 123, Milano", "+39 02 1234567")
    print(f"Ristorante creato: {ristorante.nome}")
    
    # 2. Aggiunta di personale
    chef_esecutivo = Chef("Marco", "Rossi", 3000, LivelloChef.EXECUTIVE_CHEF)
    chef_sous = Chef("Laura", "Verdi", 2500, LivelloChef.SOUS_CHEF)
    cameriere1 = Cameriere("Giuseppe", "Bianchi", 1800)
    cameriere2 = Cameriere("Sofia", "Neri", 1800)
    
    # Assunzione del personale
    print("\nAssunzione del personale:")
    print(ristorante.assumi_dipendente(chef_esecutivo))
    print(ristorante.assumi_dipendente(chef_sous))
    print(ristorante.assumi_dipendente(cameriere1))
    print(ristorante.assumi_dipendente(cameriere2))
    
    # 3. Creazione del menu
    print("\nCreazione del menu:")
    pasta_pomodoro = Piatto("Pasta al Pomodoro", "Pasta con salsa di pomodoro fresco e basilico", 
                             10.50, CategoriaEnum.PRIMO, ["pasta", "pomodoro", "basilico"], 15)
    risotto_funghi = Piatto("Risotto ai Funghi", "Risotto con funghi porcini e parmigiano", 
                            14.00, CategoriaEnum.PRIMO, ["riso", "funghi", "parmigiano"], 20)
    bistecca = Piatto("Bistecca alla Fiorentina", "Bistecca di manzo alla griglia", 
                      25.00, CategoriaEnum.SECONDO, ["manzo", "rosmarino"], 25)
    tiramisu = Piatto("Tiramisù", "Dolce classico italiano con caffè e mascarpone", 
                       8.00, CategoriaEnum.DESSERT, ["mascarpone", "caffè", "cacao"], 10)
    
    # Lo chef esecutivo aggiunge i piatti al menu
    print(chef_esecutivo.aggiungi_piatto_al_menu(ristorante.menu, pasta_pomodoro))
    print(chef_esecutivo.aggiungi_piatto_al_menu(ristorante.menu, risotto_funghi))
    print(chef_esecutivo.aggiungi_piatto_al_menu(ristorante.menu, bistecca))
    print(chef_esecutivo.aggiungi_piatto_al_menu(ristorante.menu, tiramisu))
    
    # Lo chef sous prova a modificare un ingrediente
    print("\nModifica di un ingrediente:")
    print(chef_sous.modifica_ingrediente_piatto(ristorante.menu, "pomodoro", "pomodorini", "Pasta al Pomodoro"))
    
    # 4. Gestione dei tavoli
    print("\nAggiunta di tavoli:")
    print(ristorante.aggiungi_tavolo(1, 4))  # Tavolo 1 con 4 posti
    print(ristorante.aggiungi_tavolo(2, 2))  # Tavolo 2 con 2 posti
    print(ristorante.aggiungi_tavolo(3, 6))  # Tavolo 3 con 6 posti
    print(ristorante.aggiungi_tavolo(4, 4))  # Tavolo 4 con 4 posti
    
    # 5. Assegnazione dei tavoli ai camerieri
    print("\nAssegnazione dei tavoli:")
    print(ristorante.assegna_tavolo_a_cameriere(1, cameriere1))
    print(ristorante.assegna_tavolo_a_cameriere(2, cameriere1))
    print(ristorante.assegna_tavolo_a_cameriere(3, cameriere2))
    print(ristorante.assegna_tavolo_a_cameriere(4, cameriere2))
    
    # 6. Gestione degli ordini
    print("\nCreazione degli ordini:")
    # Creiamo ordini per due tavoli
    ordine_tavolo1 = cameriere1.prendi_ordine(1, ristorante.menu, {
        "Pasta al Pomodoro": 2,
        "Tiramisù": 2
    })
    
    ordine_tavolo3 = cameriere2.prendi_ordine(3, ristorante.menu, {
        "Risotto ai Funghi": 3,
        "Bistecca alla Fiorentina": 2,
        "Tiramisù": 5
    })
    
    # Aggiungiamo gli ordini alla lista degli ordini attivi
    ristorante.ordini_attivi.append(ordine_tavolo1)
    ristorante.ordini_attivi.append(ordine_tavolo3)
    print(f"Ordini attivi: {len(ristorante.ordini_attivi)}")
    
    # 7. Gestiamo il flusso degli ordini
    print("\nAggiornamento degli stati degli ordini:")
    # Aggiorniamo lo stato degli ordini
    print(cameriere1.aggiorna_stato_ordine(ordine_tavolo1, StatoOrdine.IN_PREPARAZIONE))
    print(cameriere2.aggiorna_stato_ordine(ordine_tavolo3, StatoOrdine.IN_PREPARAZIONE))
    
    # Ordini serviti
    print(cameriere1.aggiorna_stato_ordine(ordine_tavolo1, StatoOrdine.SERVITO))
    print(cameriere2.aggiorna_stato_ordine(ordine_tavolo3, StatoOrdine.SERVITO))
    
    # Ordini pagati
    print(cameriere1.aggiorna_stato_ordine(ordine_tavolo1, StatoOrdine.PAGATO))
    print(cameriere2.aggiorna_stato_ordine(ordine_tavolo3, StatoOrdine.PAGATO))
    
    # Spostiamo gli ordini completati nello storico
    ristorante.storico_ordini.append(ordine_tavolo1)
    ristorante.storico_ordini.append(ordine_tavolo3)
    ristorante.ordini_attivi.remove(ordine_tavolo1)
    ristorante.ordini_attivi.remove(ordine_tavolo3)
    print(f"Ordini attivi: {len(ristorante.ordini_attivi)}, Storico ordini: {len(ristorante.storico_ordini)}")
    
    # Registriamo una mancia per il cameriere1
    print("\nMance:")
    print(cameriere1.aggiungi_mancia(10.0))
    
    # 8. Analizziamo i dati finanziari
    print("\nAnalisi finanziarie:")
    # Calcoliamo il totale degli stipendi
    totale_stipendi = ristorante.calcola_totale_stipendi(160)  # 160 ore mensili standard
    print(f"Totale stipendi mensili: {totale_stipendi:.2f} €")
    
    # Calcoliamo gli incassi per un periodo
    data_inizio = datetime.now() - timedelta(days=7)  # Una settimana fa
    data_fine = datetime.now()
    incassi = ristorante.calcola_incasso_per_servizio(data_inizio, data_fine)
    print(f"Incasso totale dell'ultima settimana: {incassi} €")
    
    # Analizziamo gli incassi per servizio
    incassi_per_servizio = ristorante.calcola_incasso_per_servizio(data_inizio, data_fine)
    print("Incassi per servizio:")
    for servizio, importo in incassi_per_servizio.items():
        print(f"  {servizio.capitalize()}: {importo} €")
    
    print("\nTest completato con successo!")

if __name__ == "__main__":
    main()