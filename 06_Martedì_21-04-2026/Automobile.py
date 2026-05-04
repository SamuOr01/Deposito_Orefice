# Le classi consentono di definire strutture
# che raggruppano dati (attrubuti) e comportamenti (metodi)

# Si usano per la creazione degli oggetti,
# istanze delle classi con le sue proprietà uniche

# Le classi possono essere annidate, ovvero possono avere
# al suo interno altre classi

# Si definiscono con la parola class
class Automobile:
    # Gli attributi sono variabili associate alla classe,
    # rappresentano le proprietà degli oggetti e sono condivisi tra di essi

    # Attributo di classe
    numero_ruote = 4

    # Il costruttore è un metodo speciale che viene invocato automaticamente
    # al momento della creazione di un nuovo oggetto, impostando attributi e valori iniziali.

    # __init__ accetta sempre almeno il parametro self (riferimento all'oggetto)

    # I metodi sono funzioni definite all'interno di una classe
    # che operano sugli oggetti (le istanze) della classe stessa.

    # Metodo Costruttore
    def __init__(self, marca, modello):
        # Attributo di istanza
        self.marca = marca
        # Attributo di istanza
        self.modello = modello

    # Metodo di istanza
    def stampa_info(self):
        print(f"L'automobile è una {self.marca} {self.modello}")


# # creazione o istanzazione degli oggetti della classe Automobile
# auto1 = Automobile("Nissan", "Juke")
# auto2 = Automobile("Fiat", "Panda")
# auto3 = Automobile("Fiat", "Punto")

# # stampa "L'automobile è una Nissan Juke"
# auto1.stampa_info()
# # stampa "L'automobile è una Fiat Panda"
# auto2.stampa_info()
# # stampa "L'automobile è una Fiat Punto"
# auto3.stampa_info()

# # Alle variabili e attributi di istanza
# # posso accedere come variabili normali
# auto1.marca = "Mercedez"
# auto1.modello = "Classe A"

# # stampa "L'automobile è una Mercedez Classe A"
# auto1.stampa_info()