import GestoreFile as gf

print("==============================================")
print("BENVENUTO NEL SISTEMA DI GESTIONE DELLE CLASSI")
print("==============================================")

while True:

    # MENU PRINCIPALE
    scelta = input("\nScegli un'opzione:"
                    "\n1. Crea una nuova classe"
                    "\n2. Mostra una classe"
                    "\n3. Mostra tutte le classi"
                    "\n4. Elimina una classe"
                    "\n5. Analizza una classe"
                    "\n6. Esci"
                    "\n\n> "
                    )

    match scelta:

        # Creazione di una nuova classe
        case "1":
            nome_classe = input("\nInserisci il nome della classe: ")

            # Controllo per evitare l'inserimento di un valore errato
            try:
                numero_studenti = int(input("Inserisci il numero di studenti: "))
            except ValueError:
                print("Inserisci un numero valido.")
                continue

            # Chiamata alla funzione per creare la classe e scrivere i dati nel file
            gf.crea_classe(numero_studenti, nome_classe)

        # Mostra una classe
        case "2":
            nome_classe = input("\nInserisci il nome della classe da mostrare: ")

            # Chiamata alla funzione per leggere i dati dal file e mostrarli a schermo
            classe = gf.mostra_classe(nome_classe)

            # Controllo per verificare se la classe è vuota o non esiste
            if not classe:
                print("Classe vuota o non trovata.")
                continue

            # Stampa dei dati degli studenti a schermo
            for studente in classe:
                print(f"\nID: {studente['id']}"
                        f"\nNome: {studente['nome']} {studente['cognome']}"
                        f"\nEtà: {studente['età']}"
                        f"\nClasse: {studente['classe']}"
                        f"\nMedia: {studente['media']}"
                    )

        # Mostra tutte le classi
        case "3":
            print("\nClassi disponibili:")

            # Chiamata alla funzione per mostrare tutte le classi disponibili
            gf.mostra_tutte_classi()

        # Elimina una classe
        case "4":
            nome_classe = input("\nInserisci il nome della classe da eliminare: ")

            # Chiamata alla funzione per eliminare la classe
            gf.elimina_classe(nome_classe)

        # Analizza una classe
        case "5":
            nome_classe = input("\nInserisci il nome della classe da analizzare: ")

            # Chiamata alla funzione per analizzare la classe
            gf.analizza_classe(nome_classe)

        # Esci dal programma
        case "6":
            print("Arrivederci!")
            break

        # Scelta non valida
        case _:
            print("Scelta non valida. Riprova.")
            continue