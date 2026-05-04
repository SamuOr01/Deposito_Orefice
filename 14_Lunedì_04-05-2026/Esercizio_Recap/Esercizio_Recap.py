# import modulo os
from os import path

# Funzione per registrare l'account
def registrati(path_credenziali,user, password):

    with open(path_credenziali, "w") as credenziali:
        credenziali.write(f"USERNAME: {user}"
                          f"PASSWORD: {password}"
                        )

# Funzione per accedere all'account
def login(path_credenziali, user, password):
    pass

# Funzione per aggiungere lo studente alla lista csv
def aggiungi(nome, cognome, età, data_nascita, corso):
    pass

# Funzione per modificare lo studente dalla lista csv
def modifica(nome, cognome, età, data_nascita, corso):
    pass

# Funzione o classe per l'admin


# Main

folder_path = "14_Lunedì_04-05-2026\\Esercizio_Recap"

# path_credenziali = (f"{folder_path}\\{user}.txt")
