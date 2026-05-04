# Classe
class ContoBancario:

    # Attributi
    def __init__(self, titolare: str, saldo: float):

        # Attributi privati
        self.__titolare = titolare
        self.__saldo = saldo

    # Metodo per depositare denaro sul conto se l'importo è positivo
    def deposita(self, importo: float):
        if importo > 0:
            self.__saldo += importo
            print(f"Hai versato {importo}€, il saldo attuale è {self.__saldo}")
        else:
            print("L'importo che vuoi versare non è valido")

    # metodo per prelevare denaro dal conto se l'importo e il saldo sono positivi
    def preleva(self, importo: float):
        if importo > 0 and self.__saldo >= importo:
            self.__saldo -= importo
            print(f"Hai prelevato {importo}€, il saldo attuale è {self.__saldo}")
        elif importo < 0:
            print("L'importo che vuoi prelevare non è valido")
        else:
            print("Non è possibile prelevare per saldo insufficiente")

    # Metodo per visualizzare il saldo
    def visualizza_saldo(self):
        return self.__saldo

    # Metodi per ottenere e impostare il titolare del conto
    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, titolare: str):
        if titolare != "" and titolare.isalpha():
            self.__titolare = titolare


# main

c_pippo = ContoBancario("Pippo", 0)
c_topolino = ContoBancario("Topolino", 1000)

print("# Conto Di Pippo")
print(c_pippo.get_titolare())
print(c_pippo.visualizza_saldo())
c_pippo.deposita(-5.5)
c_pippo.deposita(50)
c_pippo.preleva(100)
c_pippo.preleva(25)
print(c_pippo.visualizza_saldo())

print()

print("# Conto Di Topolino")
print(c_topolino.get_titolare())
print(c_topolino.visualizza_saldo())
c_topolino.deposita(50)
print(c_topolino.visualizza_saldo())
c_topolino.preleva(100)
print(c_topolino.visualizza_saldo())