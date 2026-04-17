# import dei moduli e delle funzioni necessarie
from math import sqrt


# Funzioni per le operazioni

def Addizione(num1, num2):
    print("La somma è:", num1 + num2)

def Sottrazione(num1, num2):
    print("La differenza è:", num1 - num2)

def Moltiplicazione(num1, num2):
    print("Il prodotto è:", num1 * num2)

def Divisione(num1, num2):
    if num2 != 0:
            print("Il risultato è:", num1 / num2)
    else:
            print("Errore: non è possibile dividere per zero!")

def Radice_Quadrata(num1, num2):
    print("La radice quadrata di", num1, "è", sqrt(num1))
    print("La radice quadrata di", num1, "è", sqrt(num2))

# Funzioni Menù Sign-Login


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
        try:
            password = input("\nInserisci la password: ")

            if len(password) < 4 or len(password) > 4 :
                print("\nLa password deve contenere 4 cifre")
                continue
            elif int(password) in lista1:
                print("\nMi dispiace questa password non è valida")
                continue
            else:
                break
        except Exception as e:
            print("\nSi è verificato un errore: ", e)
            print("La password deve contenere 4 cifre")
            continue

    print("\nAccount creato con successo")
    lista2.append(user)
    lista2.append(int(password))

    return lista2


def Login(lista1, lista2):
    while True:

        user = input("\nInserisci il tuo username: ")
        password = input("\nInserisci la password: ")
        if user not in lista1:
            if user not in lista2:
                print("Username errato, riprova")
                continue
        elif int(password) not in lista1:
            if int(password) not in lista2:
                print("Password errata, riprova")
                continue
        else:
            print("Bentornato!", user)
            break

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

while True:

    # Richiesta all'utente
    sign_login = input(
    '''
        Benvenuto, hai già un account o vuoi registrarti?

        1) Login
        2) Registrati
    ''')

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

        case _:
            print("\nInput non valido")
            continue

num1 = float(input("\nInserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))

while max_operazioni != 0:
    # Stampa il numero di operazioni rimanenti
    print("Puoi fare ancora: ", max_operazioni, "operazioni")

    # Menù di scelta dell'operazione, l'utente deve inserire l'operatore corrispondente
    scelta = input(
    '''\n
        Che operazione vuoi eseguire? (Inserisci l'operatore corrispondente)
        1) Addizione (+)
        2) Sottrazione (-)
        3) Moltiplicazione (*)
        4) Divisione (/)
        5) Radice Quadrata\n
    ''')

    match scelta:
        case "+":
            print("\nHai scelto l'addizione")
            Addizione(num1, num2)
            max_operazioni -= 1
        case "-":
            print("\nHai scelto la sottrazione")
            Sottrazione(num1, num2)
            max_operazioni -= 1
        case "*":
            print("\nHai scelto la moltiplicazione")
            Moltiplicazione(num1, num2)
            max_operazioni -= 1
        case "/":
            print("\nHai scelto la divisione")
            Divisione(num1, num2)
            max_operazioni -= 1
        case "radice":
            print("\nHai scelto la radice quadrata")
            Radice_Quadrata(num1, num2)
            max_operazioni -= 1
        case _:
            print("\nOperazione non valida, riprova!")