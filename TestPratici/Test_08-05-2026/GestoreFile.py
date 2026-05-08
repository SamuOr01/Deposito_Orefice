import numpy as np
import os

# Verifica se la cartella "Classi" esiste, altrimenti la crea
if not os.path.exists("Classi"):
    os.makedirs("Classi")

# FUNZIONI PER LA GESTIONE DELLE CLASSI

# Funzione per scrivere i dati nel file
def crea_classe(numero_studenti, nome):
    classe = []

    # Ciclo per inserire i dati di ogni studente
    for i in range(numero_studenti):
        studente = {
            "id": i+1,
            "nome": input(f"Inserisci il nome dello studente {i+1}: "),
            "cognome": input(f"Inserisci il cognome dello studente {i+1}: "),
            "età": int(input(f"Inserisci l'età dello studente {i+1}: ")),
            "classe": nome,
            "media": float(input(f"Inserisci la media dello studente {i+1}: "))
        }

        # Aggiunta dello studente alla lista della classe
        classe.append(studente)

    # Scrittura dei dati nel file
    with open(os.path.join("Classi", f"Classe_{nome}.txt"), "w", encoding="utf-8") as file:

        # Intestazione del file lasciando una riga vuota dopo
        file.write("ID | Nome | Cognome | Età | Classe | Media\n\n")

        # Scrittura dei dati di ogni studente nel file
        for studente in classe:
            file.write(f"{studente['id']} | "
                       f"{studente['nome']} | "
                       f"{studente['cognome']} | "
                       f"{studente['età']} | "
                       f"{studente['classe']} | "
                       f"{studente['media']}\n")

    # Ritorno della classe creata
    return classe

# Funzione per mostrare i dati di una classe a schermo
def mostra_classe(nome):
    classe = []

    # Apertura del file in modalità lettura
    with open(os.path.join("Classi", f"Classe_{nome}.txt"), "r", encoding="utf-8") as file:

        # Lettura dei dati dal file
        righe = file.readlines()

        # Ciclo su ogni riga del file a partire dalla terza (saltando l'intestazione e la riga vuota)
        for riga in righe[2:]:

            # Suddivisione della riga in base al separatore " | "
            dati = riga.strip().split(" | ")

            # Assegnazione dei dati a un dizionario
            studente = {
                "id": dati[0],
                "nome": dati[1],
                "cognome": dati[2],
                "età": int(dati[3]),
                "classe": dati[4],
                "media": float(dati[5])
            }

            # Aggiunta dello studente alla lista della classe
            classe.append(studente)

    # Ritorno della classe letta dal file
    return classe

# Funzione per mostrare tutte le classi disponibili a schermo
def mostra_tutte_classi():

    # Gestione dell'eccezione nel caso in cui la cartella "Classi" non esista
    try:

        # Ciclo su ogni file presente nella cartella "Classi"
        for classe in os.listdir("Classi"):

            # Rimozione della parte "Classe_" e ".txt" dal nome del file per mostrare solo il nome della classe
            nome = classe.replace("Classe_", "").replace(".txt", "")

            # Stampa del nome della classe a schermo
            print("-", nome)

    # Se la cartella "Classi" non esiste, viene stampato un messaggio di errore
    except FileNotFoundError:
        print("La cartella 'Classi' non esiste.")

# Funzione per eliminare una classe
def elimina_classe(nome):

    # Controllo per verificare se il file della classe esiste prima di eliminarlo
    if os.path.exists(os.path.join("Classi", f"Classe_{nome}.txt")):

        # Eliminazione del file della classe
        os.remove(os.path.join("Classi", f"Classe_{nome}.txt"))
        print(f"\nClasse {nome} eliminata con successo.")

    # Se il file della classe non esiste, viene stampato un messaggio di errore
    else:
        print(f"\nClasse {nome} non trovata.")

# Funzione per analizzare una classe e mostrare alcune statistiche a schermo
def analizza_classe(nome):

    # Gestione dell'eccezione nel caso in cui il file della classe non esista
    try:

        # Lettura dei dati della classe dal file
        classe = mostra_classe(nome)

        medie = []

        # Ciclo su ogni studente della classe per estrarre le medie e inserirle in una lista
        for studente in classe:
            medie.append(studente["media"])

        # Conversione della lista delle medie in un array NumPy per facilitare il calcolo delle statistiche
        medie_np = np.array(medie)

        # Stampa delle statistiche a schermo
        print(f"\nANALISI CLASSE {nome}")

        print(f"Numero studenti: {len(medie_np)}")

        print(f"Media generale: {np.mean(medie_np):.2f}")

        print(f"Media più alta: {np.max(medie_np)}")

        print(f"Media più bassa: {np.min(medie_np)}")

    # Se la cartella "Classi" non esiste, viene stampato un messaggio di errore
    except FileNotFoundError:
        print("Classe non trovata.")