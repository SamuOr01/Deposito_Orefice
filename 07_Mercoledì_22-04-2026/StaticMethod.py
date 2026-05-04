# I metodi statici sono funzioni legate alla classe ma che non operano ne sull'istanza ne sulla classe
# non richiedono dunque i parametri self o cls

class Calcolatrice:

    # Si definiscono con il decoratore @staticmethod
    @staticmethod
    def somma(a, b):
        return a + b

# Può essere chiamato sia treamite l'istanza che tramite la classe
risultato = Calcolatrice.somma(5, 3)

print(risultato) # Output: 8