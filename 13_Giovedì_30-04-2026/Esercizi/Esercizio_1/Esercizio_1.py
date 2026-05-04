# Import della funzione path del modulo os
from os import path

# Funzione per la prenotazione
def prenota(codice_fiscale, nome, cognome, tipo, data, ora):

    # Creo il percorso del file della prenotazione del paziente
    path_prenotazione = f"{folder_path}\\Prenotazione_{codice_fiscale.upper()}.txt"

    # Apro il file in scrittura e salvo i dati della prenotazione
    with open(path_prenotazione, "w") as prenotazione:
        dettagli_prenotazione = f"{nome} - {cognome} - {codice_fiscale} - {tipo} - {data} - {ora}"
        prenotazione.write(dettagli_prenotazione)

    # Stampo la conferma della prenotazione
    print(dettagli_prenotazione)

# Funzione per la modifica della prenotazione
def modifica(codice_fiscale):

    # Creo il percorso del file della prenotazione del paziente
    path_prenotazione = f"{folder_path}\\Prenotazione_{codice_fiscale.upper()}.txt"

    # Controllo che la prenotazione esista
    if not path.exists(path_prenotazione):
        print("\nPrenotazione non trovata!")
        return

    # Leggo i dati della prenotazione dal file
    with open(path_prenotazione, "r") as prenotazione:
        dati = prenotazione.readline().strip()

    # Divido i dati nei vari campi
    campi = dati.split(" - ")

    # Chiedo all’utente cosa vuole modificare
    scelte = input("\nCosa vuoi modificare?"
                   "1) Nome"
                   "2) Cognome"
                   "3) Tipo visita"
                   "4) Data"
                   "5) Ora"
                   "Inserisci numeri separati da virgola (es: 1,4,5): "
                )
    # Permetto modifiche multiple separate da virgola
    scelte = scelte.split(",")

    # Aggiorno solo i campi selezionati
    for scelta in scelte:
        scelta = scelta.strip()

        match scelta:
            case "1":
                campi[0] = input("Nuovo nome: ")
            case "2":
                campi[1] = input("Nuovo cognome: ")
            case "3":
                campi[3] = input("Nuovo tipo visita: ")
            case "4":
                campi[4] = input("Nuova data: ")
            case "5":
                campi[5] = input("Nuova ora: ")
            case _:
                print(f"Scelta non valida: {scelta}")

    # Ricostruisco la stringa aggiornata
    nuovi_dati = " - ".join(campi)

    # Sovrascrivo il file con i nuovi dati
    with open(path_prenotazione, "w") as prenotazione:
        prenotazione.write(nuovi_dati)

    print("\nPrenotazione aggiornata:")
    print(nuovi_dati)

# Funzione per l'accettazione del paziente
def accettazione(codice_fiscale):

    # Creo il percorso del file della prenotazione del paziente
    path_prenotazione = f"{folder_path}\\Prenotazione_{codice_fiscale.upper()}.txt"

    # Controllo che la prenotazione esista
    if not path.exists(path_prenotazione):
        print("\nPrenotazione non trovata!")
        return
    # Leggo i dati della prenotazione
    with open(path_prenotazione, "r") as prenotazione:
        dati = prenotazione.readline().strip()

    # Controllo se il paziente è già stato accettato
    if "ACCETTATA" in dati:
        print("\nPaziente già accettato.")
        return

    # Aggiorno lo stato della prenotazione
    nuovi_dati = dati + " - ACCETTATA"

    # Salvo l’aggiornamento nel file
    with open(path_prenotazione, "w") as prenotazione:
        prenotazione.write(nuovi_dati)

    print("\nAccettazione completata:")
    print(nuovi_dati)
    print("\nSi accomodi in sala d'attesa.")



# Main

# Percorso della cartella
folder_path = "13_Giovedì_30-04-2026\\Esercizi\\Esercizio_1"

print("Benvenuto")

# Ciclo
while True:

    # Input dell'utente
    scelta = input(
            "\nCosa deve fare?"
            "\n1) Prenotare una visita"
            "\n2) Modificare una prenotazione"
            "\n3) Accettazione"
            "\n4) Esci\n\n"
            )

    # Gestione delle scelte dell'utente
    match scelta:
        # Prenotazione
        case "1":
            codice_fiscale = input("\nInserisca il codice fiscale ")
            nome = input("Inserisca il nome ")
            cognome = input("Inserisca il cognome ")
            tipo = input("Che tipo di visita deve fare? ")
            data = input("Inserisca la data ")
            ora = input("Inserisca l'ora ")

            prenota(codice_fiscale, nome, cognome, tipo, data, ora)

        # Modifica prenotazione
        case "2":
            codice_fiscale = input("\nInserisca il codice fiscale ")

            modifica(codice_fiscale)

        # Accettazione
        case "3":
            codice_fiscale = input("\nInserisca il codice fiscale ")

            accettazione(codice_fiscale)

        # Esci
        case "4":
            print("\nArrivederci")
            break

        # Input non valido
        case _:
            print("\nInput non vallido, riprova")
            continue