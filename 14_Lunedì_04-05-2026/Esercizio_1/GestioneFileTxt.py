# Metodo per la creazione dei file txt
def crea_file_txt(data: str, lista_vendite, somma, media, lista_sopra_media):

    # Inizializzazione dei path
    folder_path = "Deposito_Orefice\\14_Lunedì_04-05-2026\\Esercizio_1"
    data_path = data.replace("/","-")
    file_path = f"{folder_path}\\Vendite_{data_path}.txt"

    # creazione del file
    with open(file_path, "w", encoding="utf-8") as resoconto:
        resoconto.write(f"Data: {data}\n")

        # Se la lista vendite è vuota
        if len(lista_vendite) == 0:
            # Scrive il messaggio
            resoconto.write("\nNon sono state effettuate vendite")
        else:
            # Altrimenti le elenca
            resoconto.write("\nle vendite sono:")

            for i, vendita in enumerate(lista_vendite, 1):
                resoconto.write(f"\n{i}) {vendita:.2f}€")

        # Scrive somma e media
        resoconto.write(f"\nLa somma è: {somma:.2f}€")
        resoconto.write(f"\nLa media è: {media:.2f}€\n")

        # Se la lista sopra la media è vuota
        if len(lista_sopra_media) == 0:
            # Scrive il messaggio
            resoconto.write("\nNon sono state effettuate vendite sopra la media")
        else:
            # Altrimenti le elenca
            resoconto.write("\nle vendite sopra la media sono:")

            for i, vendita in enumerate(lista_sopra_media, 1):
                resoconto.write(f"\n{i}) {vendita:.2f}")

    # Messaggio per capire che l'operazione è conclusa
    print(f"\nIl file, Vendite_{data_path}.txt, è stato creato con successo")