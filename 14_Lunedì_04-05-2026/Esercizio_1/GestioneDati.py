# import modulo datetime
from datetime import datetime

# Metodo per verificare che la data sia nel formato corretto
def formatta_data(data):
    data_formattata = datetime.strptime(data, "%d/%m/%Y")
    return data_formattata


# Metodo della classe per prendere gli input
def prendi_input():
    print("===Benvenuto===")

    # Ciclo fino a quando non vengono inseriti input validi
    while True:

        # Blocco try per gestire le eccezioni
        try:

            # Prendo in input la data nel formato corretto
            data = input("Inserisci la data di vendita (formato gg/mm/aaaa): ")
            data_date = formatta_data(data)
            break

        # In caso di errore riprova
        except ValueError as e:

            # Stampa un messaggio di errore e continua il ciclo
            print(f"Input errato: {e}")
            print("Riprova")
            continue


    # Ciclo fino a quando non vengono inseriti input validi
    while True:

        # Blocco try per gestire le eccezioni
        try:

            # Prendo gli input separati da spazi
            scelta = input("\nInserisci gli importi separati da uno spazio:"
                            "\n(es. 150.50 15 20.75)\n\n"
                            )

            # Trasformo la stringa in una lista di stringhe usando il separatore
            importi = scelta.split()

            # Verifica che la lista non sia vuota
            if not importi:

                # Solleva l'eccezione per entrare nel blocco except
                raise ValueError("Non hai inserito alcun input")

            # Ciclo su ogni elemento per convertirlo in float
            for i, value in enumerate(importi):
                importi[i] = float(value)

            # Restituisco la lista e la data in formato stringa
            data_stringa = datetime.strftime(data_date, "%d/%m/%Y")
            return data_stringa, importi

        # In caso di errore riprova
        except ValueError as e:

            # Stampa un messaggio di errore e continua il ciclo
            print(f"Input errato: {e}")
            print("Riprova")
            continue