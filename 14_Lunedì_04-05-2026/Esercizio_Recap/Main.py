from Sign_Login import registrati, login
from Studenti import aggiungi_studente, stampa_aula
from Utente import Admin


# Main

# Path
folder_path = "Deposito_Orefice\\14_Lunedì_04-05-2026\\Esercizio_Recap"
file_credenziali = f"{folder_path}\\Credenziali.txt"
file_csv = f"{folder_path}\\Studenti.csv"
file_log = f"{folder_path}\\Log.txt"

# Creazione Admin
admin = Admin()

while True:

    # Input Accesso
    scelta = input("\nCosa desideri fare?"
                   "\n1. Registrati"
                   "\n2. Login"
                   "\n3. Esci\n\n"
                )

    match scelta:
        # Registrazione
        case "1":
            user = input("Username: ")
            password = input("Password: ")
            registrati(file_credenziali, user, password)

        # Login
        case "2":
            user = input("Username: ")
            password = input("Password: ")

            # ADMIN
            if user == "admin" and password == "admin":

                while True:

                    # Input Menu Admin
                    scelta2 = input("\n--- ADMIN MENU ---"
                              "\n1. Aggiungi studente"
                              "\n2. Stampa aula"
                              "\n3. Reset studenti"
                              "\n4. Logout\n\n"
                            )

                    match scelta2:

                        # Aggiunta dello studente
                        case"1":
                            nome = input("Nome: ")
                            cognome = input("Cognome: ")
                            eta = input("Età: ")
                            data_nascita = input("Data nascita: ")
                            corso = input("Corso: ")
                            aggiungi_studente(file_csv, nome, cognome, eta, data_nascita, corso)

                        # Stampa dell'aula
                        case "2":
                            stampa_aula(file_csv)

                        # Reset studente
                        case "3":
                            motivo = input("Motivo reset: ")
                            admin.reset_studenti(file_csv, file_log, motivo)

                        # Uscita
                        case "4":
                            break

                        # Input non valido
                        case _:
                            print("Input non valido, riprova")
                            continue

            # UTENTE NORMALE
            elif login(file_credenziali, user, password):

                # Input utente
                while True:


                    scelta3 = input("\n--- MENU UTENTE ---"
                                    "1. Aggiungi studente"
                                    "2. Stampa aula"
                                    "3. Logout")

                    match scelta3:

                        # Aggiunta dello studente
                        case "1":
                            nome = input("Nome: ")
                            cognome = input("Cognome: ")
                            eta = input("Età: ")
                            data_nascita = input("Data nascita: ")
                            corso = input("Corso: ")
                            aggiungi_studente(file_csv, nome, cognome, eta, data_nascita, corso)

                        # Stampa dell'aula
                        case "2":
                            stampa_aula(file_csv)

                        # Uscita
                        case "3":
                            break

                        # Input non valido
                        case _:
                            print("Input non valido, riprova")
                            continue

            else:
                print("Credenziali errate")

        # Uscita
        case "3":
            break

        # Input non valido
        case _:
            print("Input non valido, riprova")
            continue