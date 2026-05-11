--L'istruzione SELECT serve per selezionare i dati da un database.

SELECT * FROM table_name;

--I dati restituiti vengono archiviati in una tabella temporanea, denominata result-set.

SELECT column1, column2
FROM table_name;

/*
Con SELECT andiamo a selezionare le colonne di una tabella andando a specificare
il nome, invece il "*" serve ad indicare tutte le colonne. Con la "," possiamo
selezionare più colonne contemporaneamente.
*/

/*
L'istruzione SELECT DISTINCT funziona esattamente come SELECT solo che restituisce
valori distinti tra loro, quindi senza ripetizioni.
*/

SELECT DISTINCT column1, column2
FROM table_name;

/*
Con SELECT DISTINCT possiamo ad esempio sapere il numero di valori unici di una
colonna usando il comando COUNT che conta i valori.
*/

SELECT COUNT(DISTINCT Name)
FROM world.country;