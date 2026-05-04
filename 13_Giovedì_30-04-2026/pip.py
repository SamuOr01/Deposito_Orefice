# Una libreria è un insieme di nomi di funzioni o di variabili raggruppate per scopo.

# Vedremo l'utilizzo di 3 librerie in particolare per l'analisi dei dati:
# Numpy - Libreria di analisi dei dati
# Pandas - Libreria per la pulizia o preanalisi dei dati
# Matplotlib - Libreria per la visualizzazione dei dati

# PIP è l'acronimo di "Pip Installs Packages" o "Preferred Installer Program" (Cambia sempre),
# installato insieme a python è il sistema di gestione dei pacchetti utilizzato da quest'ultimo per installare e gestire pacchetti software.

# PIP permette agli sviluppatori di Python di installare facilmente pacchetti e dipendenze da PyPI, il Python Package Index,
# che è un repository di software per il linguaggio di programmazione Python.

# PIP esegue 5 operazioni principali:
# 1. Installazione di pacchetti da PyPI o da altre fonti a patto che rispettino le normative imposte da Python:
#   - Il pacchetto deve poter essere modificabile dal developer
#   - Deve essere open source e testabile
# 2. Gestione delle dipendenze, se sono necessarie ulteriori librerie per far funzionare un pacchetto, Pip le installa automaticamente
# 3. Aggiornamento e rimozione dei pacchetti, con PIP possiamo aggiornare o rimuove i pacchetti
# 4. Gestione delle versioni, PIP permette di installare versioni specifiche dei pacchetti e supporta l'upgrade o il downgrade delle versioni
# 5. (Solo per conoscenza) Integrazione con ambienti virtuali, PIP può essere usatto all'interno di ambienti virtuali per creare ambienti isolati
#   permenttendo una gestione indipendente delle dipendenze delle librerie nei progetti

# Adesso installiamo le 3 librerie
# Per fare ciò apriamo il prompt dei comandi e digitiamo:

# Per installazione singola

# pip install numpy
# pip install pandas
# pip install matplotlib

# Oppure per installazione multipla

# pip install numpy, pandas, matplotlib

# Una volta installate, possiamo importarle nello script:
import numpy as np
import pandas as pd
import matplotlib as plt

# Utilizziamo gli alias per importare le librerie, questo ci consente di risparmiare tempo nella digitazione delle funzioni della libreria.