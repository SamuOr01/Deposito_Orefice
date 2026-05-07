def salva_dati(registro_vendite, totale_guadagni):

    with open("Deposito_Orefice\\15_Martedì_05-05-2026\\Esercizi\\Esercizion_1\\dati.txt", "w", encoding="utf-8") as f:

        f.write(f"GUADAGNI:{totale_guadagni}\n")

        f.write("VENDITE:\n")

        for v in registro_vendite:
            f.write(f"{v['cliente']}|{v['articoli']}|{v['totale']}\n")


def carica_dati():

    registro_vendite = []
    totale_guadagni = 0

    try:
        with open("Deposito_Orefice\\15_Martedì_05-05-2026\\Esercizi\\Esercizion_1\\dati.txt", "r", encoding="utf-8") as f:
            righe = f.readlines()

            for r in righe:

                r = r.strip()

                if r.startswith("GUADAGNI:"):
                    totale_guadagni = float(r.split(":")[1])

                elif "|" in r:
                    cliente, articoli, totale = r.split("|")

                    vendita = {
                        "cliente": cliente,
                        "articoli": articoli,
                        "totale": float(totale)
                    }

                    registro_vendite.append(vendita)

    except FileNotFoundError:
        pass

    return registro_vendite, totale_guadagni



def salva_utenti(utenti):
    with open("Deposito_Orefice\\15_Martedì_05-05-2026\\Esercizi\\Esercizion_1\\utenti.txt", "w") as f:
        for username, dati in utenti.items():
            f.write(f"{username},{dati['password']},{dati['ruolo']}\n")

def carica_utenti():
    utenti = {}

    try:
        with open("Deposito_Orefice\\15_Martedì_05-05-2026\\Esercizi\\Esercizion_1\\utenti.txt", "r") as f:
            for riga in f:
                username, password, ruolo = riga.strip().split(",")

                utenti[username] = {
                    "password": password,
                    "ruolo": ruolo
                }

    except FileNotFoundError:
        pass

    return utenti