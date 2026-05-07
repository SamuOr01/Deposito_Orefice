def salva_catalogo(lista_catalogo):

    with open("catalogo.txt", "w", encoding="utf-8") as f:
        for item in lista_catalogo:
            f.write(f"{item}\n")

def carica_catalogo():

    lista_catalogo = []

    try:
        with open("catalogo.txt", "r", encoding="utf-8") as f:
            for line in f:
                lista_catalogo.append(line.strip())
    except FileNotFoundError:
        pass

    return lista_catalogo