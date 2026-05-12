import numpy as np


# Punto 1

# Creo un array con valori da 10 a 50 (50 escluso)
array_int = np.arange(10, 50) # Estremo escluso

# Punto 2

# Stampo il risultato del tipo
print(f"Array 1: {array_int}, Tipo: {array_int.dtype}")

# Punto 3

# creo una copia dell'array per convertirlo in float64
array_int_2 = np.array(np.arange(10, 50), dtype="float64")

# Stampo il risultato il tipo
print(f"\n\nArray 2: {array_int_2}, Tipo: {array_int_2.dtype}")

# Punto 4

# Stampo il risultato
print(f"\n\nForma Array 1: {array_int.shape}\nForma Array 2: {array_int_2.shape}")