/*
Sono delle funzioni che restituiscono rispettivamente il valore minimo e
il valore massimo di una colonna, hanno lo stesso tipo di sintassi:
*/

SELECT MIN(column_name)
FROM table_name
WHERE condition;

/*
Nel prossimo esempio prenderemo il prezzo più alto da una tabella di
prodotti e assoceremo il risultato ad un nome temporaneo tramite la
parola chiave AS (ovvero un ALIAS):
*/

SELECT MAX(Price) AS LargestPrice
FROM Products;