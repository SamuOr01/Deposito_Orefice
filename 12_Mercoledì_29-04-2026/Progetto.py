from datetime import datetime

# Genitore
class Elettrodomestico:
    # Attributi privati
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str):
        self.__marca = marca
        self.__modello = modello
        self.set_anno_acquisto(anno_acquisto)
        self.__guasto = guasto

    # Metodi

    # Getter degli attributi
    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_anno_acquisto(self):
        return self.__anno_acquisto

    def get_guasto(self):
        return self.__guasto

    # Setter degli attributi
    def set_marca(self, marca):
        self.__marca = marca

    def set_modello(self, modello):
        self.__modello = modello

    def set_anno_acquisto(self, anno):
        anno_corrente = datetime.now().year

        if anno > anno_corrente:
            print(f"l'anno d'acquisto non può essere nel futuro (inserito: {anno})")
        self.__anno_acquisto = anno

    def set_guasto(self, guasto):
        self.__guasto = guasto

    # Metodi principali
    def descrizione(self):
        return (f"Marca: {self.__marca} - Modello: {self.__modello}"
                f"Anno: {self.__anno_acquisto} - Guasto: {self.__guasto}")

    def stima_costo_base(self):
        return 50.0


# Figlie
class Lavatrice(Elettrodomestico):

    # attributi privati
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, capacita_kg: int, giri_centifuga: int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__capacita_kg = capacita_kg
        self.__giri_centifuga = giri_centifuga

    # Metodi
    def get_capacita_kg(self):
        return self.__capacita_kg

    def get_giri_centifuga(self):
        return self.__giri_centifuga

    def set_capacita_kg(self, capacita):
        self.__capacita_kg = capacita

    def set_giri_centifuga(self, giri):
        self.__giri_centifuga = giri

    # stima costo base
    def stima_costo_base(self):
        costo = super().stima_costo_base()

        if self.get_capacita_kg() > 8:
            costo += 20.0
            return costo

        else:
            return costo

class Frigorifero(Elettrodomestico):

    # attributi
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, litri: int, ha_freezer: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__litri = litri
        self.__ha_freezer = ha_freezer

    # Metodi Getter e Setter degli attributi
    def get_litri(self):
        return self.__litri

    def get_ha_freezer(self):
        return self.__ha_freezer

    def set_litri(self, litri):
        self.__litri = litri

    def set_ha_freezer(self, ha_freezer):
        self.__ha_freezer = ha_freezer

    # stima costo base
    def stima_costo_base(self):
        costo = 45.0

        if self.get_litri() > 300:
            costo += 10.0

        if self.get_ha_freezer():
            costo += 15.0

        return costo

class Forno(Elettrodomestico):

    # attributi
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, tipo_alimentazione: str, ha_ventilato: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__tipo_alimentazione = tipo_alimentazione
        self.__ha_ventilato = ha_ventilato

    # Metodi
    def get_tipo_alimentazione(self):
        return self.__tipo_alimentazione

    def get_ha_ventilato(self):
        return self.__ha_ventilato

    def set_tipo_alimentazione(self, tipo_alimentazione):
        self.__tipo_alimentazione = tipo_alimentazione

    def set_ha_ventilato(self, ha_ventilato):
        self.__ha_ventilato = ha_ventilato

    # stima costo base
    def stima_costo_base(self):
        costo = 40.0

        if self.get_tipo_alimentazione() == "elettrico":
            costo += 25.0

        if self.get_ha_ventilato():
            costo += 10.0

        return costo

