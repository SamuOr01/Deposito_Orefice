# BROADCASTING IN NUMPY

# Il broadcasting è una delle funzionalità più potenti di NumPy.
# Permette di eseguire operazioni aritmetiche tra array con
# dimensioni diverse senza dover creare manualmente array
# della stessa forma.

# Grazie al broadcasting, NumPy riesce ad "adattare"
# automaticamente gli array per rendere possibile
# l’operazione element-wise.

# Questo approccio rende il codice:
# - più semplice da scrivere
# - più leggibile
# - più efficiente in termini di memoria e prestazioni

import numpy as np

# ESEMPIO BASE DI BROADCASTING

# In questo esempio:
# - A è un array di 3 elementi
# - B contiene un solo valore

# NumPy espande automaticamente B per eseguire
# l'operazione su tutti gli elementi di A.

A = np.array([1, 2, 3])
B = 10

print(A + B)
# Output: [11 12 13]

# PRINCIPI DEL BROADCASTING

# Quando NumPy esegue operazioni tra array,
# controlla se le loro dimensioni sono compatibili.

# Due dimensioni sono compatibili se:
# - sono uguali
# - oppure una delle due è 1

# Se necessario, NumPy espande automaticamente
# la dimensione pari a 1 per adattarla all’altro array.

# ESEMPIO CON ARRAY 2D

M = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

V = np.array([10, 20, 30])

# NumPy replica virtualmente V su ogni riga della matrice

print(M + V)

# Output:
# [[11 22 33]
#  [14 25 36]]


# REGOLE DEL BROADCASTING

# 1. ALLINEAMENTO DA DESTRA A SINISTRA

# NumPy confronta le dimensioni partendo da destra.

# Esempio:

# (2, 3)
# (3,)

# Il secondo array viene interpretato come:

# (1, 3)

# quindi le dimensioni risultano compatibili.


# 2. DIMENSIONI COMPATIBILI

# Due dimensioni sono compatibili se:

# - sono uguali
# - oppure una delle due è 1

# Esempi compatibili:

# (4, 3)
# (1, 3)

# (5, 1)
# (5, 7)

# Esempio NON compatibile:

# (2, 3)
# (4, 3)

# 3. ESPANSIONE AUTOMATICA

# Le dimensioni pari a 1 vengono espanse automaticamente.

# L'espansione è virtuale:
# NumPy non crea realmente copie dei dati,
# rendendo il broadcasting molto efficiente.

# VANTAGGI DEL BROADCASTING

# Efficienza:
# - evita copie inutili di array
# - riduce il consumo di memoria
# - migliora le prestazioni

# Semplicità:
# - codice più corto e leggibile
# - meno loop espliciti
# - operazioni matematiche più intuitive

# ESEMPIO PRATICO

# Possiamo usare il broadcasting anche per
# normalizzare dati o applicare trasformazioni.

dati = np.array([100, 150, 200, 250])

incremento = 50

nuovi_dati = dati + incremento

print(nuovi_dati)

# Output:
# [150 200 250 300]