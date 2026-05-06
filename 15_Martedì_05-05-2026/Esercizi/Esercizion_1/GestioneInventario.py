class Articolo:

    # Aggiungere, rimuovere e aggiornare articoli (solo admin)
    # Stampa
    def __init__(self, nome: str, prezzo: float):
        self.nome = nome
        self.prezzo = prezzo
        self.quantità_disponibile = 0


class Inventario:

    def aggiungi_articolo(self):
        pass

    def rimuovi_articolo(self):
        pass

    def aggiorna_articolo(self):
        pass