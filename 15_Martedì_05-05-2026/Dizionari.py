# I dizionari sono una struttura composta da coppie di chiavi-valori,
# sono di tipo dict, sono racchiusi tra parentesi graffe { } e sono
# ordinati e modificabili

studente = {
    "nome": "Alice",
    "età": 20,
    "sesso": "Femmina"
}

# Possiamo accedere ai valori di un dizionario utilizzando le chiavi corrispondenti:

print(studente["nome"]) # Output: "Alice"
print(studente["età"]) # Output: 20

# Possiamo modificare il valore associato a una chiave di un dizionario
# assegnando un nuovo valore a quella chiave.

studente["età"] = 21
print(studente) # Output: {'nome': 'Alice', 'età': 21, 'sesso':'Femmina'}

# Possiamo aggiungere nuove coppie chiave-valore a un dizionario assegnando
# un valore a una nuova chiave.

studente["città"] = "Roma"
print(studente) # Output: {'nome': 'Alice','età': 21,'sesso':'Femmina', 'città': 'Roma'}

# Python fornisce una varietà di metodi incorporati per lavorare con i dizionari.
# - keys() per ottenere una lista di tutte le chiavi
# - values() per ottenere una lista di tutti i valori
# - items() per ottenere una lista di tutte le coppie chiave-valore
# - get() per ottenere il valore associato a una chiave (senza generare un errore se la chiave non esiste)

print(studente.keys()) # Output: dict_keys(['nome', 'età', 'sesso'])
print(studente.values()) # Output: dict_values(['Alice', 20, 'Femmina'])