/*
È un operatore che consente di specificare più valori in una clausola,
una scorciatoia per più condizioni OR.
*/

SELECT column_name(s)
FROM table_name
WHERE column_name
    IN (value1, value2, ...);

--È possibile inserire anche una table all'interno dei valori possibili:

SELECT column_name(s)
FROM table_name
WHERE column_name
    IN (SELECT STATEMENT);

--Esempi di utilizzo:
SELECT *
FROM Customers
WHERE Country
    IN ('Germany', 'France', 'UK');

-- con NOT:
SELECT *
FROM Customers
WHERE Country
    NOT IN ('Germany', 'France', 'UK');

-- Confrontando valori di una table con un'altra table:
SELECT *
FROM Customers
WHERE Country
    IN (SELECT Country FROM Suppliers);