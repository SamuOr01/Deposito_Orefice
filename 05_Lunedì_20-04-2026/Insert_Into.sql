--L'istruzione INSERT INTO serve per inserire nuovi record in una tabella.

INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

/*
È possibile non specificare le colonne se aggiungiamo valori a tutte
le colonne ma bisogna assicurarsi che i valori abbiano l'ordine corretto
delle colonne in cui devono essere inseriti.
*/

INSERT INTO table_name
VALUES (value1, value2, value3, ...);