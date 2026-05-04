# Il polimorfismo permette di trattare oggetti di classi diverse utilizzando un'interfaccia comune.

# Si può manifestare in due modi:

# Override dei metodi - ovvero la sovrascrittura dei metodi della superclasse da parte delle sottoclassi implementando e modificando
# il comporportamento già definito nella superclasse

class Origine:

    def lavoro():
        print("Sto lavorando")

class Lavoratore_Manuale(Origine):

    def lavoro():
        print("Sto cementando")

class Lavoratore_Digitale(Origine):

    def lavoro():
        print("Sto programmando")

class Lavoratore_Nullafacente(Origine):

    def lavoro():
        print("Non sto lavorando")

def fai_lavorare(lavoratore: Origine):
    lavoratore.lavoro()


# Simulazione Overloading - Python non supporta l'overloading, ovvero la possibilità di avere
# più metodi con lo stesso nome ma differenti parametri all'interno della stessa classe, come gli altri linguaggi,
# tuttavia è possibile simularlo utilizzando:
# - argomenti opzionali (se non viene passato il valore del parametro, prende quello di default)
# - variadici (*args: una tupla con un numero variabile di parametri)

class Stampa:

    def mostra(self, a = None, b = None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None:
            print(a)
        else:
            print("Niente da mostrare")

m1 = Stampa()
m2 = Stampa()
m3 = Stampa()

m1.mostra(5, 6)
m2.mostra(69)
m3.mostra()


# Il polimorfismo passivo in Python si basa principalmente sul concetto di
# Duck Typing, non è necessario che un oggetto appartenga gerarchia specifica,
# l'importante è che si comporti come ci si aspetta, ovvero possedere gli attributi
# e/o metodi necessari

class Cerchio:

    def disegna(self):
        print("Disegno un cerchio")

class Rettangolo:

    def disegna(self):
        print("Disegno un rettangolo")

# Basta che 'figura' abbia il metodo 'disegna' per sfruttare il Duck Typing
def disegna_figura(figura):
    figura.disegna()

figure = [Cerchio(), Rettangolo()]

for figura in figure:
    disegna_figura(figura)