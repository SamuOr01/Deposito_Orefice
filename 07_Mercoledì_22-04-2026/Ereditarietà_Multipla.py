# Si parla di ereditarietà multipla quando una classe eredita da più classi

class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_info(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class Dotazioni_Speciali:
    def __init__(self, dotazioni: list[str]):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")

# La classe Auto_Sportiva eredita sia da Veicolo che da Dotazioni_Speciali
class Auto_Sportiva(Veicolo, Dotazioni_Speciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        # Alternativa a super per l'ereditarietà multipla
        Veicolo.__init__(self, marca, modello)
        Dotazioni_Speciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_info(self):
        # Chiamiamo il metodo della prima superclasse
        super().mostra_info()
        print(f"Potenza: {self.cavalli}")
        # Possiamo chiamare metodi di entrambe le superclassi
        self.mostra_dotazioni()

# Creazione dell'oggetto
auto_sportiva = Auto_Sportiva("Ferrari", "F8", ["ABS", "Controllo Trazione", "Airbag Laterali"], 720)
auto_sportiva.mostra_info()