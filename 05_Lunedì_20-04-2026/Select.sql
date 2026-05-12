/*
L’istruzione SELECT è uno dei comandi fondamentali di SQL e viene utilizzata
per recuperare dati da una tabella presente nel database.

La sintassi base è la seguente:
*/

SELECT * FROM table_name;

/*
In questo caso il simbolo * indica che vogliamo selezionare tutte
le colonne della tabella specificata.

Il risultato restituito dalla query viene salvato temporaneamente
in una tabella virtuale chiamata result-set, cioè l’insieme dei risultati
prodotti dalla query.
*/

/*
Spesso non è necessario recuperare tutte le informazioni di una tabella.
Con SELECT possiamo scegliere solo le colonne che ci interessano specificandone il nome.

Esempio:
*/

SELECT column1, column2
FROM table_name;

/*
In questo caso verranno restituite soltanto le colonne column1 e column2.

La virgola , permette di selezionare più colonne contemporaneamente.

Ad esempio:
*/

SELECT Name, Continent
FROM world.country;

/*
Questa query restituisce il nome dello Stato e il continente associato
per ogni record della tabella country.
*/


/*
L’istruzione SELECT DISTINCT funziona come una normale SELECT, ma elimina i
valori duplicati dal risultato.

La sintassi è:
*/

SELECT DISTINCT column1, column2
FROM table_name;

/*
Questa istruzione restituisce solo combinazioni uniche dei valori selezionati.

Ad esempio:
*/

SELECT DISTINCT Continent
FROM world.country;

/*
Il risultato conterrà ogni continente una sola volta, anche se nella tabella
sono presenti molti Stati appartenenti allo stesso continente.
*/


/*
SQL mette a disposizione diverse funzioni di aggregazione, tra cui COUNT(),
utilizzata per contare i valori.

Combinando COUNT() con DISTINCT possiamo sapere quanti valori unici sono
presenti in una colonna.

Esempio:
*/

SELECT COUNT(DISTINCT Name)
FROM world.country;

/*
Questa query conta quanti nomi distinti sono presenti nella colonna Name
della tabella country.
*/