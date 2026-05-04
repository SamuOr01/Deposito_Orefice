# La gestione dei file in python è fondamentale per leggere e scrivere dati sui file,
# Python fornisce una serie di funzioni di input/Output (I/O)

# Per iniziare a lavorare su un file bisogna aprirlo.
# La funzione open() accetta 2 parametri:
# - Il percorso del file
# - La modalità di apertura
file = open("13_Giovedì_30-04-2026\\Ciao.txt", "r") # Aperto in modalità di lettura

# Dopo aver aperto il file in modalità di lettura è possibile leggere il contenuto:
contenuto = file.read() # Legge l'intero contenuto
riga = file.readline() # Legge una singola riga
print(riga)

# Per scrivere dati su un file, è necessario aprire il file in modalità scrittura o aggiunta:
# - La modalità di scrittura "w" sovrascrive il contenuto del file esistente
# - La modalità di aggiunta "a" aggiunge il contenuto alla fine del file.
file = open("13_Giovedì_30-04-2026\\Ciao.txt", "w") # Apertura in modalità scrittura

# È possibile scrivere dati su un file utilizzando il metodo write().
file.write("Questo è un esempio di scrittura su file")

# Importante chiudere sempre il file, la chiusura del file libera le risorse associate
# e consente ad altri programmi o processi di accedere al file.
file.close() # Chiusura file

# Per semplificare possiamo usare with, che si occupa automaticamente di aprire e chiudere il file
with open("13_Giovedì_30-04-2026\\Ciao.txt", "r") as file:
    contenuto = file.read()


# Tabella delle modalità:
# 'r' - Lettura (default)
# 'w' - Scrittura, Se il file non esiste lo crea, altrimenti cancella il contenuto del file.
# 'a' - Append, Aggiunge il contenuto alla fine del file.
# 'x' - Creazione esclusiva, Crea un nuovo file, ma restituisce un errore se il file esiste già.
# 'r+' - Modifica, Permette di leggere e scrivere contemporaneamente.
# 'w+' - Modifica, Permette di leggere e scrivere contemporaneamente. Cancella il contenuto del file.


# Possiamo avere anche i dettagli del file.
# Utilizzando la funzione getcwd() della libreria os possiamo chiedere il path del file