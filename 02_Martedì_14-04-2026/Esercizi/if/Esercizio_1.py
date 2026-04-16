print("Benvenuto, l'accesso è consentito solo ai maggiorenni")
# Il programma chiede all'utente di inserire la propria età
età = int(input("Quanti anni hai?: "))

# Se inserisce 18 anni o più puoi entrare
if età >= 18:
    print("Prego puoi entrare")

# Se inserisce 0 anni o meno, l'età è invalida
elif età <= 0:
    print("Età non valida!")

# Se inserisce un età compresa tra 1 e 17 anni, non puoi entrare perché sei minorenne
else:
    print("Mi dispiace non puoi entrare")