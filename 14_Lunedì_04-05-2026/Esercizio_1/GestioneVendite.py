class GestioneVendite:
    # Inizializzo l'attributo della lista importi
    def __init__(self, importi: list[float]):
        self.__importi = importi

    # Restituisce il totale degli importi
    def totale_vendite(self):
        return sum(self.__importi)

    # Restituisce la media delle vendite e se sono sopra la media del periodo
    def media_vendite(self):
        somma = self.totale_vendite()
        n_importi = len(self.__importi)

        media = int(somma) / n_importi

        return media
