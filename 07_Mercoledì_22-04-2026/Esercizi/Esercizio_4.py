# Classe Prodotto
class Prodotto:

    # Costruttore con attributi delle istanze
    def __init__(self, nome, costo_produzione, prezzo_vendita):

        # Inizializzazione degli attributi negli oggetti
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    # # Diciamo a Python come rappresentare l’oggetto quando lo stampiamo
    def __repr__(self):
        return self.nome

    # Metodo che calcola il guadagno di una vendita e lo stampa
    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        print(f"Dalla sua vendita è stato generato un profitto di {profitto}€")

# Classe Elettrodomestico che eredita da Prodotto
class Elettrodomestico(Prodotto):

    # Costruttore con attributi del genitore e i propri
    def __init__(self, nome, costo_produzione, prezzo_vendita, classe_energetica, garanzia):

        # Inizializza gli attributi del genitore
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)

        # Inizializzazione dei suoi attributi
        self.classe_energetica = classe_energetica
        self.garanzia = garanzia

    # Metodo che stampa le caratteristiche dell'istanza
    def mostra_info(self):
        print(f"{self.nome} appartiene alla classe energetica {self.classe_energetica} ed ha una garanzia di {self.garanzia} anni")

# Classe Abbigliamento che eredita da Prodotto
class Abbigliamento(Prodotto):

    # Costruttore con attributi del genitore e i propri
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale, colore):

        # Inizializza gli attributi del genitore
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)

        # Inizializzazione dei suoi attributi
        self.materiale = materiale
        self.colore = colore

    # Metodo che stampa le caratteristiche dell'istanza
    def mostra_info(self):
        print(f"{self.nome} è fatto di {self.materiale} ed è di colore {self.colore}")

# Classe Fabbrica per gestire l'inventario e le vendite
class Fabbrica:

    # Costruttore con attributi delle istanze
    def __init__(self, inventario: dict[Prodotto, int]):

        # Inizializzazione dell'attributo
        self.inventario = inventario

    # Metodo che aggiunge prodotti all’inventario
    def aggiungi_prodotto(self, prodotto: Prodotto, numero: int):

        # Prende la quantità attuale (0 se non esiste)
        quantità_iniziale = self.inventario.get(prodotto, 0)

        # Somma la nuova quantità
        quantità_finale = quantità_iniziale + numero

        # Aggiorna il dizionario
        self.inventario.update({prodotto : quantità_finale})

    # Metodo per la vendita dei prodotti
    def vendi_prodotto(self, prodotto: Prodotto, numero: int):

        # Prende la quantità attuale (0 se non esiste)
        quantità_iniziale = self.inventario.get(prodotto, 0)

        # Controlla se ci sono abbastanza prodotti
        if quantità_iniziale > 0 and quantità_iniziale >= numero:

            # Sottrae i prodotti venduti
            quantità_finale = quantità_iniziale - numero

            # Aggiorna il dizionario
            self.inventario.update({prodotto : quantità_finale})

            # Calcola e stampa profitto della vendita
            prodotto.calcola_profitto()

        # Se non ci sono abbastanza prodotti, errore
        else:
            print("Prodotto non disponibile")

    # Metodo per i resi
    def resi_prodotto(self, prodotto: Prodotto, numero: int):

        # Prende la quantità attuale (0 se non esiste)
        quantità_iniziale = self.inventario.get(prodotto, 0)

        # Somma la nuova quantità
        quantità_finale = quantità_iniziale + numero

        # Aggiorna il dizionario
        self.inventario.update({prodotto : quantità_finale})


# Main

# Creazione degli oggetti e stampa delle caratteristiche
frigorifero = Elettrodomestico("Frigorifero LG", 400, 650, "A++", 5)
frigorifero.mostra_info()

lavatrice = Elettrodomestico("Lavatrice Samsung", 350, 600, "A+++", 4)
lavatrice.mostra_info()

maglietta = Abbigliamento("Maglietta Nike", 10, 25, "cotone", "nero")
maglietta.mostra_info()

jeans = Abbigliamento("Jeans Levi's", 30, 80, "denim", "blu navy")
jeans.mostra_info()

# Creazione Fabbrica con inventario vuoto
magazzino = Fabbrica({})

# Aggiunta dei prodotti nel magazzino
magazzino.aggiungi_prodotto(frigorifero, 10)
magazzino.aggiungi_prodotto(lavatrice, 5)
magazzino.aggiungi_prodotto(maglietta, 20)
magazzino.aggiungi_prodotto(jeans, 15)

# Check sull'inventario
print(f"""
      Il magazzino è stato riempito di prodotti nuovi di zecca:
      {(magazzino.inventario)}
      """)

# Vendita dei prodotti
magazzino.vendi_prodotto(frigorifero, 2)
magazzino.vendi_prodotto(lavatrice, 1)
magazzino.vendi_prodotto(maglietta, 5)
magazzino.vendi_prodotto(jeans, 3)

# # Check sull'inventario
print(f"""
      Dopo la vendita il magazzino contiene:
      {magazzino.inventario}
      """)

# Reso dei prodotti
magazzino.resi_prodotto(maglietta, 1)
magazzino.resi_prodotto(jeans, 2)

# Check sull'inventario
print(f"""
      Sono stati effettuati dei resi, adesso il magazzino contiene:
      {magazzino.inventario}
      """)