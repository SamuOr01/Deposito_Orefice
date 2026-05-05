# È possibile importare un modulo usando l'istruzione import, così facendo abbiamo
# accesso a tutte le sue classi, variabili o funzioni

# Python offre anche la possibilità di importare specifiche definizioni da un modulo,
# utilizzando la sintassi from modulo import definizione.In questo modo, è possibile importare
# solo le classi o le funzioni necessarie e utilizzarle direttamente senza dover specificare il nome del modulo.

import mio_modulo

mio_modulo.saluta("Alice") # Stampa "Ciao, Alice"

raggio = 2
cerchio = mio_modulo.Cerchio(raggio)
print(cerchio.area()) # Stampa l'area del cerchio con raggio 2