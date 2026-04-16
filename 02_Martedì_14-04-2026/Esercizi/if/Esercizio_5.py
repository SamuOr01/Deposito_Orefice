print("Benvenuto nella calcolatrice di Python!")

# Il programma chide all'utente di inserire due numeri che verranno convertiti in float
num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))

# Menù di scelta dell'operazione, l'utente deve inserire l'operatore corrispondente
scelta = input(
'''Che operazione vuoi eseguire? (Inserisci l'operatore corrispondente)
    1) Addizione (+)
    2) Sottrazione (-)
    3) Moltiplicazione (*)
    4) Divisione (/)\n
''')

match scelta:
    case "+":
        print("Hai scelto l'addizione")
        print("Il risultato di ", num1, "+", num2, "è:", num1 + num2)
    case "-":
        print("Hai scelto la sottrazione")
        print("Il risultato di ", num1, "-", num2, "è:", num1 - num2)
    case "*":
        print("Hai scelto la moltiplicazione")
        print("Il risultato di ", num1, "*", num2, "è:", num1 * num2)
    case "/":
        print("Hai scelto la divisione")
        if num2 != 0:
            print("Il risultato di ", num1, "/", num2, "è:", num1 / num2)
        else:
            print("Errore: non è possibile dividere per zero!")
    case _:
        print("Operazione non valida, riprova!")