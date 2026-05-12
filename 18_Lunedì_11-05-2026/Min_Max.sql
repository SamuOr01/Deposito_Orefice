/*
Le funzioni MIN() e MAX() sono funzioni di aggregazione in SQL
che permettono di ottenere rispettivamente:

- il valore più piccolo di una colonna;
- il valore più grande di una colonna.

Queste funzioni lavorano su un insieme di righe e restituiscono
un singolo valore.
*/

--La funzione MIN() restituisce il valore minimo presente in una colonna.

SELECT MIN(column_name)
FROM table_name
WHERE condition;

--La funzione MAX() restituisce il valore massimo presente in una colonna.

SELECT MAX(column_name)
FROM table_name
WHERE condition;


/*
Nel seguente esempio viene individuato il prezzo più alto presente nella
tabella Products.
*/

SELECT MAX(Price) AS LargestPrice
FROM Products;

/*
In questa query:

MAX(Price) calcola il valore massimo della colonna Price;
AS LargestPrice assegna un alias al risultato per renderlo più leggibile.

Il risultato sarà una singola colonna chiamata LargestPrice contenente il prezzo più alto.
SELECT MAX(Price) AS LargestPrice
FROM Products;
*/