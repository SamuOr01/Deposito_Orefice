from Utente import Utente
from GestioneInventario import Articolo

class Cliente(Utente):

    def __init__(self, username, password, carrello: dict[Articolo : int]):
        super().__init__(username, password)
        self._carrello = carrello

    # Getter
    def get_carrello(self):
        return self._carrello

    # Azioni
    def aggiungi_al_carrello(self, articolo: Articolo, quantità: int):

        carrello = self._carrello
        if quantità > 0:
            if articolo in carrello.keys():
                carrello[articolo] += quantità
            else:
                carrello[articolo] = quantità
        else:
            print("Errore non puoi aggingere al carrello una quantità negattiva o uguale a 0")

#
class GestioneCliente:

    def registrati(self):
        pass

    def login(self):
        pass