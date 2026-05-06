import numpy as np
from numpy import random

folder_path = "Deposito_Orefice\\16_Mercoledì_06-05-2026\\Esercizi\\Esercizio_2"
file_name = "SLICING_F-INDEXING.txt"
with open(f"{folder_path}\\{file_name}", "w", encoding="utf-8") as file:

    # Punto 1

    # Creo un array con 20 numeri casuali compresi tra 10 e 50
    # e lo stampo sul file txt
    array_int = random.randint(10, 50, size = 20)
    file.write(f"{array_int}")


    # Punto 2

    # Stampo i primi 10 elementi sul file txt
    file.write(f"\n\nPrimi 10 elementi: {array_int[:10]}")


    # Punto 3

    # Stampo gli ultimi 5 elementi sul file txt
    file.write(f"\n\nUltimi 5 elementi: {array_int[-5:]}")

    # Punto 4

    # Stampo gli elementi dall'indice 5 all'indice 15 (escluso) sul file txt
    file.write(f"\n\nElementi dall'indice 5 all'indice 15 (escluso): {array_int[5:15]}")


    # Punto 5

    # Stampo gli elementi dell'array con un passo di 3 sul file txt
    file.write(f"\n\nOgni 3 elementi: {array_int[::3]}")


    # Punto 6

    # Assegno il valore di 99 agli elementi dall'indice 5 all'indice 10 (escluso)
    array_int[5:10] = 99

    # Stampo l'array modificato sul txt
    file.write(f"\n\nAssegno il valore di 99 agli elementi dall'indice 5 all'indice 10 (escluso):\n{array_int}")