frutta = ["mela", "banana", "arancia", "melograno"]

scelta = input(
'''Che operazione vuoi eseguire?
    1) Aggiungi
    2) Modifica
    3) Elimina

''')

if scelta == "1": # Se l'utente sceglie 1, aggiungiamo un elemento alla lista
    print("Hai scelto di aggiungere un elemento")
    nuova_frutta = input("Quale frutto vuoi aggiungere? ")
    frutta.append(nuova_frutta.lower())
    print(frutta)
elif scelta == "2": # Se l'utente sceglie 2, modifichiamo un elemento della lista
    print("Hai scelto di modicare un elemento")
    indice = int(input("Quale elemento vuoi modificare? (inserisci l'indice) "))
    nuova_frutta = input("Quale frutto vuoi inserire? ")
    frutta[indice] = nuova_frutta.lower()
    print(frutta)
else: # Se l'utente sceglie 3, eliminiamo un elemento della lista
    print("Hai scelto di eliminare un elemento")
    indice = int(input("Quale elemento vuoi eliminare? (inserisci l'indice) "))
    frutta.remove(frutta[indice])
    print(frutta)