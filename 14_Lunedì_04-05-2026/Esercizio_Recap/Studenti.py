# Funzione per aggiungere lo studente alla lista csv
def aggiungi_studente(file_path, nome, cognome, età, data_nascita, corso):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{nome},{cognome},{età},{data_nascita},{corso}\n")

# Funzione per modificare lo studente dalla lista csv
def modifica_studente(file_path, nome, cognome, età, data_nascita, corso):
    pass

# Funzione per stampare l'aula
def stampa_aula(file_path):

    # Lista vuota
    studenti = []

    # Apre il file
    with open(file_path, "r", encoding="utf-8") as file:

        # Per ogni riga estrapola i dati
        for riga in file:
            dati = riga.strip().split(",")

            if len(dati) == 5:
                nome, cognome, età, data_nascita, corso = dati
                studenti.append((nome, cognome, età, data_nascita, corso))

    # Ordinamento per corso
    studenti.sort(key=lambda x: x[4])

    # Stampa l'elenco
    for s in studenti:
        print(f"Nome: {s[0]} {s[1]} | Età: {s[2]} | Nascita: {s[3]} | Corso: {s[4]}")