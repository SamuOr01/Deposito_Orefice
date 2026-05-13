import numpy as np
from numpy import random

path_folder = "Deposito_Orefice\\19_Martedì_12-05-2026\\Esercizi_Recap\\Esercizio_5"

# Ciclo per rendere ripetibile il programma
while True:

    print("Generazione Dati...")

    # Punto 1

    # Creo un un array di 50 numeri equidistanti tra 0 e 10
    array_eq = np.linspace(0, 10, 50)

    # Stampo l'array
    print(f"\nArray di 50 numeri equidistanti tra 0 e 10:\n\n{array_eq}")


    # Punto 2

    # Creo un array di 50 numeri casuali compresi tra 0 e 1
    array_random = random.rand(50)

    # Stampo l'array
    print(f"\nArray di 50 numeri casuali compresi tra 0 e 1:\n\n{array_random}")


    # Punto 3

    # Somma dei due array elemento per elemento per ottenere un nuovo array
    sum_array = np.add(array_eq, array_random)

    # Stampo la somma
    print(f"\nSomma dei due array elemento per elemento per ottenere un nuovo array:\n\n{sum_array}")


    # Punto 4

    # Somma totale degli elementi del nuovo array
    somma = np.sum(sum_array)

    # Stampo la somma
    print(f"\nSomma totale degli elementi del nuovo array: {somma}")


    # Punto 5

    # Somma degli elementi del nuovo array che sono maggiori di 5
    somma_maggiori_5 = np.sum(sum_array[sum_array > 5])

    # Stampo la somma
    print(f"\nSomma degli elementi del nuovo array che sono maggiori di 5: {somma_maggiori_5}")


    while True:

        # Scelta dell'utente per salvare i dati nel txt
        scelta = input("\nVuoi salvare i dati? (S/N)"
                       "\n\n> "
                       )

        # Verifica della scelta
        match scelta.upper():

            # Se la scelta è Sì
            case "S":

                # Scrive i dati nel file txt
                with open(f"{path_folder}\\Dati.txt", "w", encoding="utf-8") as file:
                    file.write(f"Array di 50 numeri equidistanti tra 0 e 10:\n\n{array_eq}")
                    file.write(f"\n\nArray di 50 numeri casuali compresi tra 0 e 1:\n\n{array_random}")
                    file.write(f"\n\nSomma dei due array elemento per elemento per ottenere un nuovo array:\n\n{sum_array}")
                    file.write(f"\n\nSomma totale degli elementi del nuovo array: {somma}")
                    file.write(f"\n\nSomma degli elementi del nuovo array che sono maggiori di 5: {somma_maggiori_5}")

                # esce dal ciclo
                print("\nDati salvati con successo!")
                print("\nOperazione Conclusa")
                break

            # Se la scelta è No
            case "N":

                # Esce dal ciclo
                print("\nOperazione Conclusa")
                break

            # Scelta non valida
            case _:

                # Riprova
                print("\nInput non valido, riprova")
                continue


    while True:

        # Scelta dell'utente per ripetere le operazioni
        scelta_2 = input("\nVuoi continuare? (S/N)"
                         "\n\n> "
                         )

        # Verifica della scelta
        match scelta_2.upper():

            # Se la scelta è Sì
            case "S":

                # Ripete il ciclo esterno
                break

            # Se la scelta è No
            case "N":

                # Esce dal programma
                print("\nArrivederci")
                exit()

            # Scelta non valida
            case _:

                # Riprova
                print("\nInput non valido, riprova")
                continue