# Classe UnitàMilitare
class UnitàMilitare:

    # Attributi
    def __init__(self, nome, numero_soldati):

        #nome dell'unità
        self.nome = nome

        # numero di soldati nell'unità
        self.numero_soldati = numero_soldati

    # Metodi speciali richiesti

    # Rappresentazione dell'oggetto legibile per l'utente
    def __str__(self):
        return f"\n{self.nome} ({self.numero_soldati} soldati)"

    # Rappresentazione dell'oggetto tecnica per lo sviluppatore
    def __repr__(self):
        return f"\nUnitàMilitare(nome='{self.nome}', numero_soldati={self.numero_soldati})"

    # Definiamo cosa succede quando usiamo len su un oggetto,
    # in uesto caso restituisce il numero di soldati dell'unità
    def __len__(self):
        return self.numero_soldati

    # Confrontiamo due oggetti con ==
    def __eq__(self, altro):
        if isinstance(altro, UnitàMilitare):
            return self.numero_soldati == altro.numero_soldati
        return False

    # Intercetta ogni accesso agli attributi
    def __getattribute__(self, attributo):
        value = super().__getattribute__(attributo)
        print(f"\n[DEBUG] Accesso a '{attributo}'")
        print()
        return value

    # Metodi

    # Stampa un messaggio sul movimento dell'unità
    def muovi(self):
        print(f"\nL'unità {self.nome} sta avanzando verso l'accampamento nemico")

    # Stampa un messaggio sull'attacco
    def attacca(self):
        print(f"\nL'unità {self.nome} sta attaccando le trincee nemiche")

    # Gestisce il ritiro strategico
    def ritirata(self):
        print(f"\nL'unità {self.nome} sta abbandonando il campo di battaglia")

# Classi Derivate

# Costruisce difese temporanee
class Fanteria(UnitàMilitare):
    def costruisci_trincea(self):
        print(f"\n{self.nome} costruisce una trincea.")

# Calibra l'artiglieria
class Artiglieria(UnitàMilitare):
    def calibra_artiglieria(self):
        print(f"\n{self.nome} calibra i mortai.")

# Esplora l'area per raccogliere informazioni sul nemico
class Cavalleria(UnitàMilitare):
    def esplora_terreno(self):
        print(f"\n{self.nome} esplora l'area in cerca di informazioni")

# Gestisce il rifornimento e la manutenzione
class SupportoLogistico(UnitàMilitare):
    def rifornisci_unità(self):
        print(f"\n{self.nome} rifornisce le unità.")

# Conduce missioni di sorveglianza
class Ricognizione(UnitàMilitare):
    def conduci_ricognizione(self):
        print(f"\n{self.nome} conduce una ricognizione.")


# Classe ControlloMilitare che eredita da tutte le classi precedenti
# per la gestione e il controllo delle unità militari
class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):

    # Attributi del padre + attributo aggiuntivo
    def __init__(self, unità_registrate: dict[UnitàMilitare, int]):

        # Attributo aggiuntivo
        self.unità_registrate = unità_registrate

    # Metodi speciali

    # Numero di unità registrate
    def __len__(self):
        return len(self.unità_registrate)

    # Rappresentazione tecnica del controllo militare
    def __repr__(self):
        return f"\nControlloMilitare(unità={list(self.unità_registrate.keys())})"

    # Rappresentazione leggibile del controllo militare
    def __str__(self):
        return f"\nControllo con {len(self)} unità registrate"

    # Confronta due istanze
    def __eq__(self, other):
        if isinstance(other, ControlloMilitare):
            print()
            return self.unità_registrate == other.unità_registrate
        print()
        return False

    # Accesso attributi
    def __getattribute__(self, attributo):
        value = super().__getattribute__(attributo)
        print(f"\n[DEBUG] Accesso a '{attributo}'")
        print()
        return value

    # Metodi

    # Aggiunge un'unità al registro
    def registra_unità(self, unità: UnitàMilitare):
        self.unità_registrate.update({unità.nome : unità.numero_soldati})

    # Elenca tutte le unità registrate
    def mostra_unità(self):
        for unità, soldati in self.unità_registrate.items():
            print(unità, soldati)

    # Mostra dettagli specifici di un'unità
    def dettagli_unità(self, nome):
        if nome in self.unità_registrate.keys():
            soldati = self.unità_registrate[nome]
            print(f"\nL'unità {nome} ha {soldati} soldati")
        else:
            print("\nUnità non presente in registro")


# Main

# Creazione unità
f1 = Fanteria("Alfa", 100)
a1 = Artiglieria("Bravo", 50)
c1 = Cavalleria("Charlie", 70)

# Uso metodi delle unità
f1.muovi()
f1.attacca()
f1.costruisci_trincea()

a1.muovi()
a1.attacca()
a1.calibra_artiglieria()

c1.muovi()
c1.esplora_terreno()

# Uso metodi speciali delle UnitàMilitari
print("\n--- METODI SPECIALI UNITÀ MILITARI---")
# __len__
print(len(f1))
print(len(a1))
print(len(c1))

# __str__
print(f1)
print(a1)
print(c1)

# __repr__
print(repr(f1))
print(repr(a1))
print(repr(c1))

# Creazione controllo militare
controllo = ControlloMilitare({})

# Registrazione unità
controllo.registra_unità(f1)
controllo.registra_unità(a1)
controllo.registra_unità(c1)

# Visualizzazione dati sistema
print("\n--- UNITÀ REGISTRATE ---")
controllo.mostra_unità()

print("\n--- DETTAGLIO UNITÀ ---")
controllo.dettagli_unità("Alfa")
controllo.dettagli_unità("Bravo")

# Uso metodi speciali del controllo
print("\n--- METODI SPECIALI CONTROLLO---")
print(len(controllo))        # __len__
print(controllo)             # __str__
print(repr(controllo))       # __repr__

# Confronto tra controlli
controllo2 = ControlloMilitare({})
controllo2.registra_unità(f1)
controllo2.registra_unità(a1)
controllo2.registra_unità(c1)

print("\n--- CONFRONTO CONTROLLI ---")
print(controllo == controllo2)   # __eq__

# Uso di __getattribute__
print("\n--- ACCESSO ATTRIBUTI ---")
print(f1.nome)
print()
print(a1.numero_soldati)