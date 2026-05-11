/*
L'istruzione UPDATE serve per modificare i record esistenti in una tabella.
Viene tendenzialmente usato insieme a WHERE per filtrare i record da modificare
altrimenti modificherebbe tutti i record della tabella.
*/

UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;

/*
Con SET andiamo a specificare i valori da cambiare indicando
la colonna con l'assegnazione del valore.
*/

UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;