# Import della funzione uniform per generare numeri float casuali
from random import uniform

# Classe padre Metodo di pagamento
class MetodoPagamento:

# Metodo per effettuare un pagamento
    def effettua_pagamento(self, importo: float):
        print(f"Ha pagato {importo}€")

# Classe figlia per i pagamenti con carta di credito
class CartaDiCredito(MetodoPagamento):

# Override del metodo di pagamento con applicazione di una commissione del 2%
    def effettua_pagamento(self, importo: float):
        imposta = (importo * 2) / 100
        totale = importo + imposta
        print(f"Ha pagato {importo:.2f}€ con il 2% di imposta, totale = {totale:.2f}€")

# Classe figlia per i pagamenti con Paypal
class Paypal(MetodoPagamento):

# Override del metodo di pagamento senza commissioni aggiuntive
    def effettua_pagamento(self, importo: float):
        print(f"Ha pagato {importo:.2f}€ istantaneamente")

# Classe figlia per i pagamenti con Bonifico Bancario
class Bonifico(MetodoPagamento):

# Override del metodo con commissione del 3% e tempi di accredito più lunghi
    def effettua_pagamento(self, importo: float):
        imposta = (importo * 3) / 100
        totale = importo + imposta
        print(f"Ha pagato {importo:.2f}€ con il 3% di imposta, totale = {totale:.2f}€, il pagamento verrà accreditato entro 3 giorni lavorativi")

# Classe che gestisce i pagamenti
class GestorePagamenti:

# Controlla se il credito è sufficiente e avvia il pagamento
    def scegli_pagamento(metodo: MetodoPagamento, credito: float, importo: float):
        if importo <= credito:
            metodo.effettua_pagamento(importo)
        else:
            print("Mi dispiace credito insufficiente")

# Funzione che simula l'interazione con l'utente
def utente():
    credito = uniform(1, 100)
    print(f"Il tuo credito è di {credito:.2f}€\n")
    nome = input("Inserisci nome: ")
    cognome = input("Inserisci cognome: ")
    prezzo = uniform(1, 100)

    print(f"Sig. {nome} {cognome}, lei paga {prezzo:.2f}€")

    while True:
        metodo = input(
                        "\nCome desidera pagare?"
                        "\n1) Carta"
                        "\n2) Paypal"
                        "\n3) Bonifico\n\n"
                    )

        match metodo:
            case "1":
                return CartaDiCredito(), credito, prezzo
            case "2":
                return Paypal(), credito, prezzo
            case "3":
                return Bonifico(), credito, prezzo
            case _:
                print("Input non valido, riprova")


# Main

# Avvia la procedura utente e recupera metodo, credito e importo
metodo, credito, importo = utente()

# Esegue il pagamento tramite il gestore
GestorePagamenti.scegli_pagamento(metodo, credito, importo)