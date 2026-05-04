import random
# Classe Genitore MembroSquadra
class MembroSquadra:

    # Costruttore che inizializza gli attributi del genitore
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    # Metodo che stampa una descrizione generale del membro della squadra
    def descrivi(self):
        print(f"Il membro {self.nome} ha {self.età} anni")

# Classe per i giocatori
class Giocatore(MembroSquadra):

    # Costruttore che inizializza gli attributi della classe figlia
    def __init__(self, nome, età, ruolo, numero_maglia):

        # Attributi del genitore
        super().__init__(nome, età)

        # Attributi della classe figlia
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    # Override Metodo descrivi
    def descrivi(self):
        print(f"Il giocaotore {self.nome} ha {self.età} anni, è un {self.ruolo} e ha la maglia numero {self.numero_maglia}")

    # Metodo che include le azioni e i ruoli dei giocatori
    def gioca_partita(self):
        match self.ruolo.lower():
            case "attaccante":
                print(f"{self.nome} ({self.ruolo} con la maglia n° {self.numero_maglia}) tira in porta")
            case "centrocampista":
                print(f"{self.nome} ({self.ruolo} con la maglia n° {self.numero_maglia}) effettua un cross insidioso")
            case "difensore":
                print(f"{self.nome} ({self.ruolo} con la maglia n° {self.numero_maglia}) impedisce agli avversari di raggiungere la porta")
            case "portiere":
                print(f"{self.nome} ({self.ruolo} con la maglia n° {self.numero_maglia}) riesce a bloccare un tiro impossibile")



# Classe per l'allenatore
class Allenatore(MembroSquadra):

    # Costruttore che inizializza gli attributi della classe figlia
    def __init__(self, nome, età, anni_di_esperienza):

        # Attributi del genitore
        super().__init__(nome, età)

        # Attributi della classe figlia
        self.anni_di_esperienza = anni_di_esperienza

    # Override Metodo descrivi
    def descrivi(self):
        print(f"Il mister {self.nome} ha {self.età} anni e ha {self.anni_di_esperienza} anni di esperienza come allenatore")

    # Metodo che include le azioni dell'allenatore
    def dirige_la_squadra(self):

        print(f"Il mister {self.nome} urla")

        match random.randint(1, 3):
            case 1:
                print("Spingete sulle fasce!")
            case 2:
                print("Difesa alta!")
            case 3:
                print("Pressing!")

# Classe per l'assistente
class Assistente(MembroSquadra):

    # Costruttore che inizializza gli attributi della classe figlia
    def __init__(self, nome, età, specializzazione):

        # Attributi del genitore
        super().__init__(nome, età)

        # Attributi della classe figlia
        self.specializzazione = specializzazione

    # Override Metodo descrivi
    def descrivi(self):
        print(f"Il membro {self.nome} ha {self.età} anni ed è un {self.specializzazione}")

    # Metodo che include le specializzazioni e le azioni degli assistenti
    def supporta_team(self):

        match self.specializzazione.lower():
            case "fisioterapista":
                print(f"{self.nome} ({self.specializzazione}) si occupa del recupero dei giocatori")
            case "analista":
                print(f"{self.nome} ({self.specializzazione}) si occupa di studiare gli avversari")
            case "preparatore atletico":
                print(f"{self.nome} ({self.specializzazione}) si occupa di preparare la condizione fisica dei giocatori")

# Classe per le squadre
class Squadra:

    # Costruttore che inizializza gli attributi della squadra
    def __init__(self, membri: list[MembroSquadra]):
        self.membri = membri

    # Metodo per aggiungere membri
    def aggiungi_membri(self):

        for _ in range(11):
            giocatore = Giocatore(
                                input("Inserisci nome: "),
                                int(input("Inserisci età: ")),
                                input("inserisci il ruolo: "),
                                int(input("Inserisci numero maglia: "))
                                )
            self.membri.append(giocatore)

        allenatore = Allenatore(
                            input("Inserisci nome: "),
                            int(input("Inserisci età: ")),
                            int(input("Inserisci gli anni di esperienza: "))
                            )

        self.membri.append(allenatore)

        assistente = Assistente(
                            input("Inserisci nome: "),
                            int(input("Inserisci età: ")),
                            input("inserisci la specializzazione: ")
                            )

        self.membri.append(assistente)

    # Metodo per elencare i membri
    def mostra_membri(self):

        print("I membri della squdra sono")
        for membro in self.membri:
            membro.descrivi()

    # Metodo per giocare contro un'altra squadra
    def gioca(self):

        for membro in self.membri:

            if isinstance(membro, Giocatore):
                membro.gioca_partita()
            elif isinstance(membro, Allenatore):
                membro.dirige_la_squadra()
            elif isinstance(membro, Assistente):
                membro.supporta_team()


    def azione_attacco(self, squadra_attacco, squadra_difesa):

        centrocampisti = []
        attaccanti = []
        difensori = []
        portieri = []

        # squadra che attacca
        for m in squadra_attacco.membri:
            if isinstance(m, Giocatore):
                if m.ruolo.lower() == "centrocampista":
                    centrocampisti.append(m)
                elif m.ruolo.lower() == "attaccante":
                    attaccanti.append(m)

        # squadra che difende
        for m in squadra_difesa.membri:
            if isinstance(m, Giocatore):
                if m.ruolo.lower() == "difensore":
                    difensori.append(m)
                elif m.ruolo.lower() == "portiere":
                    portieri.append(m)

        if not (centrocampisti and attaccanti and portieri):
            return 0

        # CROSS
        if random.random() > 0.3:
            print("Cross riuscito!")

            # DIFESA
            if difensori and random.random() < 0.4:
                print("Il difensore intercetta!")
                return 0

            # TIRO
            if random.random() > 0.4:
                print("Tiro in porta!")

                # PORTIERE
                if random.random() < 0.5:
                    print("GOOOOL!")
                    return 1
                else:
                    print("Parata del portiere!")
                    return 0
            else:
                print("Tiro sbagliato!")
                return 0
        else:
            print("Cross sbagliato!")
            return 0

    def partita(self, altra_squadra):

        print("\nInizia la partita!\n")

        print("\nSquadra 1 entra in campo:")
        self.gioca()

        print("\nSquadra 2 entra in campo:")
        altra_squadra.gioca()

        gol_self = 0
        gol_other = 0

        for _ in range(10):  # 10 azioni per squadra

            gol_self += self.azione_attacco(self, altra_squadra)
            gol_other += self.azione_attacco(altra_squadra, self)


        print("\nRISULTATO FINALE:")
        print(f"Squadra 1: {gol_self}")
        print(f"Squadra 2: {gol_other}")

        if gol_self > gol_other:
            print("Vince la Squadra 1!")
        elif gol_self < gol_other:
            print("Vince la Squadra 2!")
        else:
            print("Pareggio!")

# Main
Team1 = Squadra([])
Team2 = Squadra([])

Team1.aggiungi_membri()
Team1.mostra_membri()

Team2.aggiungi_membri()
Team2.mostra_membri()

Team1.partita(Team2)