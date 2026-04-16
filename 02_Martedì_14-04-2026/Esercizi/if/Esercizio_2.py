# creazione lista
frutta = ["mela", "banana", "arancia", "melograno"]

# chiediamo all'utente quale operazione vuole eseguire sulla lista
scelta = input(
'''Che operazione vuoi eseguire?
    1) Aggiungi
    2) Modifica
    3) Elimina

''')

# Se l'utente sceglie 1, aggiungiamo un elemento alla lista
if scelta == "1":
    print("Hai scelto di aggiungere un elemento")
    nuova_frutta = input("Quale frutto vuoi aggiungere? ")
    # aggiungiamo il nuo vo elemento alla lista
    frutta.append(nuova_frutta.lower())
    # stampiamo la lista aggiornata
    print(frutta)

# Se l'utente sceglie 2, modifichiamo un elemento della lista
elif scelta == "2":
    print("Hai scelto di modicare un elemento")
    # chiediamo all'utente quale elemento vuole modificare, indicandone l'indice
    indice = int(input("Quale elemento vuoi modificare? (inserisci l'indice) "))
    # chiediamo all'utente quale nuovo elemento vuole inserire al posto di quello scelto
    nuova_frutta = input("Quale frutto vuoi inserire? ")
    # modifichiamo l'elemento scelto con il nuovo elemento inserito dall'utente
    frutta[indice] = nuova_frutta.lower()
    # stampiamo la lista aggiornata
    print(frutta)

# Se l'utente sceglie 3, eliminiamo un elemento della lista
else:
    print("Hai scelto di eliminare un elemento")
    # chiediamo all'utente quale elemento vuole eliminare, indicandone l'indice
    indice = int(input("Quale elemento vuoi eliminare? (inserisci l'indice) "))
    # eliminiamo l'elemento scelto dalla lista
    frutta.remove(frutta[indice])
    # stampiamo la lista aggiornata
    print(frutta)