# Creazione del menù
scelta = input(
'''
    Quale parte del programma vuoi eseguire?
    1) Utilizzo di if
    2) Utilizzo di while e range()
    3) Utilizzo di for
    4) Utilizzo di if, while e for insieme\n
''')

# Gestione delle scelte
match scelta:
    # Scelta = 1
    case "1":
        # Punto 1: Utilizzo di if

        # Input dell'utente
        numero = int(input("\nInserisci un numero: "))

        # Verifica se il modulo del numero diviso 2 è zero, si tratta di un numero è pari, altrimenti è dispari
        if numero % 2 == 0:
            print(numero, "è un numero pari")
        else:
            print(numero, "è un numero dispari")

    # Scelta = 2
    case "2":
        # Punto 2: Utilizzo di While e Range()

        print("\nConto alla rovescia\n")

        # Variabile booleana di controllo per il ciclo while
        esegui = True

        # Finchè il valore è True il ciclo sarà eseguito all'infinito
        while esegui:
            # input dell'utente per iniziare il conto alla rovescia
            n = int(input("Da quale numero vuoi iniziare? "))

            # Stampa riga vuota per migliorare laleggibilità della console
            print()

            # Se l'input è maggiore di zero, esegue il ciclo for che parte dal numero inserito e arriva fino a zero,
            # decrementando di 1 ad ogni iterazione
            if n > 0:
                for i in range(n, -1, -1):
                    print(i)

            # Chiediamo all'utente se vuole eseguire un altro conto alla rovescia
            scelta = input("\nVuoi riprovare? (s/n) ")
            # Se l'utente risponde 'n', la variabile di controllo viene impostata a False, interrompendo il ciclo while
            if scelta.lower() == 'n':
                esegui = False

    # Scelta = 3
    case "3":
        # Punto 3: Utilizzo di For

        # Creazione di una lista vuota per immagazzinare i numeri inseriti dall'utente
        numeri = []

        # Chiediamo all'utente quanti numeri vuole inserire così da poter impostare il range del ciclo
        len_lista = int(input("\nQuanti numeri vuoi inserire? "))

        # Il ciclo chiede all'utente di inserire un numero che viene aggiunto alla lista
        for i in range(len_lista):
            numero = int(input("Inserisci un numero: "))
            numeri.append(numero)

        # Stampa riga vuota per migliorare laleggibilità della console
        print()

        # Per ogni numero nella lista, stampa il numero e il suo quadrato
        for n in numeri:
            print(n, "-->", n ** 2)

    # Scelta = 4
    case "4":
        # Punto 4: Utilizzo di If While e For insieme

        # Creazione di una lista di numeri (puoi anche lasciarla vuota per testare il caso in cui la lista è vuota)
        # numeri = []
        numeri = [6, 74, 66, 100, 30]

        # Se la lista non è vuota
        if len(numeri) != 0:
            # Trova il numero massimo
            massimo = 0
            for n in numeri:
                if n > massimo:
                    massimo = n

            # Conta il numero di elementi nella lista
            conteggio_lista = 1

            while conteggio_lista < len(numeri):
                conteggio_lista += 1

            # Stampa il numero massimo e il numero di elementi nella lista
            print("\nIl numero massimo è:", massimo)
            print("il numero di elementi nella lista è:", conteggio_lista)
        else:
            # Se la lista è vuota, stampa un messaggio
            print("lista Vuota")

    #  Se la scelta dell'utente non corrisponde a nessuno dei casi precedenti
    case _:
        # Stampa un messaggio di errore
        print("Scelta non valida, riprova!")