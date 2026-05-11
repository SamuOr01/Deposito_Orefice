/*
Gli ALIAS SQL servono per assegnare un nome temporaneo ad un elemento
come una tabella, una colonna, il risultato di una funzione ecc ecc...;
In questo modo possiamo richiamare direttamente il nome temporaneo assegnato
all'elemento.

Gli ALIAS possono essere utili quando:

- sono coinvolte più tabelle in una QUERY;
- vengono usate le funzioni in una QUERY;
- i nomi delle colonne sono grandi o poco leggibili;
- due o più colonne vengono combinate insieme;

Per assegnare un ALIAS viene usata la parola chiave AS quando andiamo a
selezione o richiamare in SELECT o in FROM l'elemento a cui assegnare il nome:
*/

SELECT column_name AS alias_columName
FROM table_name AS alias_tableName;