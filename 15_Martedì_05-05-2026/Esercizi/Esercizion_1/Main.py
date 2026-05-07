from GestioneClienti import Cliente
from Amministrazione import Amministratore
from GestioneInventario import Inventario
from GestoreFile import salva_dati, carica_dati, salva_utenti, carica_utenti


# Carica dati salvati
registro_vendite, totale_guadagni = carica_dati()

# Carica utenti salvati
utenti = carica_utenti()

# Creazione inventario e articoli
inventario = Inventario()

inventario.aggiungi_articolo("latte", 10, 1.5)
inventario.aggiungi_articolo("pane", 5, 1.0)
inventario.aggiungi_articolo("pasta", 8, 2.0)


# Creazione admin
admin = Amministratore("admin", "admin")

# Carica utenti salvati
utenti = carica_utenti()


# Sign up
def registrazione():
    print("\n--- REGISTRAZIONE ---")

    username = input("Scegli username: ")
    password = input("Scegli password: ")

    if username in utenti:
        print("Utente già esistente")
        return None

    utenti[username] = {
        "password": password,
        "ruolo": "cliente"
    }

    salva_utenti(utenti)

    print("Registrazione completata!")
    return username

# Login
def login():

    # Input credenziali
    username = input("Username: ")
    password = input("Password: ")

    # Verifica credenziali
    if username == admin.get_username() and password == admin.get_password():
        return "admin", admin

    if username in utenti:
            dati = utenti[username]

            if dati["password"] == password:
                return dati["ruolo"], username

    # Se credenziali errate, chiedi se vogliono registrarsi
    print("Sembra che tu non abbia un account, creane uno!")
    nuovo = registrazione()
    return "cliente", nuovo


# Menu Cliente
def menu_cliente(cliente):

    # Variabile globale per tenere traccia dei guadagni totali
    global totale_guadagni

    # Loop del menu cliente
    while True:

        # Input scelta cliente
        scelta = input("\n--- CLIENTE ---"
                       "\n1. Visualizza inventario"
                       "\n2. Aggiungi al carrello"
                       "\n3. Checkout"
                       "\n4. Logout"
                       "\n\n> ")

        match scelta:

            # Inventario
            case "1":
                # Richiama il metodo visualizza_articoli dell'inventario
                inventario.visualizza_articoli()

            # Carrello
            case "2":
                # Input articolo e quantità per chiamare il metodo aggiungi_al_carrello del cliente
                nome = input("Articolo: ")
                quantita = int(input("Quantità: "))
                cliente.aggiungi_al_carrello(nome, quantita)

            # Checkout
            case "3":
                # Chiama il metodo checkout del cliente, passando inventario, registro vendite e totale guadagni
                totale_guadagni = cliente.checkout(
                    inventario,
                    registro_vendite,
                    totale_guadagni
                )

                # Salva dati dopo ogni checkout
                salva_dati(registro_vendite, totale_guadagni)

            # Logout
            case "4":
                # Salva dati prima di uscire
                salva_dati(registro_vendite, totale_guadagni)
                break

            # Scelta non valida
            case _:

                # Stampa messaggio di errore e continua il loop
                print("Scelta non valida")
                continue


# Menu Admin
def menu_admin(admin):

    # Loop del menu admin
    while True:

        # Input scelta admin
        scelta = input("\n--- ADMIN ---"
                       "\n1. Visualizza inventario"
                       "\n2. Aggiungi / Restock articolo"
                       "\n3. Rimuovi articolo"
                       "\n4. Aggiorna quantità articolo"
                       "\n5. Visualizza vendite"
                       "\n6. Visualizza guadagni"
                       "\n7. Logout"
                       "\n\n> ")

        match scelta:

            # Inventario
            case "1":

                # Richiama il metodo visualizza_inventario dell'admin, passando l'inventario
                admin.visualizza_inventario(inventario)

            # Aggiungi / Restock articolo
            case "2":

                # Input nome, prezzo e quantità per chiamare il metodo aggiungi_articolo dell'admin,
                # passando inventario, nome, prezzo e quantità
                nome = input("Nome articolo: ")
                prezzo = float(input("Prezzo: ").replace(",", "."))
                quantità = int(input("Quantità: "))
                admin.aggiungi_articolo(inventario, nome, prezzo, quantità)

            # Rimuovi articolo
            case "3":

                # Input nome per chiamare il metodo rimuovi_articolo dell'admin, passando inventario e nome
                nome = input("Nome articolo: ")
                admin.rimuovi_articolo(inventario, nome)


            # Aggiorna quantità articolo
            case "4":

                # Input nome e nuova quantità per chiamare il metodo aggiorna_quantità dell'admin, passando
                # inventario, nome e quantità
                nome = input("Nome articolo: ")
                quantità = int(input("Nuova quantità: "))
                admin.aggiorna_quantità(inventario, nome, quantità)

            # Vendite
            case "5":

                # Richiama il metodo visualizza_vendite dell'admin, passando il registro vendite
                admin.visualizza_vendite(registro_vendite)

            # Guadagni
            case "6":

                # Richiama il metodo visualizza_guadagni dell'admin, passando il totale guadagni
                admin.visualizza_guadagni(totale_guadagni)

            # Logout
            case "7":

                # Salva dati prima di uscire
                salva_dati(registro_vendite, totale_guadagni)
                break

            # Scelta non valida
            case _:

                # Stampa messaggio di errore e continua il loop
                print("Scelta non valida")
                continue


# Loop principale
while True:

    # Input scelta menu principale
    scelta = input("\n===== MENU ====="
                   "\n1. Login"
                   "\n2. Registrazione"
                   "\n3. Esci"
                   "\n\n> ")

    match scelta:

        # Login
        case "1":

            # Chiama la funzione login e salva il ruolo e l'utente restituiti
            ruolo, username = login()

            # Se il login ha successo, mostra il menu corrispondente al ruolo
            if ruolo == "cliente":
                cliente = Cliente(username, utenti[username]["password"], {})
                menu_cliente(cliente)
            elif ruolo == "admin":
                menu_admin(username)

        # Registrazione
        case "2":

            # Chiama la funzione registrazione e salva l'utente restituito
            registrazione()

        # Esci
        case "3":

            # Salva dati prima di uscire
            salva_dati(registro_vendite, totale_guadagni)
            break

        # Scelta non valida
        case _:

            # Stampa messaggio di errore e continua il loop
            print("Scelta non valida")
            continue