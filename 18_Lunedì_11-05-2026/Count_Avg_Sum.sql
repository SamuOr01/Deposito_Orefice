/*
Le funzioni di aggregazione in SQL vengono utilizzate per eseguire
calcoli su un insieme di righe e restituire un singolo valore come risultato.

Tra le più importanti troviamo:

| Funzione  | Descrizione                 |
| --------- | --------------------------- |
| `COUNT()` | Conta il numero di record   |
| `AVG()`   | Calcola la media dei valori |
| `SUM()`   | Calcola la somma dei valori |

Tutte queste funzioni possono essere combinate con la clausola WHERE per filtrare i dati
prima del calcolo.


La funzione COUNT() restituisce il numero di record selezionati da una query.

Sintassi:
*/

SELECT COUNT(column_name)
FROM table_name
WHERE condition;

/*
Può essere utilizzata anche con * per contare tutte le righe della tabella.

Esempio:
*/

SELECT COUNT(*)
FROM Customers;

--Questa query restituisce il numero totale di clienti presenti nella tabella.


/*
La funzione AVG() calcola il valore medio di una colonna contenente valori numerici.

Sintassi:
*/

SELECT AVG(column_name)
FROM table_name
WHERE condition;

--Esempio:

SELECT AVG(Price)
FROM Products;

--Questa query restituisce il prezzo medio dei prodotti.


/*
La funzione SUM() calcola la somma totale dei valori presenti in una colonna numerica.

Sintassi:
*/

SELECT SUM(column_name)
FROM table_name
WHERE condition;

--Esempio:

SELECT SUM(Price)
FROM Products;

--Questa query restituisce la somma totale di tutti i prezzi presenti nella tabella Products.