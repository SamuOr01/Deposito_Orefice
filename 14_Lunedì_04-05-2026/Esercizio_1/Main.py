# Import dei moduli creati
from GestioneDati import prendi_input
from GestioneVendite import GestioneVendite
from GestioneFileTxt import crea_file_txt

# Dichiarazione del main
def main():

    # Esecuzione delle operazioni:

    # Input
    data, lista_vendite = prendi_input()

    # gestione vendite
    gv = GestioneVendite(lista_vendite)

    # somma, media, lista sopra la media
    somma = gv.totale_vendite()
    media = gv.media_vendite()
    vendite_sopra_media = gv.vendite_sopra_la_media()

    # File txt
    crea_file_txt(data, lista_vendite, somma, media, vendite_sopra_media)

# chiamata del main
main()