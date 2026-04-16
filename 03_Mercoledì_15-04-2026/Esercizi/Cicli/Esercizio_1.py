# Chiedi all'utente da quale numero far paritre il conto alla rovescia

print("Conto alla rovescia\n")

# Variabile booleana di controllo per il ciclo while
esegui = True

# Finchè il valore è True il ciclo sarà eseguito all'infinito
while esegui:

    # input dell'utente per iniziare il conto alla rovescia
    inizio = int(input("Da quale numero vuoi iniziare? "))

    # Stampa riga vuota per migliorare laleggibilità della console
    print()

    # Esegue il ciclo for che parte dal numero inserito e arriva fino a zero,
    # decrementando di 1 ad ogni iterazione
    for i in range(inizio, -1, -1):
        print(i)

    # Chiediamo all'utente se vuole eseguire un altro conto alla rovescia
    scelta = input("\nVuoi riprovare? (s/n) ")

    # Se l'utente risponde 'n', la variabile di controllo viene impostata a False, interrompendo il ciclo while
    if scelta.lower() == 'n':
        esegui = False