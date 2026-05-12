/*
L’istruzione utilizzata per limitare il numero di record restituiti da una
query dipende dal sistema di database utilizzato.

In alcuni DBMS esiste SELECT TOP, mentre in altri (come MySQL) si utilizza LIMIT.

La clausola SELECT TOP è utilizzata in alcuni sistemi (ad esempio SQL Server)
per specificare quanti record restituire.

Tuttavia, non è supportata da tutti i database.

Nel caso di MySQL si utilizza invece LIMIT.
*/

SELECT column_name
FROM table_name
WHERE condition
LIMIT number;

/*
LIMIT indica a SQL di restituire solo un numero massimo di righe.

Questo è particolarmente utile quando:

- la tabella contiene molti record;
- si vogliono visualizzare solo anteprime dei dati;
- si ottimizzano le prestazioni delle query;
- si lavora con paginazione dei risultati.
*/

--Esempio
SELECT * FROM Customers
LIMIT 50;

/*
Questa query restituisce al massimo 50 record dalla tabella Customers.
Se la tabella contiene meno di 50 righe, verranno restituite tutte.
*/