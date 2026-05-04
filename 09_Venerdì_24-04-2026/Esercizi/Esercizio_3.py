# Classe Genitore
class Veicolo:

    # Attributi
    def __init__(self, marca: str, modello: str, anno: int, accensione: bool):

        # Attributi protetti
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = accensione

    # Metodi

    def accendi(self):
        self._accensione = True
        return self._accensione

    def spegni(self):
        self._accensione = False
        return self._accensione

    def get_marca(self):
        return self._marca.lower()

    def get_modello(self):
        return self._modello.lower()

    def get_anno(self):
        return self._anno

# Classi Figlie:
class Auto(Veicolo):

    # Attributi
    def __init__(self, marca: str, modello: str, anno: int, accensione: bool, numero_porte: int):

        # Attributi protetti del genitore
        super().__init__(marca, modello, anno, accensione)

        # Attributo protetto del figlio
        self._numero_porte = numero_porte

    # Metodi
    def suona_clacson(self):
        print("PIIIIIIIII")

    def get_numero_porte(self):
        return self._numero_porte

class Furgone(Veicolo):

    # Attributi
    def __init__(self, marca: str, modello: str, anno: int, accensione: bool, capacità_carico: int):

        # Attributi protetti del genitore
        super().__init__(marca, modello, anno, accensione)

        # Attributo protetto del figlio
        self._capacità_carico = capacità_carico

    # Metodi
    def carica(self):
        print("Sto caricando il furgone")

    def scarica(self):
        print("Sto scaricando il furgone")

    def get_capacità_carico(self):
        return self._capacità_carico

class Motocicletta(Veicolo):

    # Attributi
    def __init__(self, marca: str, modello: str, anno: int, accensione: bool, tipo: str):

        # Attributi protetti del genitore
        super().__init__(marca, modello, anno, accensione)

        # Attributo protetto del figlio
        self._tipo = tipo

    # Metodi
    def esegui_wheelie(self):

        # Se la moto è sportiva, esegui il wheelie
        if self.get_tipo() == "sportiva":
            print("Sto impennandoooo!!!")
        else:
            print("Non posso impennare con questa moto")

    def get_tipo(self):
        return self._tipo.lower()

# Classe parallela per la gestione
class GestoreParcoVeicoli:

    # Attributi
    def __init__(self, veicoli: list[Veicolo]):

        # Attributo protetto
        self._veicoli = veicoli

    # Metodi

    def get_veicoli(self):
        return self._veicoli

    def aggiungi_veicolo(self, veicolo: Veicolo):

        # Controlla se il veicolo è già presente nel parco
        for v in self.get_veicoli():
            if veicolo.get_marca() == v.get_marca() and veicolo.get_modello() == v.get_modello():
                print("Veicolo già presente in lista")
                break
        else:
            self.get_veicoli().append(veicolo)
            print("Veicolo aggiunto")

    def rimuovi_veicolo(self, marca: str, modello: str):

        # Cerca il veicolo da rimuovere nella lista
        for veicolo in self.get_veicoli():
            if veicolo.get_marca() == marca.lower() and veicolo.get_modello() == modello.lower():
                self.get_veicoli().remove(veicolo)
                print("Veicolo rimosso dalla lista")
                break
        else:
            print("Veicolo non presente in lista")

    def lista_veicoli(self):

        # Stampa i dettagli di ciascun veicolo nella lista
        for i, veicolo in enumerate(self.get_veicoli(), 1):
            print(f"{i}. Marca: {veicolo.get_marca()}, Modello: {veicolo.get_modello()}, Anno: {veicolo.get_anno()}")

# Creazione di veicoli
auto1 = Auto(marca="Toyota", modello="Corolla", anno=2022, accensione=False, numero_porte=4)
furgone1 = Furgone(marca="Fiat", modello="Ducato", anno=2021, accensione=False, capacità_carico=1500)
moto1 = Motocicletta(marca="Ducati", modello="Panigale V4", anno=2023, accensione=False, tipo="Sportiva")

# Creazione del gestore del parco veicoli
gestore = GestoreParcoVeicoli([])

# Aggiungi veicoli al parco
gestore.aggiungi_veicolo(auto1)
gestore.aggiungi_veicolo(furgone1)
gestore.aggiungi_veicolo(moto1)

# Mostra la lista dei veicoli
gestore.lista_veicoli()

# Accendere i veicoli
auto1.accendi()
furgone1.accendi()
moto1.accendi()

# Suonare il clacson dell'auto
auto1.suona_clacson()

# Caricare e scaricare il furgone
furgone1.carica()
furgone1.scarica()

# Eseguire un wheelie con la moto
moto1.esegui_wheelie()

# Rimuovere un veicolo dal parco
gestore.rimuovi_veicolo("Toyota", "Corolla")

# Mostra di nuovo la lista dei veicoli
gestore.lista_veicoli()