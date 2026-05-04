# Libreria per definire le classi astratte
from abc import ABC, abstractmethod

# classe con metodi astratti
class Impiegato:

    def __init__(self, nome: str, cognome: str, stipendio_base: float):
        self._nome = nome
        self._cognome = cognome
        self._stipendio_base = stipendio_base

    @abstractmethod
    def calcola_stipendio(self):
        pass

    def get_nome(self):
        return self._nome.capitalize()

    def get_cognome(self):
        return self._cognome.capitalize()

    def get_stipendio_base(self):
        return self._stipendio_base

class ImpiegatoFisso(Impiegato):

    def __init__(self, nome: str, cognome: str, stipendio_base: float):
        super().__init__(nome, cognome, stipendio_base)

    def calcola_stipendio(self):
        return self.__stipendio_base

class ImpiegatoAProvvigione(Impiegato):

    def __init__(self, nome: str, cognome: str, stipendio_base: float, bonus: float):
        super().__init__(nome, cognome, stipendio_base)
        self.__bonus = bonus

    def calcola_stipendio(self):
        return self.__stipendio_base + self.__bonus

    def get_bonus(self):
        return self.__bonus

class GestioneImpiegati:

    def __init__(self, impiegati: list[Impiegato]):
        self.__impiegati = impiegati

    def get_impiegati(self):
        return self.__impiegati

    def aggiung_impiegati(self, impiegato: Impiegato):
        if impiegato.get_nome() not in self.get_impiegati() and impiegato.get_cognome() not in self.get_impiegati():
            self.get_impiegati().append(impiegato)
            print(f"L'impiegato: {impiegato.get_nome()} {impiegato.get_cognome()} è stato aggiunto alla lista")
        else:
            print(f"L'impiegato: {impiegato.get_nome()} {impiegato.get_cognome()} è già presente in lista")

    # def stampa_lista_impiegati(self):
    #     for i, impiegato in enumerate(self.get_impiegati(), 1):
    #         if impiegato.get_bonus():