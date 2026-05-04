# L'astrazione serve a separare le operazioni di alto livello da quella di basso livello

# Astrazione Attiva e Passiva

# Attiva: Completamente pratica, in python non esistono le interfacce (Simulazione ereditarietà multipla) perchè non sono necessarie

# Passiva: semplifica l'interazionele con elementi complessi lasciando solamente i dettagli rilevanti ed è quella
# che ci  permette di avere le 3 regole OOP contemporaneamente

# Una classe astratta è una classe che ha metodi astratti (vuoti, non implementati) ma non può essere istanziata.
# Le classi astratte si usano come base per le altre classi

# Possono esserci classi astratte senza metodo astratto, ma non possono esserci metodi astratti senza classi astratte

# Libreria per definire le classi astratte
from abc import ABC, abstractmethod

# Classe Astratta
class Animale(ABC):

    # L'uso del decoratore @abstarctmethod impone alle sottoclassi di definire
    # i metodi astratti della superclasse
    @abstractmethod
    def muovi(self):
        pass

# Classi figlie che implementano il metodo muovi
class Cane(Animale):
    def muovi(self):
        print("Corro")

class Pesce(Animale):
    def muovi(self):
        print("Nuoto")


# Inoltre è possibile definire dei metodi concreti nelle classi astratte rendendo così
# il comportamento base riutilizzabile

from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza

    def area(self):
        return self.larghezza * self.altezza

    def perimetro(self):
        return 2 * (self.larghezza + self.altezza)


# f = Forma() # TypeError: Can't instantiate abstract class Forma

r = Rettangolo(5, 10)
print(r.area()) # Output: 50
print(r.perimetro()) # Output: 30