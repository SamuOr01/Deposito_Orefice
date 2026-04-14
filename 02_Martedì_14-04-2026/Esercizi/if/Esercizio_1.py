print("Benvenuto, l'accesso è consentito solo ai maggiorenni")
età = int(input("Quanti anni hai?: "))

if età >= 18: # Se inserisci 18 anni o più puoi entrare
    print("Prego puoi entrare")
elif età <= 0: # Se inserisci 0 anni o meno, l'età è invalida
    print("Età non valida!")
else: # Se inserisci un numero tra 1 e 17 anni, non puoi entrare perché sei minorenne
    print("Mi dispiace non puoi entrare")