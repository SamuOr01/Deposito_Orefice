from random import randint

# Creazione menù con richiesta input
scelta_menù = input(
'''
    Quale programma vuoi usare?

    1) Number Akinator
    2) Sequenza di Fibonacci\n
''')

# Opzioni in base all'input
match scelta_menù:
    # Case 1
    case "1":
        print("\nBenvenuto su Number Akinator")
        # Viene generato un numero casuale tra 1 e 100 (inclusi)
        numero = randint(1, 100)

        # loop infinito fino a quando il numero viene indovinato
        while True:
            # Tentativo dell'utente
            scelta = int(input("\nA quale numero sto pensando? "))

            # Se indovina esce dal ciclo con break
            if scelta == numero:
                print("Complimenti! Hai indovinato!")
                print("Stavo pensando proprio al numero:", scelta)
                break

            # Altrimenti Il gioco continua
            else:
                print("Mi dispiace hai sbagliato!\n")

                # richiesta di voler continuare oppure no a giocare
                # altrimenti c'è il rischio che il programma non finisca
                scelta_2 = input("Vuoi continuare a provare? (s/n) ")

                if scelta_2.lower() == "n":
                    print("\nA presto")
                    break
                else:
                    continue

    # Case 2
    case "2":
        # Richiesta di input del valore con cui concluedere la sequenza
        scelta = int(input("Inserisci un numero con il quale terminare la sequenza di Fibonacci: "))

        # Inizializzazione dei primi 2 numeri della sequenza
        primo_numero = 0
        secondo_numero = 1

        # Stampa dei primi 2 numeri della sequenza
        print(primo_numero)
        print(secondo_numero)

        # Loop per stampare la sequenza di fibonacci dove ogni numero è la somma dei due precedenti
        while True:
                # Esegue la somma dei 2 numeri
                somma = primo_numero + secondo_numero

                # Se la somma è minore del valore dell'input continua la sequenza
                if somma < scelta:
                    print(somma)

                    # assegnamo i nuovi valori alle variabili per continuare la sequenza
                    primo_numero = secondo_numero
                    secondo_numero = somma

                # Altrimenti esce dal ciclo
                else:
                    break