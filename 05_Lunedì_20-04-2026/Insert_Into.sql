/*
L’istruzione INSERT INTO viene utilizzata per inserire nuovi record
all’interno di una tabella del database.

Ogni record inserito corrisponde a una nuova riga della tabella.

La sintassi generale è:
*/

INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

/*
In questa query:

- dopo il nome della tabella vengono specificate le colonne da valorizzare;
- la clausola VALUES contiene i valori che verranno inseriti nelle rispettive colonne.

Specificare esplicitamente le colonne è il metodo più consigliato,
perché rende la query più chiara e sicura.

Esempio:
*/

INSERT INTO Customers (CustomerName, Country, City)
VALUES ('Mario Rossi', 'Italy', 'Catania');

/*
Questa query inserisce un nuovo cliente nella tabella Customers.

Il database assocerà:

- 'Mario Rossi' alla colonna CustomerName;
- 'Italy' alla colonna Country;
- 'Catania' alla colonna City.

Se vogliamo inserire valori in tutte le colonne della tabella,
possiamo omettere l’elenco delle colonne.

Esempio:
*/

INSERT INTO table_name
VALUES (value1, value2, value3, ...);

/*
Tuttavia, in questo caso è fondamentale rispettare esattamente
l’ordine delle colonne definito nella tabella.

Supponiamo di avere una tabella con questa struttura:

| ID | Name | Country |
| -- | ---- | ------- |
| 1  | Luca | Italia   |

*/

--Possiamo inserire un nuovo record con:

INSERT INTO Customers
VALUES (2, 'Anna', 'Francia');

/*
Il risultato sarà:

| ID | Name | Country |
| -- | ---- | ------- |
| 1  | Luca | Italia  |
| 2  | Anna | Francia |

*/

