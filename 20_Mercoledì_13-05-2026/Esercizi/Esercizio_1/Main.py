import numpy as np
from Functions import (
    crea_matrice,
    estrai_sotto_matrice_centrale,
    matrice_trasposta,
    determinante_matrice_quadrata,
    matrice_inversa,
    applica_funzione_matematica,
    filtra_elementi_matrice,
    check_matrice,
    salva_txt
)

# Menù
print("Benvenuto!")

# Inizializzazione Matrice e Parametri globali
matrice = None
params = None

# Inizio Loop
while True:

    # Input menù
    scelta = input("\nChe operazione vuoi eseguire?"
                   "\n1) Creazione matrice 2D"
                   "\n2) Estrai sotto-matrice"
                   "\n3) Matrice Trasposta"
                   "\n4) Somma elementi della matrice"
                   "\n5) Prodotto elemento per elemento delle matrici"
                   "\n6) Media elementi della matrice"
                   "\n7) Determinante matrice quadrata"
                   "\n8) Calcolare matrice inversa (se quadrata e invertibile)"
                   "\n9) Applicare funzioni matematiche alla matrice"
                   "\n10) Filtrare elementi della matrice"
                   "\n11) Esci"
                   "\n\n> "
                )

    match scelta:

        # Punto 1.1
        case "1":
            print("\nHai scelto di creare una matrice")

            # Ciclo interno fino a quando non vengono inseriti input corrretti
            while True:

                # Prova a chiedere l'input
                try:

                    # Input dei parametri
                    i_range = int(input("\nInserisci il range iniziale della matrice: "))
                    f_range = int(input("Inserisci il range finale della matrice: "))
                    dim1 = int(input("Inserisci la prima dimensione della matrice: "))
                    dim2 = int(input("Inserisci la seconda dimensione della matrice: "))

                # Se va in eccezione riprova
                except ValueError:
                    print("\nNon hai inserito il valore corretto, riprova")
                    continue

                # Se non ci sono errori esce dal ciclo interno
                else:
                    break

            try:
                # Creazione matrice
                matrice = crea_matrice(i_range, f_range, dim1, dim2)

            # Se va in eccezione riprova
            except ValueError as e:
                print(f"Errore: {e}")
                continue

            # Memorizzo i parametri
            params = (i_range, f_range, dim1, dim2)

            # Stampa la matrice
            descrizione = (f"Matrice {matrice.shape}: \n\n{matrice}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 1.2
        case "2":

            # Verifica esistenza della matrice
            if not check_matrice(matrice):
                continue

            # Estrazione sotto-matrice centrale
            sotto_matrice = estrai_sotto_matrice_centrale(matrice)

            # Verifica esistenza sotto-matrice
            if sotto_matrice is None:
                print("Matrice troppo piccola")
                continue

            # Stampa la sotto-matrice centrale
            descrizione = (f"\nSotto-Matrice centrale {sotto_matrice.shape}: \n\n{sotto_matrice}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 1.3
        case "3":

            # Verifica esistenza della matrice
            if not check_matrice(matrice):
                continue

            # Creazione matrice trasposta
            trasposta = matrice_trasposta(matrice)

            # Stampa la matrice trasposta
            descrizione = (f"\nMatrice Trasposta {trasposta.shape}: \n\n{trasposta}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 1.4
        case "4":

            # Verifica esistenza della matrice
            if not check_matrice(matrice):
                continue

            # Calcolo della somma degli elementi della matrice
            somma = np.sum(matrice)

            # Stampa la somma
            descrizione = (f"\nLa somma degli elementi della matrice {matrice.shape}: {somma}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 2.1
        case "5":

            # Verifica esistenza della matrice
            if not check_matrice(matrice):
                continue

            # Verifica esistenza dei parametri
            if params is None:
                print("Devi prima creare la matrice")
                continue

            # Recupera i parametri precedentemente memorizzati
            i_range, f_range, dim1, dim2 = params

            # Creazione seconda matrice
            matrice2 = crea_matrice(i_range, f_range, dim1, dim2)

            # Verifica che le matrici abbiano la stessa shape
            if matrice.shape != matrice2.shape:
                print("Le matrici devono avere stessa shape")
                continue

            # Prodotto tra le due matrici
            prodotto = np.multiply(matrice, matrice2)

            # Stampa il prodotto elemento per elemento delle matrici
            descrizione = (f"\nIl prodotto degli elementi delle matrici {matrice.shape}: \n\n{prodotto}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 2.2
        case "6":

            # Verifica esistenza della matrice
            if not check_matrice(matrice):
                continue

            # Calcolo della media degli elementi della matrice
            media = np.mean(matrice)

            # Stampa la media
            descrizione = (f"\nLa media degli elementi della matrice {matrice.shape}: {media}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 2.3
        case "7":

            # Verifica esistenza della matrice
            if not check_matrice(matrice):
                continue

            # Calcolo del determinante solo se la matrice è quadrata
            determinante = determinante_matrice_quadrata(matrice)

            # Verifica l'esistenza del determinante
            if determinante is None:
                print("La matrice non è quadrata")
                continue

            # Stampa il determinante della matrice
            descrizione = (f"\nIl determinante della matrice {matrice.shape}: {determinante}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 3.1
        case "8":

            # Verifica esistenza della matrice
            if not check_matrice(matrice):
                continue

            # Calcolo della matrice inversa solo se la matrice è quadrata e invertibile
            inversa = matrice_inversa(matrice)

            # Verifica esistenza della matrice inversa
            if inversa is None:
                print("La matrice non è quadrata o non è invertibile")
                continue

            # Stampa la matrice inversa
            descrizione = (f"\nMatrice Inversa {inversa.shape}: \n\n{inversa}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 3.2
        case "9":

            # Verifica esistenza della matrice
            if not check_matrice(matrice):
                continue

            # Input utente per la scelta della funzione matematica
            while True:
                scelta_funzione = input(
                    "\nScegli funzione:"
                    "\n1) SENO"
                    "\n2) COSENO"
                    "\n3) ESPONENZIALE"
                    "\n4) LOGARITMO"
                    "\n\n> "
                )


                match scelta_funzione:
                    case "1":
                        funzione = "sin"
                    case "2":
                        funzione = "cos"
                    case "3":
                        funzione = "exp"
                    case "4":
                        funzione = "log"
                    case _:
                        print("Input non valido")
                        continue

                # Controllo valori per il logaritmo
                if funzione == "log" and np.any(matrice <= 0):
                    print("Logaritmo non valido con valori <= 0")
                    continue

                # Applico la funzione
                risultato = applica_funzione_matematica(matrice, funzione)
                break

            # Stampo il risultato
            descrizione = (f"\nRisultato della funzione {funzione} applicata alla matrice {matrice.shape}:\n\n{risultato}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 3.3
        case "10":

            # Verifica esistenza della matrice
            if not check_matrice(matrice):
                continue

            # Input per la soglia del filtro
            try:
                soglia = int(input("\nInserisci la soglia per filtrare gli elementi della matrice: "))
            except ValueError:
                print("Input non valido")
                continue

            # Filtra gli elementi della matrice in base alla soglia
            elementi_filtrati = filtra_elementi_matrice(matrice, soglia)

            # Stampa gli elementi filtrati
            descrizione = (f"\nElementi della matrice {matrice.shape} maggiori di {soglia}: \n\n{elementi_filtrati}")
            print(f"\n{descrizione}")

            # Salva i dati nel txt
            salva_txt(descrizione)

        # Punto 1.5
        case "11":
            # Esce dal programma
            print("\nArrivederci!")
            break

        # Input non valido
        case _:
            # Riprova
            print("\nInput non valido, riprova")
            continue

# Verificare il salvataggio nel txt