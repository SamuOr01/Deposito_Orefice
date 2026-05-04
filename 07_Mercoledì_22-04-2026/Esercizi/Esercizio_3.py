# Classe padre Animale
class Animale:

    # Inizializzazione attributi
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    # Metodi per il verso e stampare l'età
    def fai_suono(self):
        print(f"{self.nome} emette un suono generico")

    def stampa_età(self):
        print(f"Ha {self.età} anni di vita")

# Classe Leone figlia di Animale
class Leone(Animale):

    # Override del metodo
    def fai_suono(self):
        print(f"\n{self.nome} ruggisce")

    # Metodo specifico per la caccia del leone
    def caccia(self):
        print("Caccia le gazzelle")

# Classe Giraffa figlia di Animale
class Giraffa(Animale):

    # Override del metodo
    def fai_suono(self):
        print(f"\nNon so che verso faccia {self.nome}")

    # Metodo specifico per la giraffa
    def collo_alto(self):
        print("Grazie al suo collo alto può mangiare le foglie degli alberi più alti")
        print("e può scorgere i pericoli in lontanaza")

# Classe Pinguino figlia di Animale
class Pinguino(Animale):

    # Override del metodo
    def fai_suono(self):
        print(f"\n{self.nome} fa il verso di Pingu")

    # Metodo specifico per il pinguino
    def pesca(self):
        print("Pesca i pesci")


# Creazione oggetto Leone e utilizzo dei suoi metodi
leone = Leone("Leone", 10)
leone.fai_suono()
leone.stampa_età()
leone.caccia()

# Creazione oggetto Giraffa e utilizzo dei suoi metodi
giraffa = Giraffa("Giraffa", 5)
giraffa.fai_suono()
giraffa.stampa_età()
giraffa.collo_alto()

# Creazione oggetto Pinguino e utilizzo dei suoi metodi
pinguino = Pinguino("Pinguino", 5)
pinguino.fai_suono()
pinguino.stampa_età()
pinguino.pesca()