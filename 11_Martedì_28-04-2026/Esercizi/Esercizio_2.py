# Libreria per definire le classi astratte
from abc import ABC, abstractmethod

# Classe Astratta
class VeicoloTrasporto(ABC):

    # Inizializzazione degli attributi
    def __init__(self, targa: str, peso_massimo: int):
        self._targa = targa
        self._peso_massimo = peso_massimo

        # 0 perchè è vuoto
        self._carico_attuale = 0

    # Metodo astratto
    @abstractmethod
    def costo_manutenzione(self):
        pass

    # Metodi concreti
    def carica(self, peso):
        if peso <= self._peso_massimo:
            self._carico_attuale += peso
        else:
            print("Mi dispiace, il peso supera la capacità massima")

    def scarica(self):
        self._carico_attuale = 0

    # Getter targa e peso massimo
    def get_targa(self):
        return self._targa.upper()

    def get_peso_massimo(self):
        return self._peso_massimo

# Classe Camion figlia di VeicoloTrasporto
class Camion(VeicoloTrasporto):

    # Inizializzazione degli attributi
    def __init__(self, targa: str, peso_massimo: int, numero_assi: int):
        super().__init__(targa, peso_massimo)
        self.__numero_assi = numero_assi

    # Metodo implementato dalla classe figlia
    def costo_manutenzione(self):
        return (100 * self.get_numero_assi()) + (1 * self.get_peso_massimo())

    # Getter numero assi
    def get_numero_assi(self):
        return self.__numero_assi


# Classe Furgone figlia di VeicoloTrasporto
class Furgone(VeicoloTrasporto):

    # Inizializzazione degli attributi
    def __init__(self, targa: str, peso_massimo: int, alimentazione: str):
        super().__init__(targa, peso_massimo)
        self.__alimentazione = alimentazione

    # Metodo implementato dalla classe figlia
    def costo_manutenzione(self):
        if self.get_alimentazione() == "elettrico":
            return 200 + (1 * self.get_peso_massimo())
        elif self.get_alimentazione() == "diesel":
            return 150 + (1 * self.get_peso_massimo())
        else:
            return 100 + (1 * self.get_peso_massimo())

    # Getter alimentazione
    def get_alimentazione(self):
        return self.__alimentazione.lower()

# Classe Motocarro figlia di VeicoloTrasporto
class Motocarro(VeicoloTrasporto):

    # Inizializzazione degli attributi
    def __init__(self, targa: str, peso_massimo: int, anni_servizio: int):
        super().__init__(targa, peso_massimo)
        self.__anni_servizio = anni_servizio

    # Metodo implementato dalla classe figlia
    def costo_manutenzione(self):
        return (50 * self.get_anni_servizio()) + (1 * self.get_peso_massimo())

    # Getter anni di servizio
    def get_anni_servizio(self):
        return self.__anni_servizio

# Classe per la gestione dei veicoli
class gestoreFlotta:

    # Inizializzazione degli attributi
    def __init__(self, veicoli: list[VeicoloTrasporto]):
        self.__veicoli = veicoli

    # Getter lista veicoli
    def get_veicoli(self):
        return self.__veicoli

    # Metodo per aggiungere un veicolo alla lista
    def aggiungi_veicolo(self, veicolo: VeicoloTrasporto):
        self.get_veicoli().append(veicolo)

    # Metodo per rimuovere un veicolo dalla lista
    def rimuovi_veicolo(self, targa: str):
        for veicolo in self.get_veicoli():
            if veicolo.get_targa() == targa:
                self.get_veicoli().remove(veicolo)
                print(f"Il veicolo con la targa: {targa} è stato rimosso dalla lista dei veicoli")
        else:
            print(f"Non è presente alcun veicolo con la targa: {targa}")

    # Metodo per calcolare il costo totale della manutenzione del veicolo
    def costo_totale_manutenzione(self):
        somma_costo_manutenzione_veicoli = 0
        for veicolo in self.get_veicoli():
            somma_costo_manutenzione_veicoli += veicolo.costo_manutenzione()
        return somma_costo_manutenzione_veicoli

    # Metodo per stampare la lista
    def stampa_veicoli(self):
        pass