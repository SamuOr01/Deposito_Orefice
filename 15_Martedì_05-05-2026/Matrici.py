# Una matrice è una lista di liste, tipo list, ordinate e modificabili,
# ogni lista interna rappresenta una riga della matrice.

matrice = [
    [1, 2, 3], # prima riga
    [4, 5, 6], # seconda riga
    [7, 8, 9]  # terza riga
]

# Matrice 3x3 in cui ogni elemento è un numero intero. Possiamo accedere agli elementi
# utilizzando gli indici delle righe e delle colonne

# Accesso all'elemento nella prima riga e seconda colonna
elemento = matrice[0][1]

print(elemento) # Output: 2

# Possiamo anche iterare sugli elementi di una matrice utilizzando
# i cicli for annidati, sia per le righe che per le colonne.

for riga in matrice:
    for elemento in riga: print(elemento)

# Questa iterazione stamperebbe tutti gli elementi della matrice uno per uno