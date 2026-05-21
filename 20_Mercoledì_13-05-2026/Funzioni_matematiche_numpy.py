import numpy as np

A = np.array([10, 20, 30])
B = np.array([1, 2, 3])


# NumPy mette a disposizione diverse funzioni aritmetiche
# che permettono di eseguire operazioni elemento per elemento
# tra array della stessa dimensione.
#
# Le principali sono:
# - np.add() -> somma
# - np.subtract() -> sottrazione
# - np.multiply() -> moltiplicazione
# - np.divide() -> divisione

print(f"Somma: {np.add(A, B)}")
print(f"Sottrazione: {np.subtract(A, B)}")
print(f"Moltiplicazione: {np.multiply(A, B)}")
print(f"Divisione: {np.divide(A, B)}")

print() # Riga vuota per pulizia output

# NumPy include anche numerose funzioni matematiche applicabili
# direttamente agli array.
#
# Alcune delle più utilizzate sono:
# - np.sin() -> seno
# - np.cos() -> coseno
# - np.exp() -> esponenziale
# - np.log() -> logaritmo naturale
#
# Le operazioni vengono eseguite su ogni elemento dell'array.

print(f"Seno: {np.sin(A)}")
print(f"Coseno: {np.cos(A)}")
print(f"Esponenziale: {np.exp(A)}")
print(f"Logaritmo: {np.log(A)}")

print() # Riga vuota per pulizia output

# NumPy offre anche strumenti molto utili per l'analisi statistica.
#
# Le funzioni principali sono:
# - np.mean() -> media aritmetica
# - np.median() -> mediana
# - np.std() -> deviazione standard
# - np.var() -> varianza

print(f"Media: {np.mean(A)}")
print(f"Mediana: {np.median(A)}")
print(f"STD: {np.std(A)}")
print(f"Varianza: {np.var(A)}")

print() # Riga vuota per pulizia output

# NumPy include funzioni dedicate all'algebra lineare
# con la quale possiamo lavorare con matrici,
# sistemi lineari, autovalori e molto altro.

M1 = np.array([1, 2], [3, 4])
M2 = np.array([5, 6], [7, 8])

# Le funzioni principali sono:
# - np.dot()    -> prodotto scalare o matriciale
# - np.matmul() -> moltiplicazione tra matrici

print(f"Prodotto mat dot: {np.dot(A, B)}")
print(f"Prodotto mat mul: {np.matmul(A, B)}")

# Determinante e Inversa:

# - np.linalg.det() -> calcola il determinante
# - np.linalg.inv() -> calcola la matrice inversa

print(f"Determinante: {np.linalg.det(A)}")
print(f"Inversa: {np.linalg.inv(B)}")

# Autovalori e Autovettori:

# La funzione np.linalg.eig() restituisce:
# - autovalori
# - autovettori
# associati a una matrice quadrata.

autovalori, autovettori = np.linalg.eig(M1)

print(f"Autovalori: {autovalori}")
print(f"Autovettori:\n{autovettori}")

print()

# Risoluzione di  Sistemi Lineari:

# np.linalg.solve() permette di risolvere sistemi lineari
# del tipo:
#
# Ax = B
#
# dove:
# - A è la matrice dei coefficienti
# - B è il vettore dei termini noti

A_sistema = np.array([[2, 1],
                      [1, 3]])

B_sistema = np.array([8, 13])

soluzione = np.linalg.solve(A_sistema, B_sistema)

print(f"Soluzione del sistema: {soluzione}")