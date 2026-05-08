import os

# FUNZIONI PER LA GESTIONE DELLE CLASSI

# Funzione per scrivere i dati nel file
def crea_classe(numero_studenti, nome):
    classe = []
    for i in range(numero_studenti):
        studente = {
            "id": i+1,
            "nome": input(f"Inserisci il nome dello studente {i+1}: "),
            "cognome": input(f"Inserisci il cognome dello studente {i+1}: "),
            "età": input(f"Inserisci l'età dello studente {i+1}: "),
            "classe": nome,
            "media": input(f"Inserisci la media dello studente {i+1}: ")
        }
        classe.append(studente)

    with open(f"Classi\\Classe_{nome}.txt", "w", encoding="utf-8") as file:
        for studente in classe:
            file.write(f"{studente['id']},{studente['nome']},{studente['cognome']},{studente['età']},{studente['classe']},{studente['media']}\n")

    return classe

# Funzione per leggere i dati dal file
def mostra_classe(nome):
    classe = []
    with open(f"Classi\\Classe_{nome}.txt", "r", encoding="utf-8") as file:
        righe = file.readlines()

        for riga in righe:
            dati = riga.strip().split(",")

            studente = {
                "id": dati[0],
                "nome": dati[1],
                "cognome": dati[2],
                "età": dati[3],
                "classe": dati[4],
                "media": dati[5]
            }

            classe.append(studente)

    return classe

def elimina_classe(nome):
    if os.path.exists(f"Classi\\Classe_{nome}.txt"):
        os.remove(f"Classi\\Classe_{nome}.txt")
        print(f"\nClasse {nome} eliminata con successo.")
    else:
        print(f"\nClasse {nome} non trovata.")

# FUNZIONI PER LA GESTIONE DEGLI STUDENTI