from Utente import Utente
from GestioneInventario import Inventario

class Cliente(Utente):

    def __init__(self, username, password, carrello: dict[str : int]):
        super().__init__(username, password)
        self._carrello = carrello

    # Getter
    def get_carrello(self):
        return self._carrello

    # Azioni
    def aggiungi_al_carrello(self, articolo: str, quantità: int):

        carrello = self._carrello
        if quantità > 0:
            if articolo in carrello.keys():
                carrello[articolo] += quantità
            else:
                carrello[articolo] = quantità
        else:
            print("Errore non puoi aggingere al carrello una quantità negattiva o uguale a 0")

    def checkout(self, inventario, registro_vendite, totale_guadagni):

        carrello = self._carrello

        if not carrello:
            print("Carrello vuoto")
            return totale_guadagni

        totale = 0

        # 1. controllo disponibilità
        for nome, quantità in carrello.items():

            if nome not in inventario.inventario:
                print(f"Articolo {nome} non presente")
                return totale_guadagni

            articolo = inventario.inventario[nome]

            if quantità > articolo.quantità_disponibile:
                print(f"Stock insufficiente per {nome}")
                return totale_guadagni

        # 2. esegui acquisto
        for nome, quantità in carrello.items():

            articolo = inventario.inventario[nome]

            inventario.sottrai_articolo(nome, quantità)

            totale += articolo.prezzo * quantità

        # 3. salva vendita
        vendita = {
            "cliente": self.get_username(),
            "articoli": carrello.copy(),
            "totale": totale
        }

        registro_vendite.append(vendita)
        totale_guadagni += totale

        # 4. ricevuta
        print("\n--- RICEVUTA ---")
        for nome, quantità in carrello.items():
            prezzo = inventario.inventario[nome].prezzo
            print(f"{nome} x{quantità} = €{prezzo * quantità}")

        print(f"TOTALI: €{totale}")
        print("Acquisto completato")

        # 5. svuota carrello
        self._carrello.clear()

        return totale_guadagni