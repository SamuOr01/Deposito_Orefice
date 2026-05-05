# I Moduli sono file che contengono variabili, funzioni o classi
# che possono essere importati in altri script Python

# Permettono di organizzare il codice in modo da migliorarne
# la modularità, la leggibilità e manutenibilità

# Esistono anche molti moduli standard di Python disponibili, che forniscono
# funzionalità predefinite, come ad esempio il modulo math per le operazioni
# matematiche o il modulo datetime per la manipolazione delle date e degli orari.

def saluta(nome):
    print("Ciao, ", nome)

PI = 3.14159

class Cerchio:

    def __init__(self, raggio):
        self.raggio = raggio

    def area(self): return PI * self.raggio**2