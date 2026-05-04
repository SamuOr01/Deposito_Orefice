# L' Ereditarietà consente di creare nuove classi a partire da classi esistenti

# Con il metodo super si richiama il costruttore sella superclasse permettendo così
# alla sottoclasse di estendere e modificare il comportamento della superclasse

# La sottoclasse può sovrascrivere i metodi della superclasse per modificare o estendere
# il loro comportamento. Questo è utile quando si vuole che una sottoclasse si comporti
# in modo leggermente diverso rispetto alla superclasse.

# Si parla di ereditarietà singola quando una classe eredita da una sola classe

class Animale:
    def __init__(self, nome):
        self.nome = nome

    def fai_verso(self):
        print(f"{self.nome} fa un verso generico")

# La classe Cane eredita dalla classe Animale
class Cane(Animale):

    def fai_verso(self):
        print(f"{self.nome} sta abbaiando")

class Gatto(Animale):

    def fai_verso(self):
        print(f"{self.nome} sta miagolando")

# Creazione degli oggetti
animale = Animale("Pippo")
cane = Cane("Fido")
gatto = Gatto("Ture")

print(animale.fai_verso())
print(cane.fai_verso())
print(gatto.fai_verso())