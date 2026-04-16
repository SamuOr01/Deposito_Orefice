# Import dei moduli random e math per usare le funzioni randint e sqrt
from random import randint
from math import sqrt

# Punto 1

# Inizializzazione funzione
def Numero_Positivo():
    # creazione del loop
    while True:
        # Input dell'utente
        numero = int(input("\nInserisci un numero positivo "))

        # Se il numero è positivo
        if numero > 0:

            # Stampa il messaggio
            print("\n",numero, "è un numero positivo")

            # Restituisce il numero ed esce dalla funzione
            return numero

        # Se il numero è 0 o è negativo continua il ciclo
        elif numero == 0:
            print("\nHai inserito 0")
            continue
        else:
            print("\n",numero, "è un numero negativo")
            continue

# Punto 2

# Inizializzazione funzione
def Lista_Casuale_Di_Interi(limite):
    # Se il limite è None chiede di usare la funzione 1 per usare quel valore come limite del range
    if not limite:
        print("\nPer poter usare questa funzione devi prima usare il comando 1")
        return

    # inizializzazione di una lista vuota
    numeri = []

    # Cicla per il numero di iterazioni imposte dal limite
    for _ in range(limite):

        # Assegno un valore intero casuale da aggiungere alla lista
        numero = randint(1, limite)
        numeri.append(numero)

    # stampo e restituisco la lista
    print("\n",numeri)
    return numeri

# Punto 3

# Inizializzazione funzione
def Somma_Numeri_Pari(lista):
    # Se la lista non esiste chiede di usare la funzione 2 per crearla
    if not lista:
        print("\nPer poter usare questa funzione devi prima usare il comando 2")
        return

    # Inizializziamo le variabili della somma e della lista dei numeri pari
    somma_pari = 0
    lista_pari = []

    # Cicliamo per ogni numero della lista
    for numero in lista:
        # Se è pari: lo aggiungiamo alla lista e sommiamo
        if numero % 2 == 0:
            lista_pari.append(numero)
            somma_pari += numero

    #Stampo i risultati
    print("\nI numeri pari sono:", lista_pari)
    print("La somma dei numeri pari presenti nella lista è:", somma_pari)

# Punto 4

# Inizializzazione funzione
def Stampa_Numeri_Dispari(lista):
    # Se la lista non esiste chiede di usare la funzione 2 per crearla
    if not lista:
        print("\nPer poter usare questa funzione devi prima usare il comando 2")
        return

    # Inizializzo la lista dei numeri dispari
    lista_dispari = []

    # Cicliamo per ogni numero della lista
    for numero in lista:

        # Se è dispari: lo aggiungiamo alla lista
        if numero % 2 != 0:
            lista_dispari.append(numero)

    # Stampiamo la lista
    print("\nI numeri dispari sono:", lista_dispari)

# Punto 5

# Inizializzazione funzione
def È_Primo(numero):

    # Se il numero è minore di 2
    if numero < 2:
        # La funzione restituisce False
        return False

    # Il ciclo for controlla se esiste un divisore tra 2 e la radice quadrata del numero.
    # +1 perchè lo stop del range è escluso
    for i in range(2, int(sqrt(numero)) + 1):

        # Se trova divisori, il numero non è primo
        if numero % i == 0:
            # La funzione restituisce False
            return False

    # Altrimenti il numero è primo e la funzione restituisce True
    return True

# Punto 6

# Inizializzazione funzione
def Stampa_Numeri_Primi(lista):
    # Se la lista non esiste chiede di usare la funzione 2 per crearla
    if not lista:
        print("\nPer poter usare questa funzione devi prima usare il comando 2")
        return

    # Stampiamo messaggio
    print("\nI numeri primi presenti nella lista sono:")

    # Cicliamo per ogni numero della lista
    for numero in lista:

        # Richiamiamo la funzione di verifica
        if È_Primo(numero):

            # Se è primo lo stampiamo
            print(numero)

# Punto 7

# Inizializzazione funzione
def Somma_Numeri_Lista(lista):
    # Se la lista non esiste chiede di usare la funzione 2 per crearla
    if not lista:
        print("\nPer poter usare questa funzione devi prima usare il comando 2")
        return

    # Inizializziamo la variabile della somma
    somma = 0

    # Cicliamo per ogni numero della lista
    for numero in lista:

        # Aggiorniamo il valore della somma
        somma += numero

    # Stampiamo il valore della somma
    print("\nLa somma dei numeri presenti nella lista è:", somma)

    # Verifichiamo che sia un numero primo
    if È_Primo(somma):
        print("\nLa somma è un numero primo")
    else:
        print("\nLa somma non è un numero primo")

# Punto 8 - Menù

# Inizializziamo le varibili del limite e della lista da passare come parametri iniziali
limite = None
lista = []

# Ciclo infinito per il menù
while True:

    # Visualizzazione del menù e richiesta input
    scelta = input(
    '''
        Quale funzione vuoi eseguire?

        1) Numero Positivo
        2) Lista casuale di interi
        3) Somma numeri pari
        4) Lista numeri dispari
        5) Verifica numero primo
        6) Lista Numeri primi
        7) Somma numero primo
        8) Esci dal programma\n
    ''')

    # Verifica dell'input
    match scelta:

        # Chiamata della funzione 1 e immagazzinamento del valore int restituito
        case "1":
            limite = Numero_Positivo()

        # Chiamata della funzione 2 con parametro lista e immagazzinamento del valore list restituito
        case "2":
            lista = Lista_Casuale_Di_Interi(limite)

        # Chiamata della funzione 3 con parametro lista
        case "3":
            Somma_Numeri_Pari(lista)

        # Chiamata della funzione 4 con parametro lista
        case "4":
            Stampa_Numeri_Dispari(lista)

        # Chiamata della funzione 5 con parametro input
        case "5":
            numero = int(input("\nInserisci un numero da verificare: "))

            # Verifica del valore booleano restituito
            if È_Primo(numero):
                # Se è True il numero è primo e viene stampato un messaggio
                print("\nIl numero", numero, "è primo.")
            else:
                # Se è False il numero non è primo e viene stampato un messaggio
                print("\nIl numero", numero, "non è primo.")

        # Chiamata della funzione 6 con parametro lista
        case "6":
            Stampa_Numeri_Primi(lista)

        # Chiamata della funzione 7 con parametro lista
        case "7":
            Somma_Numeri_Lista(lista)

        # Per uscire da ciclo e chiudere il programma
        case "8":
            break

        # Input non valido, continuo il ciclo
        case _:
            print("Comando errato!")
            continue