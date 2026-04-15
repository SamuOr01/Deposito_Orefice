# Chiedi all'utente di inserire un numero
# Il programma verifica se quel numero è primo fino a quando non ne immagazzina 5

# Creazione di una lista vuota per immagazzinare 5 numeri primi
numeri_primi = []

# Finchè la lista contiene meno di 5 numeri primi, il ciclo continua
while len(numeri_primi) < 5:

    # Chiede all'utente di inserire un numero
    numero = int(input("Inserisci un numero: "))

    # Se il numero è maggiore di 1 e il modulo del numero diviso 2 è diverso da zero
    # oppure è uguale a 2
    if numero > 1 and numero % 2 != 0 or numero == 2:

        # Il numero è primo e viene aggiunto alla lista
        numeri_primi.append(numero)

    # Altrimenti il numero non è primo e viene stampato un messaggio
    else:
        print("Il numero", numero, "non è primo.")

# Alla fine del ciclo stampa la lista dei numeri immagazzianti
print("I numeri primi inseriti sono:", numeri_primi)