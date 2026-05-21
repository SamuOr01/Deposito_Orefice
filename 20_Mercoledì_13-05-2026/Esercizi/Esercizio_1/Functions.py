import numpy as np
from numpy import random
from datetime import datetime


def salva_txt(descrizione):

    now = datetime.now()
    giorno = now.day
    mese = now.month
    anno = now.year
    ore = now.hour
    minuti = now.minute

    filename = f"{giorno}-{mese}-{anno}_{ore}-{minuti}.txt"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(descrizione)

# Parte 1

# Punto 1.1 - Funzione per la creazione della matrice
def crea_matrice(i_range, f_range, dim1, dim2):

    # Il range iniziale non deve essere maggiore di quello finale
    if i_range >= f_range:
        raise ValueError("Range non valido")

    # Le dimensioni della matrice non devono essere minori o uguali a zero
    if dim1 <= 0 or dim2 <= 0:
        raise ValueError("Dimensioni non valide")

    # Crea la matrice
    matrice = random.randint(i_range, f_range, size = [dim1, dim2])

    # Restituisce la matrice
    return matrice

# Punto 1.2 - Estrazione sotto-matrice centrale
def estrai_sotto_matrice_centrale(matrice):

    # Ottengo la dimensione delle righe e delle colonne
    righe = matrice.shape[0]
    colonne = matrice.shape[1]

    # La matrice non deve avere meno di 2 righe e colonne
    if righe < 2 or colonne < 2:
        return None

    else:
        # Estrae la sotto-matrice
        sotto_matrice = matrice[(righe // 2) - 1:(righe // 2) + 1, (colonne // 2) - 1:(colonne // 2) + 1]
        return sotto_matrice

# Punto 1.3 - matrice trasposta
def matrice_trasposta(matrice):
    trasposta = np.transpose(matrice)
    return trasposta

# Punto 2.3 - Determinate della matrice
def determinante_matrice_quadrata(matrice):
    righe = matrice.shape[0]
    colonne = matrice.shape[1]

    # Se la matrice è quadrata calcola il determinante
    if righe == colonne:
        determinante = np.linalg.det(matrice)
        return determinante
    else:
        return None

# Punto 3.1 - Calcola la matrice inversa
def matrice_inversa(matrice):
    righe = matrice.shape[0]
    colonne = matrice.shape[1]

    # Se la matrice è quadrata calcola la matrice inversa
    if righe == colonne:
        try:
            inversa = np.linalg.inv(matrice)
            return inversa
        except np.linalg.LinAlgError:
            return None
    else:
        return None

# Punto 3.2 - Applica una funzione matematica alla matrice
def applica_funzione_matematica(matrice, funzione):
    if funzione == "sin":
        return np.sin(matrice)
    elif funzione == "cos":
        return np.cos(matrice)
    elif funzione == "exp":
        return np.exp(matrice)
    elif funzione == "log":
        return np.log(matrice)

# Punto 3.3 - Filtra gli elementi tramite Boolean Indexing
def filtra_elementi_matrice(matrice, soglia):
    return matrice[matrice > soglia]

# Funzione di utility per verificare l'esistenza della matrice
def check_matrice(matrice):
    if matrice is None:
        print("Per eseguire questa operazione devi prima aver creato una matrice")
        print("Seleziona 1")
        return False

    else:
        return True