/*
L'istruzione GROUP BY serve ad raggruppare i record con stessi valori
del result-set su una o più colonne.
Viene spesso utilizzato con funzioni per raggruppare il result-set.
*/

SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);


--Esempio Group By
SELECT Country, COUNT(CustomerID)
FROM Customers
GROUP BY Country;


--Esempio Group By con Order By
SELECT Country, COUNT(CustomerID)
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;