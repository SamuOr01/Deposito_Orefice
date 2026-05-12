/*
L’operatore BETWEEN viene utilizzato per selezionare valori compresi
all’interno di un intervallo.

Può essere applicato a:

- valori numerici
- stringhe
- date

Una caratteristica importante è che BETWEEN è inclusivo, cioè include
sia il valore iniziale che quello finale dell’intervallo.

Sintassi generale
*/

SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;


/*
BETWEEN può essere combinato con altre clausole logiche come AND o
operatori come IN.

Esempio:
*/

SELECT *
FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID NOT IN (1, 2, 3);

/*
Questa query:

- seleziona i prodotti con prezzo tra 10 e 20;
- esclude quelli appartenenti alle categorie 1, 2 e 3.
*/


/*
BETWEEN è molto utilizzato anche con i valori di tipo data.

Esempio:
*/

SELECT *
FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';

--Questa query restituisce tutti gli ordini effettuati nel mese di luglio 1996.


/*
A seconda del DBMS, le date possono essere scritte in modi diversi.

Esempio (formato alternativo):
*/

SELECT *
FROM Orders
WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;

--Oppure nel formato standard ISO (consigliato):

SELECT *
FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';


/*
È possibile negare l’intervallo utilizzando NOT BETWEEN.

Esempio con Order By e Not Between:
*/

SELECT *
FROM Products
WHERE ProductName NOT BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;

/*
Questa query restituisce tutti i prodotti il cui nome non rientra nell’intervallo
alfabetico specificato.
*/