# Ciclo While
# Si usa il ciclo while quando non si sa a priori quante volte deve essere eseguito il blocco di codice

conteggio = 0

# Cicla in loop fino a quando la condizione è vera
# Nel momento in cui la condizione restituisce false, il ciclo si interrompe
while conteggio < 5:
    print(conteggio)
    conteggio += 1


# Il ciclo più utile è quello booleano

controllore = True

while controllore:
    # Lasciando solo questa riga il ciclo sarebbe infinito
    print("Ciao")

    # Per interrompere il ciclo, è necessario modificare la variabile di controllo
    scelta = input("Vuoi continuare? (s/n) ")
    if scelta.lower() == 'n':
        controllore = False

# Ciclo For
# Si usa il ciclo for quando si è a conoscenza di quante volte deve essere eseguito il blocco di codice

numeri = [1, 2, 3, 4, 5]

# Per ogni elemento nella lista numeri
for numero in numeri:
    # Stampa l'elemento corrente
    print(numero)


# La funzione range(), permette di generare una sequenza di numeri
# Utilizza dei parametri per specificare:
# l'inizio (opzionale, default 0), la fine (obbligatorio) e il passo (opzionale, default 1) della sequenza

# Utilizzo di range() con un solo parametro stop
# Genera una sequenza di numeri da 0 a 4 (0 incluso 5 escluso)
for i in range(5):
    print(i)

# Utilizzo di range() con un parametro start e stop
# Genera una sequenza di numeri da 2 a 7 (2 incluso 8 escluso)
for i in range(2, 8):
    print(i)

# Utilizzo di range() con un parametro start, stop e step
# Genera una sequenza di numeri da 1 a 9 (1 incluso 10 escluso con passo 2)
for i in range(1, 10, 2):
    print(i)