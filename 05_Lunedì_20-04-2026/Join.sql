/*
È una clausula che viene utilizzata per combinare righe da due o più tabelle,
in base a una colonna correlata tra di loro.
*/

SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers
    ON Orders.CustomerID=Customers.CustomerID;

/*
In questo esempio stiamo andando a prendere i record che hanno lo stesso valore
CustomerID unendo i valori selezionati generando un result-set con 3 colonne:

1.OrderID della tabella orders
2.CustomerName della tabella customers
3.OrderDate della tabella orders
*/

/*
Ci sono 4 tipi di join:

- (INNER) JOIN: restituisce record con valori in comune
- LEFT (OUTER) JOIN: restituisce tutti i record della tabella di sinistra
  e i record con valori in comune
- RIGHT (OUTER) JOIN: restituisce tutti i record della tabella di destra
  e i record con valori in comune
- FULL (OUTER) JOIN: restituisce tutti i record quando è presente una
  corrispondenza in uno dei due a sinistra o nella tabella a destra
*/


--INNER JOIN seleziona i record con valori corrispondenti in entrambe le tabelle.

SELECT column_name(s)
FROM table1
INNER JOIN table2
    ON table1.column_name = table2.column_name;

--Esempio di utilizzo:
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID;

--Esempio di utilizzo con più join (da notare le parentesi):
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers
    ON Orders.ShipperID = Shippers.ShipperID);


/*
Questi join restituiscono i record della tabella di riferimento (Left o Right
in base al tipo di join) insieme ai record che con i valori corrispondenti.
*/

SELECT column_name(s)
FROM table1
LEFT JOIN table2
    ON table1.column_name = table2.column_name;

/*
Un esempio dove recuperiamo e ordiniamo tutti i clienti in aggiunta
recuperiamo anche l'eventuale id dell'ordine:
*/

SELECT Orders.OrderID, Customers.CustomerName
FROM Customers
LEFT JOIN Orders
    ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName;


--CROSS JOIN restituisce tutti i record da entrambe le tabelle.
SELECT column_name(s)
FROM table1
CROSS JOIN table2;