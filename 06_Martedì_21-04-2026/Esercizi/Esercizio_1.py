# Importiamo il modulo math per la funzione sqrt
from math import sqrt

# definiamo la classe Punto
class Punto:

    # Metodo init e attributi
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Metodo per lo spostamento delle cordinate
    def muovi(self):

        #input delle nuove coordinate
        dx = int(input("Inserisci lo spostamento della coordinata x: "))
        dy = int(input("Inserisci lo spostamento della coordinata y: "))

        # Assegnazione dei nuovi valori
        self.x = dx
        self.y = dy

        # Stampa dei nuovi valori
        print(f"Le nuove coordinate del punto sono: ({self.x}, {self.y})")

    # Metodo per il calcolo della distanza del punto dall'origine
    def distanza_da_origine(self):

        # Stampiamo il risultato del teorema di pitagora
        print(f"{sqrt((self.x ** 2) + (self.y ** 2)):.3f}")

# Creazione dell'oggetto e chiamata dei suoi metodi
p1 = Punto(5, 4)
p1.distanza_da_origine()
p1.muovi()
p1.distanza_da_origine()