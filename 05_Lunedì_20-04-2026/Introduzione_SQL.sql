/*
Structured Query Language, abbreviato in SQL, è un linguaggio utilizzato
per creare, modificare, gestire e interrogare database relazionali.

Si tratta di un DSL (Domain Specific Language), cioè un linguaggio progettato
per uno scopo specifico: comunicare con i sistemi di gestione dei database relazionali,
chiamati RDBMS (Relational Database Management System).

Per utilizzare SQL è necessario un DBMS (Database Management System), ovvero un software che permette di:

- creare database;
- memorizzare dati;
- modificare informazioni;
- effettuare interrogazioni in modo efficiente.

Il DBMS viene spesso definito anche motore o gestore del database.

Nel nostro caso utilizzeremo MySQL, uno dei DBMS relazionali più diffusi.

MySQL è composto principalmente da:

un server, che gestisce i database;
un client, attraverso cui l’utente invia comandi SQL.

È un software multipiattaforma disponibile su numerosi sistemi operativi, come Linux, Windows e macOS.
Molte distribuzioni Linux moderne utilizzano oggi MariaDB, un fork compatibile con MySQL.

MySQL supporta numerosi linguaggi e tecnologie, tra cui:

- Java
- PHP
- Python
- .NET
- ODBC

Un database relazionale può essere visto come un insieme di tabelle collegate tra loro tramite relazioni.

Ogni tabella è composta da:

- colonne -> rappresentano gli attributi dei dati;
- righe (o record) -> rappresentano le singole informazioni salvate.

L’interrogazione di un database avviene tramite una query.

Una query è un’istruzione SQL che viene inviata al database per richiedere informazioni o modificare dati.
Il risultato di una query viene generalmente restituito sotto forma di tabella.
*/

--Esempio:

SELECT * FROM world.country;

--Questa query seleziona tutte le colonne (*) della tabella country presente nel database world.


--È possibile recuperare solo alcune colonne invece dell’intera tabella.

--Esempio:

SELECT Continent
FROM world.country;

--In questo caso viene restituita soltanto la colonna Continent della tabella country.


/*
SQL possiede una sintassi molto rigorosa ma, nella maggior parte dei DBMS, non distingue
tra maiuscole e minuscole per quanto riguarda i comandi.

Ad esempio:

SELECT e select

sono equivalenti.

Tuttavia, nomi di tabelle e colonne possono essere sensibili al maiuscolo/minuscolo a seconda
del sistema operativo e del DBMS utilizzato.

Molti database richiedono il punto e virgola (;) alla fine di ogni istruzione SQL.

Il punto e virgola serve a separare più istruzioni eseguite nella stessa sessione.

Esempio:
*/

SELECT * FROM world.country;


/*
Alcuni dei comandi SQL più importanti:

| Comando           | Descrizione                |
| ----------------- | -------------------------- |
| `SELECT`          | Estrae dati da un database |
| `INSERT INTO`     | Inserisce nuovi dati       |
| `UPDATE`          | Aggiorna dati esistenti    |
| `DELETE`          | Elimina dati               |
| `CREATE DATABASE` | Crea un database           |
| `DROP DATABASE`   | Elimina un database        |
| `CREATE TABLE`    | Crea una tabella           |
| `ALTER TABLE`     | Modifica una tabella       |
| `DROP TABLE`      | Elimina una tabella        |
| `CREATE INDEX`    | Crea un indice             |
| `DROP INDEX`      | Elimina un indice          |

In SQL è possibile inserire commenti per rendere il codice più leggibile.

Per il commento su una singola riga si utilizza --.

Esempio:
*/

-- selezioniamo tutte le colonne
SELECT * FROM table_name;


--Per commenti più lunghi o multilinea si utilizzano /* e */.

--Esempio:

/*
Selezioniamo tutte le colonne
della tabella specificata
*/
SELECT * FROM world.country;