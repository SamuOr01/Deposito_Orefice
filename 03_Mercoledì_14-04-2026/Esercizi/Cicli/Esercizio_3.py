# Inizializziamo una variabile booleana di controllo
esegui = True

# Inizializziamo una variabile per la somma a 0
somma = 0

# Finchè esegui è True, chiediamo all'utente di inserire un numero
while esegui:

    # Input dell'utente
    numero = int(input("Inserisci un numero: "))

    # Se il numero è diverso da 0
    if numero != 0:

        # Lo aggiungiamo alla somma
        somma += numero
    # Se il numero è 0 
    else:

        # Cambiamo il valore di esegui a False per uscire dal ciclo
        esegui = False

        # Stampiamo la somma dei numeri inseriti
        print("la somma dei numeri inseriti è: ", somma)