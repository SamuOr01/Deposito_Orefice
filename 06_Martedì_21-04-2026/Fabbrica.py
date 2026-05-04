# Generalmente si usa uno script solo per le classi
# da importare in un altro script che li gestisce

# importiamo la classe Automobile
import Automobile as Auto

# Possiamo dare dei tipi specifici alle variabili (opzionale)
def crea_auto(marca: str, modello: str):

    # auto è la variabile, Auto è il file Automobile.py e Automobile è la classe
    auto = Auto.Automobile(marca, modello)
    auto.stampa_info()
    return auto

# Funzione per istanziare gli oggetti della classe
def main():

    # Dichiariamo una lista
    lista_auto = []

    # Ciclo
    while True:

        # input per la marca della macchina
        marca = input("Inserisci la marca (Q per uscire): ")

        # Se uguale a "q" esce dal ciclo
        if marca.lower() == "q":
            break

        # Input del modello
        modello = input("Inserisci il modello: ")

        # Chiama la funzione con i due input come parametri
        # e aggiunge alla lista i valori restituiti
        lista_auto.append(crea_auto(marca, modello))

    # Stampa il totale delle auto in lista
    print(f"\nAuto in lista: {len(lista_auto)}")

    # Cicla per stampare le info
    for auto in lista_auto:
        auto.stampa_info()

# Chiamata alla funzione main
main()