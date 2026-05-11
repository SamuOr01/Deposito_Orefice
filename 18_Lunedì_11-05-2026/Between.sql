/*
È un operatore che seleziona i valori (come: numeri, testo o date)
all'interno di un determinato intervallo. L'operatore è inclusivo
ovvero sono inclusi i valori di inizio e fine.
*/

SELECT column_name(s)
FROM table_name
WHERE column_name
    BETWEEN value1 AND value2;

--Un esempio di utilizzo con più condizioni:
SELECT *
FROM Products
WHERE Price
    BETWEEN 10 AND 20 AND CategoryID NOT IN (1,2,3);

--Un esempio utilizzando le date:
SELECT *
FROM Orders
WHERE OrderDate
    BETWEEN #07/01/1996# AND #07/31/1996#;

--Un'altra sintassi per le date è:
SELECT *
FROM Orders
WHERE OrderDate
    BETWEEN '1996-07-01' AND '1996-07-31';

--Un esempio utilizzando un ORDER BY:
SELECT *
FROM Products
WHERE ProductName
    NOT BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;