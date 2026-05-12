import numpy as np
from numpy import random

# Punto 1

# Creo la matrice 6x6 con numeri random tra 1 e 100
matrice_int = random.randint(1, 100, size = (6, 6))

# Stampo la matrice
print(f"Matrice {matrice_int.shape}:\n\n{matrice_int}")


# Punto 2

# Dalla matrice 6x6 estraggo una matrice 4x4
matrice_int_2 = matrice_int[:4, :4]

# Stampo la nuova matrice
print(f"\nMatrice {matrice_int_2.shape}:\n\n{matrice_int_2}")


# Punto 3

# Inverto la matrice
matrice_invertita = matrice_int_2[::-1]

# Stampo la matrice invertita
print(f"\nMatrice {matrice_invertita.shape} invertita:\n\n{matrice_invertita}")


# Punto 4

# Stampo la diagonale della matrice invertita con il F.Indexing
print(f"\nDiagonale della Matrice invertita {matrice_invertita.shape}:\n\n{matrice_invertita[[0, 1, 2, 3], [0, 1, 2, 3]]} (F.Indexing)")

# Stampo la diagonale della matrice invertita con np.diagonal()
print(f"\nDiagonale della Matrice invertita {matrice_invertita.shape}:\n\n{matrice_invertita.diagonal()} (np.diagonal())")


# Punto 5

# Stampo la matrice invertita sostituendo -1 a tutti i multipli di 3
matrice_invertita[matrice_invertita % 3 == 0] = -1
print(f"\nSostituisco -1 a tutti i multipli di 3 della matrice invertita:\n\n{matrice_invertita}")