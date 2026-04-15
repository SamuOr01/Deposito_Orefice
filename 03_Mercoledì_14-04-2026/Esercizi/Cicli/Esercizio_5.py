# Chiediamo all'utente di inserire stop e step per il range
stop = int(input("Inserisci il numero massimo di iterazioni: "))
step = int(input("Inserisci il passo: "))

# Utilizziamo i valori forniti come parametri per il range
for i in range(0, stop, step):
    # Stampiamo il risultato
    print(i)