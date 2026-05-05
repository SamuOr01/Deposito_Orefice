class GestioneVendite:
    # Inizializzo l'attributo della lista importi
    def __init__(self, importi: list[float]):
        self.__importi = importi

    # Restituisce il totale degli importi
    def totale_vendite(self):
        return sum(self.__importi)

    # Restituisce la media delle vendite
    def media_vendite(self):
        somma = self.totale_vendite()
        n_importi = len(self.__importi)

        # Non necessario un controllo per divisore != da 0
        # poichè il programma impedisce input vuoti
        media = somma / n_importi

        # Restituisce la media
        return media

    # Funzione per le vendite sopra la media
    def vendite_sopra_la_media(self):

        # Lista vuota
        lista_sopra_media = []

        # Prendo il valore della media
        media = self.media_vendite()

        # Ciclo su ogni elemento della lista
        for value in self.__importi:

            # Se il valore è maggiore della media, lo aggiunge alla lista
            if value > media:
                lista_sopra_media.append(value)

        # Se nella lista ci sono valori sopra la media, la restituisce
        if len(lista_sopra_media) > 0:
            return lista_sopra_media

        # Se nella lista non ci sono valori sopra la media, stampa il messaggio e la restituisce
        else:
            print("Nessuna vendita sopra la media")
            return lista_sopra_media