# Gestore dei Ticket
class TicketRiparazione:
    def __init__(self, id_ticket, elettrodomestico: Elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        # Lo stato iniziale è sempre "aperto" alla creazione del ticket perchè non esiste altrimenti un ticket
        self.__stato = "aperto"
        # Inizializziamo una lista vuota che conterrà le note aggiunte
        self.__note = []

    # Getter e Setter
    def get_id_ticket(self):
        return self.__id_ticket

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def get_stato(self):
        return self.__stato

    def set_stato(self, stato):
        # Lista dei valori ammessi per lo stato
        stati_validi = ["aperto", "in lavorazione", "chiuso"]

        if stato not in stati_validi:
            print(f"Stato non valido: '{stato}'. Scegli tra {stati_validi}")

        self.__stato = stato

    def get_note(self):

        # Restituiamo una copia della lista per evitare modifiche esterne
        return self.__note.copy()

    # Metodi per Aggiungere note e calcolare il preventivo
    def aggiungi_nota(self, testo):
        self.__note.append(testo)

    # La sintassi *voci_extra raccoglie tutti gli argomenti posizionali extra in una tupla rendendo il metodo variadico
    def calcola_preventivo(self, *voci_extra):

        # Chiamo il metodo polimorfico senza sapere quale sottoclasse sia l'oggetto
        costo_base = self.__elettrodomestico.stima_costo_base()
        totale = costo_base + sum(voci_extra)
        return totale

# gestore Officina
class Officina:
    def __init__(self, nome):
        self.nome = nome
        # Lista pubblica che conterrà tutti i ticket dell'officina
        self.tickets = []

    def aggiungi_ticket(self, ticket):
        self.tickets.append(ticket)

    # Cerca il ticket per id e ne aggiorna lo stato
    def chiudi_ticket(self, id_ticket):

        for ticket in self.tickets:

            if ticket.get_id_ticket() == id_ticket:
                ticket.set_stato("chiuso")
                print(f"Ticket {id_ticket} chiuso con successo.")
                return

        print(f"Ticket {id_ticket} non trovato.")

    def stampa_ticket_aperti(self):

        print(f"\n--- Ticket aperti in {self.nome} ---")

        # Variabile booleana di controllo per sapere se ha trovato almeno un ticket aperto
        trovati = False

        for ticket in self.tickets:

            # Mostriamo solo quelli non chiusi
            if ticket.get_stato() != "chiuso":
                trovati = True
                el = ticket.get_elettrodomestico()
                # Accedo all'attributo __name__ dell'oggetto classe restituito da type() per ottenere il nome della classe come stringa
                tipo = type(el).__name__
                print(f"ID: {ticket.get_id_ticket()} | Tipo: {tipo} | Stato: {ticket.get_stato()}")

        if not trovati:
            print("Nessun ticket aperto.")

    # Calcola la somma di tutti i preventivi base senza voci extra
    def totale_preventivi(self):
        totale = 0

        for ticket in self.tickets:

            # Chiamiamo senza argomenti extra quindi voci_extra sarà una tupla vuota
            totale += ticket.calcola_preventivo()

        return totale

    # Analizza i ticket per tipo di elettrodomestico
    def statistiche_per_tipo(self):

        # Dizionario con i tipi e le occorrenze
        contatori = {"Lavatrice": 0, "Frigorifero": 0, "Forno": 0, "Altro": 0}

        for ticket in self.tickets:

            el = ticket.get_elettrodomestico()

            # isinstance(oggetto, Classe) restituisce True se l'oggetto è un'istanza della classe o di una sua sottoclasse
            if isinstance(el, Lavatrice):
                contatori["Lavatrice"] += 1

            elif isinstance(el, Frigorifero):
                contatori["Frigorifero"] += 1

            elif isinstance(el, Forno):
                contatori["Forno"] += 1

            else:
                # Categoria per eventuali elettrodomestici generici
                contatori["Altro"] += 1

        print("\n--- Statistiche per tipo ---")

        for tipo, quantita in contatori.items():
            print(f"Numero di {tipo.lower()} in riparazione: {quantita}")


#Test e stampa

print("\n|||||||||| OFFICINA DI LUCA E SAMUELE - RIPARALAND ||||||||||\n")

# Creazione degli elettrodomestici
lav1 = Lavatrice("Samsung", "WW90T", 2019, "Pompa di scarico rotta", 9, 1200)
lav2 = Lavatrice("Whirlpool", "Serie4", 2021, "Centrifuga troppo rumorosa", 7, 1000)
fri1 = Frigorifero("LG", "GBB72", 2020, "Non raffredda", 360, True)
fri2 = Frigorifero("Whirlpool", "SW8AM2", 2018, "Perdita d'acqua", 250, False)
for1 = Forno("Samsung", "SEW884", 2022, "Resistenza bruciata", "elettrico", True)
for2 = Forno("Smeg", "TR4110", 2017, "Termostato difettoso", "gas", False)

# Mostriamo la descrizione e il costo base di ogni elettrodomestico
print("--- Descrizioni e stime costo base ---")
# Lista mista di oggetti di tipi diversi
elettrodomestici = [lav1, lav2, fri1, fri2, for1, for2]

for el in elettrodomestici:
    print(el.descrizione())
    print(f"> Costo base stimato: €{el.stima_costo_base():.2f}")

# Ticket di riparazione
print("\n|||||||||| Creazione dei ticket ||||||||||")
t1 = TicketRiparazione("T001", lav1)
t2 = TicketRiparazione("T002", fri1)
t3 = TicketRiparazione("T003", for1)
t4 = TicketRiparazione("T004", lav2)
t5 = TicketRiparazione("T005", fri2)
t6 = TicketRiparazione("T006", for2)

# Note e cambio stati
t1.aggiungi_nota("Richiesta ricambio pompa")
t1.aggiungi_nota("Cliente disponibile dal pomeriggio")
t2.set_stato("in lavorazione")
t3.aggiungi_nota("Resistenza da ordinare")

# Calcolo preventivi con voci extra usando il metodo variadico
print("\n--- Preventivi ---")

# Passsiamo tre voci extra che vengono raccolte nella tupla voci_extra
prev_t1 = t1.calcola_preventivo(25.0, 15.0, 8.50)
prev_t2 = t2.calcola_preventivo(40.0)
prev_t3 = t3.calcola_preventivo(55.0, 12.0)

# Senza voci extra sum() su tupla vuota restituisce 0
prev_t4 = t4.calcola_preventivo()
print(f"Preventivo T001 (Lavatrice 9kg): €{prev_t1:.2f}")
print(f"Preventivo T002 (Frigorifero con freezer): €{prev_t2:.2f}")
print(f"Preventivo T003 (Forno elettrico ventilato): €{prev_t3:.2f}")
print(f"Preventivo T004 (Lavatrice 7kg): €{prev_t4:.2f}")

# Creazione dell'officina e aggiungo tutti i ticket
print("\n|||||||||| Gestione offcina ||||||||||")
officina = Officina("Riparazioni veloci Sicilia")

for t in [t1, t2, t3, t4, t5, t6]:
    officina.aggiungi_ticket(t)

officina.stampa_ticket_aperti()

# Chiudiamo un ticket e verifichiamo che sparisca dalla lista degli aperti
officina.chiudi_ticket("T005")
officina.stampa_ticket_aperti()

# Mostro il totale di tutti i preventivi base
print(f"\nTotale preventivi base (senza voci extra): €{officina.totale_preventivi():.2f}")

# Mostro le statistiche per tipo usando isinstance()
officina.statistiche_per_tipo()

# Dimostriamo l'uso diretto di type() per confronto esplicito
print("\n--- Uso diretto di type() ---")

for ticket in officina.tickets:
    el = ticket.get_elettrodomestico()
    # type() restituisce l'oggettp classe esatto senza risalire la gerarchia a differenza di isinstance
    if type(el) == Lavatrice:
        print(f"Ticket {ticket.get_id_ticket()}: tipo esatto di lavatrice rilevato con type()")