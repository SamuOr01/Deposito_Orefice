# Le funzioni sono blocchi di codice autonomi che eseguono una determinata operazione

# Possono avere o no il return
# Possono avere o no i parametri

# Senza return
def saluta(nome):
    print("Ciao ", nome)

# Possono avere infiniti parametri e infinite righe

def somma(a, b):
    risultato = a + b
    print("La somma è:", risultato)

# Per essere eseguite necessitano di essere chiamate, scrivendo il nome con le parentesi
# e gli eventuali parametri

saluta("Alice")
somma(5, 3)

# Con return
def quadrato(numero):
    return numero * numero

risultato = quadrato(4)
print(risultato) # Output: 16

# Deve esserci solo un return per funzione,
# l'unico mod per averne di più è mettendo le condizioni con l'if

# Tipi di parametri

# 1) Posizionali -> paasati in ordine esatto
# 2) keyword -> passati in qualsiasi ordine specificando il nome del parametro
# 3) di default -> assegna un valore predefinito qualora il parametro non venga passato

def saluta(nome:str, messaggio="Ciao"):
    print(f"{messaggio} {nome}")

saluta("Mario") # Chiamata alla funzione
saluta("Luigi", messaggio="Buongiorno")

# Funzioni Generatori

# Permettono di iterare su una serie di valori, ma invece di restituire tutti i valori insieme,
# li restituiscono uno alla volta, utile per stampare sequenze molto lunghe e complesse
def fibonacci(n):
    a, b = 0, 1
    print(a)
    print(b)

    while a < n:
        # yield equivalente di return, ma invece di chiudere la funzione
        # restituisce un valore e ricomincia fino alla fine dell'iterazione
        yield a
        a, b = b, a + b

fibonacci(100)

# Decoratori

# Sono una funzione che modifica il comportamento di un'altra funzione o metodo senza modificarne direttamente il codice.
def decoratore(funzione):
    # Un wrapper è una funzione interna definita all'interno di un decoratore che "avvolge" la funzione originale,
    # permettendo di aggiungere funzionalità extra prima o dopo l'esecuzione della funzione decorata,
    # senza alterarne direttamente il codice.
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopol'esecuzione della funzione")
    return wrapper

# Si applicano anteponendo il simbolo @ al nome del decoratore sopra la funzione da decorare.
@decoratore
def saluta():
    print("Ciao!")

saluta()

# Decoratori per funzioni con parametri

# Il wrapper utilizza in genere *args e **kwargs per garantire che possa gestire un numero variabile
# di argomenti posizionali e keyword, mantenendo la flessibilità della funzione originale.
def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b

print("risultato è", somma(3, 4))