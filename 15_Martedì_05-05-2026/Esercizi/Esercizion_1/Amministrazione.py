from Utente import Utente
from GestioneInventario import Inventario

class Amministratore(Utente):

    def __init__(self, username, password):
        super().__init__(username, password)

    # 1. Visualizza inventario
    def visualizza_inventario(self, inventario: Inventario):
        inventario.visualizza_articoli()

    # 2. Visualizza vendite
    def visualizza_vendite(self, registro_vendite: list):
        if not registro_vendite:
            print("Nessuna vendita effettuata")
            return

        for vendita in registro_vendite:
            print("\n--- VENDITA ---")
            print(f"\nCliente: {vendita['cliente']}")
            print(f"\nArticoli: {vendita['articoli']}")
            print(f"\nTotale: €{vendita['totale']}")

    # 3. Visualizza guadagni totali
    def visualizza_guadagni(self, totale_guadagni: float):
        print(f"Guadagni totali: €{totale_guadagni}")

    def aggiungi_articolo(self, inventario, nome, prezzo, quantità):
        inventario.aggiungi_articolo(nome, quantità, prezzo)
        print(f"{nome} aggiunto/aggiornato")

    def rimuovi_articolo(self, inventario, nome):
        inventario.rimuovi_articolo(nome)
        print(f"{nome} rimosso dall'inventario")

    def aggiorna_quantità(self, inventario, nome, quantità):
        inventario.aggiorna_quantità(nome, quantità)
        print(f"{nome} aggiornato a {quantità}")