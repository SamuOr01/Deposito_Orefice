import numpy as np
from numpy import random

# Punto 1

# Creo un array di 12 numeri equidistanti tra 0 e 1
array_eq = np.linspace(0, 1, 12)

# Stampo l'array
print(f"Array con 12 numeri equidistanti tra 0 e 1:\n\n{array_eq}")


# Punto 2

# Cambia la forma dell'array in una matrice 3x4
matrice_eq = array_eq.reshape(3, 4)

# Stampo la matrice
print(f"\nNuova forma dell'array:\n\n{matrice_eq.shape}")


# Punto 3

# Creo una matrice 3x4 di numeri casuali tra 0 e 1
matrice_float = random.rand(3, 4)

# Stampo la matrice
print(f"\nMatrice {matrice_float.shape} di numeri casuali tra 0 e 1:\n\n{matrice_float}")


# Punto 4

# Stampo la somma delle due matrici
somma_matrice_eq = np.sum(matrice_eq)
somma_matrice_float = np.sum(matrice_float)

print("La somme sono:")
print(f"\n\nMatrice Numeri equidistanti: {somma_matrice_eq}")
print(f"\nMatrice con numeri casuali tra 0 e 1: {somma_matrice_float}")