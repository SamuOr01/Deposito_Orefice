# NumPy (Numerical Python) è una libreria open source fondamentale per il calcolo scientifico in Python.
# Permette di lavorare con array e matrici multidimensionali, cioè strutture dati che possono
# avere una o più dimensioni e che risultano molto più efficienti delle normali liste Python
# sia in termini di memoria che di velocità.

# Oltre alla gestione degli array, NumPy offre un’ampia gamma di funzioni matematiche
# che consentono di eseguire operazioni complesse, come calcoli vettoriali e matriciali,
# algebra lineare, trasformate di Fourier e analisi statistiche.

# Grazie a queste caratteristiche, è ampiamente utilizzata in ambiti come l’analisi dei dati,
# la modellazione scientifica e il machine learning. Inoltre, permette di integrare codice scritto
# in C, C++ e Fortran, migliorando ulteriormente le prestazioni delle operazioni numeriche.

# Numpy ha dei concetti e delle keyword di base:
# - ndarray: L'oggetto array multidimensionale principale di NumPy. Gli array di NumPy sono più veloci
#   e più efficienti in termini di memoria rispetto alle liste native di Python.
# - dtype: Specifica il tipo di dato degli elementi di un array. I tipi di dato comuni
#   includono int, float, bool, etc.
# - shape: Una proprietà che restituisce le dimensioni dell'array. Per esempio, un array con 3 righe e
#   4 colonne avrà una shape di (3, 4).
# - arange: Una funzione per creare array con valori sequenziali. È simile alla funzione range() di Python,
#   ma restituisce un array invece di una lista.
# - reshape: Cambia la shape di un array senza modificarne i dati.
# - linspace: Genera un array di numeri equamente distribuiti tra un valore iniziale e un valore finale.
# - random: Modulo per generare array con valori casuali, incluse distribuzioni normali e uniformi.
# - sum, mean, std: Funzioni per calcolare rispettivamente la somma, la media e la deviazione standard
#   degli elementi di un array.

# Per iniziare ad usare numpy importiamo il modulo
import numpy as np


# NDARRAY

# L'ndarray è l'elemento fondamentale di NumPy.
# È un array multidimensionale che può contenere dati di un singolo tipo.

# Creazione di un array monodimensionale
arr = np.array([1, 2, 3, 4, 5])

# Creazione di un array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# È possibile creare array NumPy utilizzando funzioni come:
# - np.array() -> Converte una lista in array
# - np.zeros() -> Crea un array pieno di zeri, ha come parametro la lunghezza dell'array
# - np.ones() -> Crea un array pieno di uno, ha come parametro la lunghezza dell'array
# - np.arange() -> Funziona come la funzione range() con start, stop e step
# - np.linspace() -> Genera un array di valori distribuiti uniformemente tra un punto iniziale e uno finale

# Questo esempio ne spiega alcuni ma per vederli tutti vai alla fine delle slide,
# più precisamente la slide NP1*:

print("Forma dell'array:", arr.shape) # Output: (5,)
print("Dimensioni dell'array:", arr.ndim) # Output: 1
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5
print("Indice del valore massimo:", arr.argmax()) # Output: 4


# DTYPE

# Il dtype specifica il tipo di dati contenuti nell'array.
# Può essere int, float, bool, etc.

arr = np.array([1, 2, 3], dtype='int32')
print(arr.dtype) # Output: int32


# SHAPE

# La shape di un array indica le sue dimensioni.
# È una tupla che rappresenta il numero di elementi in ciascuna dimensione (numero_righe, numero_colonne).

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) # Output: (2, 3)


# ARANGE

# La funzione arange crea un array contenente una sequenza di numeri,
# simile a range di Python con start, stop e step.

arr = np.arange(10)
print(arr) # Output: [0 1 2 3 4 5 6 7 8 9]


# RESHAPE

# La funzione reshape cambia la forma di un array senza modificarne i dati.

arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr) # Output: [[0 1 2] [3 4 5]]


# INDEXING E SLICING

# Gli array NumPy possono essere indicizzati e affettati in modo
# simile alle liste Python, ma con funzionalità aggiuntive.

arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0]) # Output: 1

# Slicing
print(arr[1:3]) # Output: [2 3]

# Boolean Indexing -> Usare una condizione booleana come indice
print(arr[arr > 2]) # Output: [3 4 5]

# Gli array NumPy supportano il slicing e il fancy indexing, permettendo
# di estrarre porzioni di array e modificare il loro contenuto in modo efficiente.

arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]]
                  )

# Slicing sulle righe
print(arr_2d[1:3]) # Output: [[ 5 6 7 8]
                            # [ 9 10 11 12]]

# Slicing sulle colonne
# print(arr_2d[:, 1:3]) # Output: [[ 2 3]
                                 # [ 6 7]
                                 # [10 11]]

# Slicing misto
print(arr_2d[1:3, 1:3]) # Output: [[ 6 7]
                                 # [10 11]]


# SLICING

# È una tecnica utilizzata per estrarre una parte di un array o di una sequenza.
# In NumPy, lo slicing è simile a quello delle liste in Python, ma è molto più potente e versatile.
# Consente di ottenere porzioni di un array esistente senza copiare i dati, il che è efficiente in
# termini di memoria.

# La sintassi base per lo slicing in NumPy è:

# array[start:stop:step]

# - start: L'indice di inizio dello slicing (inclusivo). Se omesso, il valore predefinito è 0.
# - stop: L'indice di fine dello slicing (esclusivo). Se omesso, il valore predefinito è la dimensione dell'array.
# - step: Il passo tra un indice e l'altro. Se omesso, il valore predefinito è 1.

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base
print(arr[2:7]) # Output: [2 3 4 5 6]

# Slicing con passo
print(arr[1:8:2]) # Output: [1 3 5 7]

# Omettere start e stop
print(arr[:5]) # Output: [0 1 2 3 4]
print(arr[5:]) # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr[-5:]) # Output: [5 6 7 8 9]
print(arr[:-5]) # Output: [0 1 2 3 4]


# FANCY INDEXING

# È una tecnica che permette di selezionare elementi di un array utilizzando array di indici interi.
# Questo consente una selezione complessa e flessibile di elementi rispetto allo slicing normale.

arr = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices]) # Output: [20 40]

# Utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr[indices]) # Output: [10 30 50]


# DIFFERENZE TRA SLICING E FANCY INDEXING

# Slicing:
    # - È limitato a selezioni rettangolari, cioè regolari e contigui dei dati.
        # - regolari -> con una forma semplice e ordinata
        # - contigui -> senza “buchi”, cioè tutti gli elementi sono uno accanto all’altro
    # - Restituisce una vista dell'array originale
    #   (non crea una copia).
    # - Utilizza indici di inizio, fine e passo.

# Fancy Indexing:
    # - Può selezionare elementi non contigui e in ordine arbitrario.
    # - Crea sempre una copia dei dati selezionati.
    # - Utilizza array di indici interi.

#