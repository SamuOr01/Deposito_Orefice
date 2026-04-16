print(1 + 2)
print(10 - 5)

print(1 + 5) # Addizione
print(6 - 5 ) # Sottrazione
print(3 * 2) # Moltiplicazione
print(4 / 2) # Divisione
print(3 ** 2) # Potenza


# Variabili

x = 10 # Numeri Interi
y = -5 #Numeri Interi

a = 3.14 # Numeri in virgola mobile (float)
b = -1.0 # Numeri in virgola mobile (float)

nome = "Alice" # Stringhe
msg = 'Ciao!' # Stringhe

s = "Python"
print(s[0]) # Output: 'P'
print(s[2]) # Output: 't'

saluto = "Ciao"
nome = "Alice"
messaggio = saluto + " " + nome
print(messaggio) # Output: 'Ciao Alice'

# Metodi delle stringhe
s = "Ciao Mondo!"
print(len(s)) # Output: 12 # Questo non è un metodo, ma una funzione che restituisce la lunghezza della stringa
print(s.upper()) # Output: 'CIAO, MONDO!'
print(s.split(',')) # Output: '[CIAO] , [MONDO!]'
print(s.replace('mondo', 'universo')) # Output: 'Ciao, universo!'

# Booleani
t = True # Vero
f = False # Falso
print(t)
print(f)

# Operatori Booleani (di confronto)
'''
== Uguale a
!= Diverso da
< Minore di
> Maggiore di
<= Minore o uguale a
>= Maggiore o uguale a
'''
x = 5
y = 10
print(x == y) # Output: False
print(x != y) # Output:True
print(x < y) # Output: True

# Operatori Booleani (logici)
x = 5
y = 10
z = 7
print(x < y and y > z) # Output: True
print(x < y or y < z) # Output: True
print(not(x < z)) # Output: False

# Collezioni in Python
#Liste
numeri = [1, 2, 3, 4, 5]
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, "Alice", True, 4.5]

#Gli indici iniziano da zero
print(numeri[0]) # Output: 1
print(numeri[2]) # Output: 3

numeri[2] = 10 # Le liste sono ordinate e modificabili
print(numeri) # Output: [1, 2, 10, 4, 5]

# Metodi delle liste
numeri = [3, 1, 4, 2, 5]
print(len(numeri)) # Output: 5
numeri.append(6)
print(numeri) # Output: [3, 1, 4, 2, 5, 6]
numeri.insert(2, 10)
print(numeri) # Output: [3, 1, 10, 4, 2, 5, 6]
numeri.remove(4)
print(numeri) # Output: [3, 1, 10, 2, 5, 6]
numeri.sort()
print(numeri) # Output: [1, 2, 3, 5, 6, 10]

# Tuple
punto = (3, 4) # Le tuple sono immutabili
#Gli indici iniziano da zero
punto[0] = 5 # Genera errore

punto = 3, 4 # Tuple packing
x, y = punto # Tuple unpacking
print(x, y) # Output: 3 4

# Set (Insiemi)
numeri = {1,2, 3} # I set sono modificabili e non ordinati

#Gli indici iniziano da zero
set3 = {1, 2, 3, 3, 3, 4, 4, 5} # I set npn contengono duplicati, se provi ad inserirli verranno ignorati
print(set3) # Output: {1, 2, 3, 4, 5}

#Accettano i metodi matematici degli insiemi
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}