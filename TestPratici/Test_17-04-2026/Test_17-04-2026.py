# import dei moduli e delle funzioni necessarie
from math import sqrt


# Funzioni per le operazioni

# Somma
def Addizione(num1, num2):
    print("\nLa somma è:", num1 + num2)

# Differenza
def Sottrazione(num1, num2):
    print("\nLa differenza è:", num1 - num2)

# Prodotto
def Moltiplicazione(num1, num2):
    print("\nIl prodotto è:", num1 * num2)

# Divisione
def Divisione(num1, num2):

    # Il divisore deve essere diverso da zero
    if num2 != 0:
        print("\nIl risultato è:", num1 / num2)
    else:
        print("\nErrore: non è possibile dividere per zero!")

# Radice Quadrata
def Radice_Quadrata(num):

    # Il numero deve essere maggiore o uguale a zero
    if num >= 0:
        print("\nLa radice quadrata è", sqrt(num))
    else:
        print("\nErrore: non è possibile fare la radice quadrata di un numero negativo!")

# Funzioni Menù Sign-Login

# Fare registrazione
def Registrati(lista1, lista2):
    # Inizio ciclo per fare inserire un input valido per lo user
    while True:

        # Richiesta input
        user = input("\nInserisci il tuo username: ")

        #Verifica validità dell'input
        if user in lista1:
            # Non valido = continua il ciclo
            print("\nUn altro utente sta già usando questo username")
            continue
        else:
            # Valido = esce dal ciclo
            break

    # Inizio ciclo per fare inserire un input valido per la password
    while True:

        # Con questo blocco si evitano eccezioni che bloccano l'esecuzione
        try:

            # Richiesta input
            password = input("\nInserisci la password: ")

            #Verifica validità dell'input
            if len(password) < 4 or len(password) > 4 :

                # Non valido = continua il ciclo
                print("\nLa password deve contenere 4 cifre")
                continue

            # Non valido = continua il ciclo
            elif int(password) in lista1:
                print("\nMi dispiace questa password non è valida")
                continue

            # Valido = esce dal ciclo
            else:
                break

        # Cattura le eccezioni e continua il ciclo
        except Exception as e:
            print("\nSi è verificato un errore: ", e)
            print("La password deve contenere 4 cifre")
            continue

    # Aggiunge user e password alla lista
    print("\nAccount creato con successo")
    lista2.append(user)
    lista2.append(int(password))

    # restituisce la lista
    return lista2

# Fase di Login
def Login(lista1, lista2):

    # Ciclo per chiedere le credenziali fino a quando non sono inserite correttamente
    while True:

        # Input di user e password
        user = input("\nInserisci il tuo username: ")
        password = input("\nInserisci la password: ")


        # Controllo username
        if user not in lista1 and user not in lista2:
            print("Username errato, riprova")
            continue

        # Controllo password
        if int(password) not in lista1 and int(password) not in lista2:
            print("Password errata, riprova")
            continue

        # Se le credenziali corrispondono esce dal ciclo
        else:
            print("\nBentornato!", user)
            break

    # Restituisce lo user
    return user



# ----
# Main
# ----

# Dichiarazione Liste degli account
# Una già completa e una vuota per praticità d'esempio
account1 = ["Samu01", 1524]
account2 = []

# Numero massimo di operazioni dell'utente prima di riloggare
max_operazioni = 5

# Menù Sign-Login

# Cicla fino a quando non viene effettuato il Login o la Registrazione
while True:

    # Richiesta all'utente
    sign_login = input(
    '''
        Benvenuto, hai già un account o vuoi registrarti?

        1) Login
        2) Registrati
    ''')

    # Opzioni in base all'input
    match sign_login:

        # Se l'utente sceglie Login
        case "1":
            utente = Login(account1, account2)
            break

        # Se l'utente sceglie Registrati
        case "2":
            account2 = Registrati(account1, account2)
            utente = Login(account1, account2)
            break

        # Altrimenti continua il ciclo
        case _:
            print("\nInput non valido")
            continue

# Ciclo fino a quando il counter arriva a 0
while max_operazioni != 0:

    # Stampa il numero di operazioni rimanenti
    print("\nPuoi fare ancora: ", max_operazioni, "operazioni")

    # Menù di scelta dell'operazione, l'utente deve inserire l'operatore corrispondente
    scelta = input(
    '''\n
        Che operazione vuoi eseguire? (Inserisci l'operatore corrispondente)
        1) Addizione (+)
        2) Sottrazione (-)
        3) Moltiplicazione (*)
        4) Divisione (/)
        5) Radice Quadrata (radice)\n
    ''')

    # se l'utente sceglie la Radice Quadrata chiede un solo input
    if scelta.lower() == "radice":
        num = float(input("\nInserisci un numero: "))

    # Altrimenti chiede 2 input
    else:
        num1 = float(input("\nInserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))

    # Opzioni in base all'input
    match scelta:

        # L'utente ha scelto Addizione e stampa il messaggio
        case "+":
            print("\nHai scelto l'addizione")

            # Chiama la funzione scelta
            Addizione(num1, num2)

            # Decrementa il counter
            max_operazioni -= 1

        # L'utente ha scelto Sottrazione e stampa il messaggio
        case "-":
            print("\nHai scelto la sottrazione")

            # Chiama la funzione scelta
            Sottrazione(num1, num2)

            # Decrementa il counter
            max_operazioni -= 1

        # L'utente ha scelto Moltiplicazione e stampa il messaggio
        case "*":
            print("\nHai scelto la moltiplicazione")

            # Chiama la funzione scelta
            Moltiplicazione(num1, num2)

            # Decrementa il counter
            max_operazioni -= 1

        # L'utente ha scelto Divisione e stampa il messaggio
        case "/":
            print("\nHai scelto la divisione")

            # Chiama la funzione scelta
            Divisione(num1, num2)

            # Decrementa il counter
            max_operazioni -= 1

        # L'utente ha scelto radice Quadrata e stampa il messaggio
        case "radice":
            print("\nHai scelto la radice quadrata")

            # Chiama la funzione scelta
            Radice_Quadrata(num)

            # Decrementa il counter
            max_operazioni -= 1

        # L'utente ha inserito un input non valido e stampa il messaggio
        case _:
            print("\nInput non valido, riprova!")