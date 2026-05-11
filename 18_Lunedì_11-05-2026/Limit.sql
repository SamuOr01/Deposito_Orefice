/*
L'istruzione SELECT TOP serve per specificare il numero di record da restituire.
Non tutti i sistemi di database supportano questa istruzione. MySQL supporta l'operazione
LIMIT per selezionare un numero limitato di record.
*/

SELECT column_name
FROM table_name
WHERE condition
LIMIT number;

/*
LIMIT quindi ci permette di indicare il numero massimo di record da
recuperare da un database, questa operazione tendenzialmente si esegue
per tabelle con un grande numero di record ottimizzando le prestazioni.
*/

SELECT * FROM Customers
LIMIT 50;