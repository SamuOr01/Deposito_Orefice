from GestioneDati import InputUtente
from GestioneVendite import GestioneVendite

lista_importi = InputUtente().prendi_input()

g_v = GestioneVendite(lista_importi)

print(g_v.totale_vendite())