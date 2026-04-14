# Il programma chiede all'utente se possiede già un account
has_account = input("Possiedi già un account? (S/N): ")

# Se l'utente non possiede un account, lo crea
if has_account.upper() == "N":
    # Dichiarazione lista contenente le informazioni dell'account
    account = []
    # Creazione di username e password per l'account
    user = input("Inserisci un username: ")
    password = input("Inserisci una password: ")
    # Il programma genera un ID univoco per l'account
    id = 5020
    # Aggiunge alla lista le credenziali dell'account
    account.append(user)
    account.append(password)
    account.append(id)
    # Stampa il risultato dell'operazione
    print("Account creato con successo!")
    print("Il tuo ID è:", id)
    print("Benvenuto", user)
    print(account)

# Se l'utente possiede già un account, lo fa accedere
else:
    # Dichiarazione lista contenente le informazioni dell'account esistente
    account = ["Samu01", "Python01", 5020]
    user = input("Inserisci il tuo username: ")

    # Con un if annidato controlla che le credenziali inserite corrispondano a quelle presenti nella lista
    if account[0] == user:
        password = input("Inserisci la tua password: ")
        if account[1] == password:
            id = input("Inserisci il tuo ID: ")
            if account[2] == int(id):
                print("Accesso riuscito!")
                print("Benvenuto", user)

    # Se le credenziali non corrispondono, stampa un messaggio di errore
    else:
        print("Si è verificato un errore, riprova!")