# Classe Libro
class Libro:

    # Inizializzaziopne attributi
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    # Metodo per stampare la descrizione del libro
    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine\n")

# Funzione per creare un libro chiedendo input all'utente
def crea_libri():
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci il nome dell'autore del libro: ")
    pagine = input("Inserisci il numero di pagine del libro: ")

    print()

    libro = Libro(titolo, autore, pagine)
    libro.descrizione()

# Funzione principale che gestisce il flusso del programma
def main():

    numero_libri = int(input("Quanti libri vuoi creare? "))

    print()

    if numero_libri == 0:
        print("\nNon hai creato libri")
    elif numero_libri == 1:
        crea_libri()

        print(f"\nHai creato un libro")
    else:
        for _ in range(numero_libri):
            crea_libri()

        print(f"\nHai creato {numero_libri} libri")

# Chiamata della funzione principale
main()