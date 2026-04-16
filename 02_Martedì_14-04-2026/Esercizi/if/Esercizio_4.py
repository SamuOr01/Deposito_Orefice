print("Benvenuto, la visione del film è consentita solo ai maggiorenni")
# Il programma chiede all'utente di inserire la propria età
età = int(input("Quanti anni hai?: "))

# Se inserisce 18 anni o più puoi entrare
if età >= 18:
    print("Prego puoi entrare, buona visione!")

# Se inserisce un età inferiore a 18 anni, non puoi entrare perché sei minorenne
else:
    print("Mi dispiace non puoi vedere questo film")