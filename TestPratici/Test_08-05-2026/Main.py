import GestoreFile as gf

print("==============================================")
print("BENVENUTO NEL SISTEMA DI GESTIONE DELLE CLASSI")
print("==============================================")

while True:

    scelta_1 = input("\nA cosa vuoi accedere?"
                     "\n1. Gestione classi"
                     "\n2. Gestione studenti"
                     "\n3. Esci"
                     "\n\n> "
                    )

    match scelta_1:
        case "1":

            while True:

                scelta_2 = input("\nScegli un'opzione:"
                                "\n1. Crea una nuova classe"
                                "\n2. Mostra una classe esistente"
                                "\n3. Mostra tutte le classi"
                                "\n4. Elimina una classe"
                                "\n5. Esci"
                                "\n\n> \n"
                                )

                match scelta_2:
                    case "1":
                        nome_classe = input("\nInserisci il nome della classe: ")
                        numero_studenti = int(input("Inserisci il numero di studenti: "))
                        gf.crea_classe(numero_studenti, nome_classe)

                    case "2":
                        nome_classe = input("\nInserisci il nome della classe da mostrare: ")
                        classe = gf.mostra_classe(nome_classe)
                        for studente in classe:
                            print(f"\nID: {studente['id']}"
                                  f"\nNome: {studente['nome']} {studente['cognome']}"
                                  f"\nEtà: {studente['età']}"
                                  f"\nClasse: {studente['classe']}"
                                  f"\nMedia: {studente['media']}"
                                )

                    case "3":
                        pass

                    case "4":
                        pass

                    case "5":
                        print("Tornando al menu principale...")
                        break

                    case _:
                        print("Scelta non valida. Riprova.")
                        continue

        case "2":
            pass

        case "3":
            print("Grazie per aver utilizzato il sistema di gestione delle classi. Arrivederci!")
            break

        case _:
            print("Scelta non valida. Riprova.")
            continue