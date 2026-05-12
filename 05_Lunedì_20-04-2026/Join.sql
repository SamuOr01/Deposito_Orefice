/*
Le JOIN sono clausole utilizzate per combinare dati provenienti da due o più tabelle.

L’unione avviene tramite una colonna comune tra le tabelle, chiamata generalmente:

chiave primaria (Primary Key);
chiave esterna (Foreign Key).

Le JOIN sono fondamentali nei database relazionali, perché permettono di collegare
informazioni distribuite in più tabelle.

Ci sono 4 tipi di join:

| Tipo         | Descrizione                                       |
| ------------ | ------------------------------------------------- |
| `INNER JOIN` | Restituisce solo i record corrispondenti          |
| `LEFT JOIN`  | Restituisce tutti i record della tabella sinistra |
| `RIGHT JOIN` | Restituisce tutti i record della tabella destra   |
| `FULL JOIN`  | Restituisce tutti i record di entrambe le tabelle |
| `CROSS JOIN` | Restituisce tutte le combinazioni possibili       |


La clausola INNER JOIN restituisce solamente i record che possiedono valori corrispondenti in entrambe le tabelle.

Sintassi generale:
*/

SELECT column_name(s)
FROM table1
INNER JOIN table2
    ON table1.column_name = table2.column_name;

--La clausola ON specifica la condizione di collegamento tra le due tabelle.

--Esempio di utilizzo:
SELECT Orders.OrderID,
       Customers.CustomerName,
       Orders.OrderDate
FROM Orders
INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID;

/*
Questa query:

- collega la tabella Orders con la tabella Customers;
- utilizza il campo CustomerID come relazione;
- restituisce solo i record con un CustomerID presente in entrambe le tabelle.

Il result-set finale contiene:

- OrderID della tabella Orders;
- CustomerName della tabella Customers;
- OrderDate della tabella Orders.
*/

--SQL permette di concatenare più JOIN nella stessa query.

SELECT Orders.OrderID,
       Customers.CustomerName,
       Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers
    ON Orders.ShipperID = Shippers.ShipperID);

/*
Questa query collega:

- Orders
- Customers
- Shippers

in un unico result-set.
*/


/*
La clausola LEFT JOIN restituisce:

- tutti i record della tabella di sinistra;
- i record corrispondenti della tabella di destra.

Se non esiste corrispondenza, i valori mancanti vengono riempiti con NULL.

Sintassi:
*/

SELECT column_name(s)
FROM table1
LEFT JOIN table2
    ON table1.column_name = table2.column_name;

--Esempio:
SELECT Orders.OrderID,
       Customers.CustomerName
FROM Customers
LEFT JOIN Orders
    ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

/*
Questa query:

- restituisce tutti i clienti;
- mostra l’eventuale ordine associato;
- mantiene nel risultato anche i clienti senza ordini.


RIGHT JOIN funziona in modo opposto a LEFT JOIN.

Restituisce:

tutti i record della tabella di destra;
i record corrispondenti della tabella di sinistra.

Sintassi:
*/

SELECT column_name(s)
FROM table1
RIGHT JOIN table2
    ON table1.column_name = table2.column_name;


/*
FULL OUTER JOIN restituisce:

- tutti i record della tabella sinistra;
- tutti i record della tabella destra;
- unendo quelli che hanno corrispondenze.

Le righe senza corrispondenza vengono completate con valori NULL.

Sintassi:
*/

SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
    ON table1.column_name = table2.column_name;

/*
Nota: MySQL non supporta direttamente FULL OUTER JOIN.
Spesso viene simulato combinando LEFT JOIN e RIGHT JOIN con UNION.
*/

/*
La clausola CROSS JOIN restituisce tutte le combinazioni possibili
tra le righe delle due tabelle.

Sintassi:
*/

SELECT column_name(s)
FROM table1
CROSS JOIN table2;

/*
Se:

- la prima tabella contiene 3 righe;
- la seconda contiene 4 righe;

il risultato avrà 3 × 4 = 12 righe.
*/