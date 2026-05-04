# Classe Per gli input
class InputUtente:

    # Metodo della classe per prendere gli input
    def prendi_input(self):
        print("===Benvenuto===")

        # Ciclo fino a quando non vengono inseriti input validi
        while True:

            # Blocco try per gestire le eccezioni
            try:
                # Prendo gli input separati da spazi
                scelta = input("\nInserisci gli importi separati da uno spazio: ")

                # Trasformo la stringa in una lista di stringhe usando il separatore
                importi = scelta.split(" ")

                # Ciclo su ogni elemento per convertirlo in float
                for i, value in enumerate(importi):
                    importi[i] = float(value)

                # Restituisco la lista
                return importi

            # In caso di errore riprova
            except ValueError as e:

                # Pulisce la lista
                importi.clear()

                # Stampa un messaggio di errore e continua il ciclo
                print(f"Input errato: {e}")
                print("Riprova")
                continue