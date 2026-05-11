--È un operatore che cerca un pattern preciso usando anche i metacaratteri:

SELECT column1, column2
FROM table_name
WHERE columnN LIKE pattern;

--In questo esempio seleziona tutti i clienti con il nome che inizia per "a":

SELECT *
FROM Customers
WHERE CustomerName LIKE 'a%';