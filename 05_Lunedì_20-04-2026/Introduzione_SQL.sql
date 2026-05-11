/*
Structured Query Language (SQL) è un linguaggio di interrogazione (query) utilizzato per creare,
modificare e gestire i dati in un database relazionale.
Si tratta di un linguaggio specifico di dominio (DSL) usato per comunicare con i sistemi di gestione
di database relazionali (RDBMS).

SQL: COSA CI SERVE Useremo un DBMS(database management system) ovvero un sistema software progettato
per consentire la creazione, la manipolazione e l'interrogazione efficiente di database, per questo
detto anche "gestore o motore del database". Nello specifico useremo MySQL che si basa sul modello
relazionale quindi un RDBMS (relational database management system).

MySQL o Oracle MySQL è un relational database management system (RDBMS) composto da un client
a riga di comando e un server.
Ambo i costituenti sono multipiattaforma e sono disponibili ufficialmente su tutte le distribuzioni
conosciute, quali Debian, Ubuntu e CentOS, sebbene lo abbiano sostanzialmente sostituito con MariaDB
a partire dal 2012.
È software libero rilasciato a doppia licenza, compresa la GNU General Public License, sviluppato per
essere il più possibile conforme agli standard ANSI SQL e ODBC SQL. I sistemi e i linguaggi di
programmazione che lo supportano sono molto numerosi, fra cui ODBC, Java, Mono, .NET, PHP, Python.

SQL è un linguaggio standard per l'archiviazione, la manipolazione e il recupero dei dati nei database.
Nonostante sia uno standard ANSI/ISO ci sono molte versioni SQL ed estensioni proprietarie dei vari software
di database. Un database si può riassumere in una serie di tabelle identificate con un nome e possono essere
relazionate tra loro, queste tabelle sono divise in colonne per ogni attributo e in righe (record) per le
informazioni che vogliamo salvare.

LE QUERY L'interrogazione di un database avviene mediante una query. Ovvero una espressione o una serie di
espressioni con delle richieste da fare al database per avere una risposta, sotto forma di tabella.

Questa query sta interrogando il database "world" andando a selezionare la tabella "country" dando quindi
come risultato direttamente le righe della tabella country.
*/

SELECT * FROM world.country;

/*
In questo esempio andiamo a recuperare solo la colonna "Continent" della tabella country dando come risultato
una tabella con una singola colonna con solo i valori di Continent di tutte le righe di country.
*/

SELECT Continent
FROM world.country;

/*
SQL è un linguaggio da una sintassi molto specifica che non è sensibile alle variazioni tra MAIUSCOLE e minuscole:
"select" e "SELECT" sono uguali. Non è lo stesso per il nome delle tabelle e delle colonne.
Alcuni sistemi di database richiedono un punto e virgola alla fine di ogni istruzione SQL. Il punto e virgola è il
modo standard per separare ogni istruzione SQL nei database che consentono l'esecuzione di più istruzioni SQL nella
stessa chiamata al server (come MySQL).

Alcuni dei comandi SQL più importanti:

- SELECT -> estrae i dati da un database
- UPDATE -> aggiorna i dati in un database
- DELETE -> elimina i dati da un database
- INSERT INTO -> inserisce nuovi dati in un database
- CREATE DATABASE -> crea un nuovo database
- ALTER DATABASE -> modifica un database
- DROP DATABASE -> elimina un database
- CREATE TABLE -> crea una nuova tabella
- ALTER TABLE -> modifica una tabella
- DROP TABLE -> elimina una tabella
- CREATE INDEX -> crea un indice (chiave di ricerca)
- DROP INDEX -> elimina un indice

In SQL si può commentare una riga inserendo "--" prima del testo da commentare:
*/

-- selezioniamo tutte le colonne
SELECT * FROM table_name -- dalla tabella

È possibile anche fare un commento multi riga inserendolo tra "/*" e "*/".
/* selezioniamo tutte le colonne
SELECT * FROM table_name */
SELECT * FROM world.country -- dalla tabella country del database world