class Convertitore:

    # Metodi statici
    @staticmethod

    # euro in dollari
    def euro_in_dollari(importo_euro):
        tasso_cambio = 1.08
        # moltiplico l'importo in euro per il tasso
        importo_dollaro = importo_euro * tasso_cambio
        return float(importo_dollaro)

    @staticmethod
    # km in miglia
    def km_in_miglia(km):
        fattore_fisso = 0.621371
        #moltiplico i km per il fattore
        miglia = km * fattore_fisso
        return float(miglia)

# Stampo i risultati chiamando i metodi senza creare istanze
print(f"15€ sono {Convertitore.euro_in_dollari(15):.2f}$")

print(f"15 km sono {Convertitore.km_in_miglia(15)} miglia")