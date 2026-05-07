from modulo_capoprincipale import Giacca, Pantalone, Gilet
from modulo_finitura import Cravatta, Papillon, Pochette

import random

# Lista per scelta degli oggetti
lista_capo_principale = [
    "Giacca",
    "Pantalone",
    "Gilet"
]

lista_finitura = [
    "Cravatta",
    "Papillon",
    "Pochette"
]

lista_taglie =[
    "S",
    "M",
    "L",
    "XL",
    "XXL"
]

lista_colori = [
    "Nero",
    "Bianco",
    "Blu",
    "Rosso"
]

lista_tessuti = [
    "Lana",
    "Cotone",
    "Seta"
]

lista_tipo_taglio = [
    "skinny",
    "wide",
    "slim"
]

lista_larghezze = [
    5,
    7,
    9
]

lista_tipo_chiusura = [
    "a clip",
    "a nodo"
]

prezzo_giacca = 40.0
prezzo_pantalone = 30.0
prezzo_gilet = 25.0

prezzo_cravatta = 15.0
prezzo_papillon = 15.0
prezzo_pochette = 10.0

codice = 0
lista_catalogo = []

def random_caratteristiche_capo_principale(codice, lista_tessuti, lista_colori, lista_taglie, lista_tipo_taglio):
    # Generazione casuale delle caratteristiche
    codice += 1
    tessuto = random.choice(lista_tessuti)
    colore = random.choice(lista_colori)
    taglia = random.choice(lista_taglie)
    tipo_taglio = random.choice(lista_tipo_taglio)
    numero_bottoni = random.randint(1, 3)
    è_reversibile = random.choice([True, False])


    return codice, tessuto, colore, taglia, tipo_taglio, numero_bottoni, è_reversibile

def random_caratteristiche_finitura(codice, lista_tessuti, lista_colori, lista_larghezze, lista_tipo_chiusura):

    # Generazione casuale delle caratteristiche
    codice += 1
    tessuto = random.choice(lista_tessuti)
    colore = random.choice(lista_colori)
    larghezza = random.choice(lista_larghezze)
    tipo_chiusura = random.choice(lista_tipo_chiusura)
    ha_piega_decorativa = random.choice([True, False])

    return codice, tessuto, colore, larghezza, tipo_chiusura, ha_piega_decorativa

def creazione_casuale(lista_capo_principale, lista_finitura):

    while True:

        scelta = input("Cosa desidera acquistare?"
                    "\n1. Capo Principale"
                    "\n2. Finitura"
                    "\n\n> "
                    )

        match scelta:
            case "1":
                codice, tessuto, colore, taglia, tipo_taglio, numero_bottoni, è_reversibile = random_caratteristiche_capo_principale(codice, lista_tessuti, lista_colori, lista_taglie, lista_tipo_taglio)
                capo_principale_scelto = random.choice(lista_capo_principale)

                if capo_principale_scelto == "Giacca":
                    capo_principale = Giacca(codice, "Giacca", tessuto, colore, taglia, prezzo_giacca, numero_bottoni)
                    print(f"Hai scelto: {capo_principale._nome} - Costo totale: {capo_principale.costo()}€")
                    lista_catalogo.append(capo_principale)

                elif capo_principale_scelto == "Pantalone":
                    capo_principale = Pantalone(codice, "Pantalone", tessuto, colore, taglia, prezzo_pantalone, tipo_taglio)
                    print(f"Hai scelto: {capo_principale._nome} - Costo totale: {capo_principale.costo()}€")
                    lista_catalogo.append(capo_principale)

                elif capo_principale_scelto == "Gilet":
                    capo_principale = Gilet(codice, "Gilet", tessuto, colore, taglia, prezzo_gilet, è_reversibile)
                    print(f"Hai scelto: {capo_principale._nome} - Costo totale: {capo_principale.costo()}€")
                    lista_catalogo.append(capo_principale)
            case "2":
                codice, tessuto, colore, larghezza, tipo_chiusura, ha_piega_decorativa = random_caratteristiche_finitura(codice, lista_tessuti, lista_colori, lista_larghezze, lista_tipo_chiusura)
                finitura_scelta = random.choice(lista_finitura)

                if finitura_scelta == "Cravatta":
                    finitura = Cravatta(codice, "Cravatta", tessuto, colore, larghezza, prezzo_cravatta)
                    print(f"Hai scelto: {finitura._nome} - Costo totale: {finitura.costo()}€")
                    lista_catalogo.append(finitura)

                elif finitura_scelta == "Papillon":
                    finitura = Papillon(codice, "Papillon", tessuto, colore, prezzo_papillon, tipo_chiusura)
                    print(f"Hai scelto: {finitura._nome} - Costo totale: {finitura.costo()}€")
                    lista_catalogo.append(finitura)

                elif finitura_scelta == "Pochette":
                    finitura = Pochette(codice, "Pochette", tessuto, colore, prezzo_pochette, ha_piega_decorativa)
                    print(f"Hai scelto: {finitura._nome} - Costo totale: {finitura.costo()}€")
                    lista_catalogo.append(finitura)
            case _:
                print("Scelta non valida. Riprova.")
                continue