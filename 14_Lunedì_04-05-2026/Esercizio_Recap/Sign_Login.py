# import modulo os
from os import path

# Funzione per registrare l'account
def registrati(path_credenziali, user, password):

    # crea il file delle credenziali
    with open(path_credenziali, "w", encoding="utf-8") as credenziali:
        credenziali.write(f"{user},{password}\n")

# Funzione per accedere all'account
def login(path_credenziali, user, password):

    # Se non esiste lo crea
    if not path_credenziali:
        print("Non sei registrato")
        registrati(path_credenziali, user, password)

    # Se esiste effettua il login
    else:
        with open(path_credenziali, "r", encoding="utf-8") as credenziali:
            for riga in credenziali:
                u, p = riga.strip().split(",")
                if u == user and p == password:
                    return True
        return False