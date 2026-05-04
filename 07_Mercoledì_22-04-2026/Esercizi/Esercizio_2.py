class Animale:

    # inizializzo attributo di classe
    numero_animali = 0

    # attributi nome e specie
    def __init__(self, nome: str, specie: str):
        self.nome = nome
        self.specie = specie
        # incremento dell'attributo di classe dentro il costruttore
        Animale.numero_animali += 1

    # metodo di classe
    @classmethod
    # Nei classmethods cls si riferisce alla classe come self si riferisce alla classe nei costruttori
    def quanti_animali(cls):
        # stampo il totale
        print(f"Numero di animali creati: {cls.numero_animali}")

# Creazione oggetti
a1 = Animale("Pippo", "Montone")
print(f"\n{a1.nome} il {a1.specie}")

a2 = Animale("Pina", "Mucca")
print(f"\n{a2.nome} la {a2.specie}")

a3 = Animale("Tina", "Pecora")
print(f"\n{a3.nome} la {a3.specie}")

a4 = Animale("Rocco", "Toro")
print(f"\n{a4.nome} il {a4.specie}")

a5 = Animale("Melo", "Barbagianni")
print(f"\n{a5.nome} il {a5.specie}\n")

# richiamo il metodo dalla classe e non dalle istanze
Animale.quanti_animali()