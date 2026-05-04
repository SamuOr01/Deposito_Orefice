# Classe generica
class Persona:

    # Attributi
    def __init__(self, nome: str, età: int):
        # Attributi privati
        self.__nome = nome
        self.__età = età

    # Metodo presentazione
    def presentazione(self):
        return f"Mi chiamo {self.get_nome()}, ho {self.get_età()} anni"

    # Metodo per leggere la variabile privata nome
    def get_nome(self):
        return self.__nome

    # Metodo per assegnare la variabile privata nome
    def set_nome(self, nome: str):
        if nome != "" and nome.isalpha():
            self.__nome = nome

    # Metodo per leggere la variabile privata età
    def get_età(self):
        return self.__età

    # Metodo per assegnare la variabile privata età
    def set_età(self, età: int):
        if età > 0:
            self.__età = età

class Studente(Persona):

    # Attributi
    def __init__(self, nome: str, età: int, voti: list[int]):

        # Attributi del genitore
        super().__init__(nome, età)

        # Attributo del figlio
        self.voti = voti

    # Metodo per calcolare la media
    def calcola_media(self):
        if not self.voti:
            return None
        else:
            return sum(self.voti) / len(self.voti)

    # Override Metodo presentazione
    def presentazione(self):
        media = self.calcola_media()
        if media is None:
            return f"{super().presentazione()} e non ho ancora voti"
        return f"{super().presentazione()} e la mia media dei voti è di {media:.2f}"

class Professore(Persona):

    # Attributi
    def __init__(self, nome: str, età: int, materia: str):

        # Attributi del genitore
        super().__init__(nome, età)

        # Attributo del figlio
        self.materia = materia

    # Override Metodo presentazione
    def presentazione(self):
        return f"{super().presentazione()} e insegno {self.materia.lower()}"


# Main

# Creazione degli oggetti
s = Studente("Maico", 15, [5, 3, 4, 2, 5, 4, 4, 1, 2, 2])
s2 = Studente("Kevini", 15, [])
p = Professore("Pippo", 65, "geostoria")

# Chiamata del metodo
print(s.presentazione())
print(s2.presentazione())
print(p.presentazione())