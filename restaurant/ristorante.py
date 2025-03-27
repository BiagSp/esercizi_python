"""
Progetta e implementa un sistema di gestione per un ristorante utilizzando le classi Python. 
Il sistema dovrà gestire menu, ordinazioni, personale e clienti.

"""
from enum import Enum
from datetime import datetime



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
        self.modifiche = {}
        
        
        
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
            self.assegna_tavoli.append(numero_tavolo)
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
                raise TypeError("Lo stato deve essere un'istanza di StatoOrdine")
            
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
    def __init__(self):
        pass