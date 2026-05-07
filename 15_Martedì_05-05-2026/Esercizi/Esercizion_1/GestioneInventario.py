class Articolo:

    def __init__(self, nome: str, prezzo: float):
        self.nome = nome
        self.prezzo = prezzo
        self.quantità_disponibile = 0


class Inventario:

    def __init__(self):
        self.inventario: dict[str, Articolo] = {}

    def aggiungi_articolo(self, nome: str, quantità: int, prezzo: float):

        if quantità <= 0:
            print("Quantità non valida")
            return

        if nome in self.inventario:
            self.inventario[nome].quantità_disponibile += quantità
        else:
            self.inventario[nome] = Articolo(nome, prezzo)
            self.inventario[nome].quantità_disponibile = quantità

    def rimuovi_articolo(self, nome: str):
        if nome in self.inventario:
            del self.inventario[nome]

    def vendi_articolo(self, nome: str, quantità: int):

        if nome not in self.inventario:
            print("Articolo non esistente")
            return

        if quantità <= 0:
            print("Quantità non valida")
            return

        if self.inventario[nome].quantità_disponibile < quantità:
            print("Stock insufficiente")
            return

        self.inventario[nome].quantità_disponibile -= quantità

    def aggiorna_quantità(self, nome: str, quantità: int):

        if nome in self.inventario and quantità >= 0:
            self.inventario[nome].quantità_disponibile = quantità
        else:
            print("Operazione non valida")

    def visualizza_articoli(self):

        for articolo in self.inventario.values():
            print(f"Articolo: {articolo.nome}, Prezzo: {articolo.prezzo}, Quantità disponibile: {articolo.quantità_disponibile}")