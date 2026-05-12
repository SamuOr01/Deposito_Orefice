/*
La clausola WHERE viene utilizzata per applicare condizioni alle query SQL e
filtrare i record restituiti nel result-set.

Grazie a WHERE possiamo selezionare solo le righe che soddisfano una determinata condizione.

La sintassi generale è:
*/

SELECT column1, column2
FROM table_name
WHERE condition;

/*
Le condizioni vengono specificate dopo la clausola WHERE.

Nel caso di valori testuali, le stringhe devono essere racchiuse tra apici singoli (' ').

Esempio:
*/

SELECT *
FROM world.country
WHERE Region = 'Antarctica';

--Questa query restituisce tutti i record della tabella country appartenenti alla regione Antarctica.

/*
La clausola WHERE può essere utilizzata anche con valori numerici.

Esempio:
*/

SELECT *
FROM world.country
WHERE Population = 0;

--In questo caso vengono selezionati tutti i Paesi con popolazione uguale a 0.


/*
SQL mette a disposizione diversi operatori per costruire condizioni:

| Operatore | Significato               |
| --------- | ------------------------- |
| `=`       | Uguale                    |
| `>`       | Maggiore di               |
| `<`       | Minore di                 |
| `>=`      | Maggiore o uguale         |
| `<=`      | Minore o uguale           |
| `<>`      | Diverso da                |
| `BETWEEN` | Compreso in un intervallo |
| `LIKE`    | Ricerca tramite pattern   |
| `IN`      | Confronto con più valori  |

*/

/*
Un valore NULL indica l’assenza di un valore.

È importante distinguere NULL da:

- 0
- una stringa vuota ('')
- uno spazio (' ')

Un campo NULL rappresenta un’informazione mancante o non specificata.

I valori NULL non possono essere confrontati con gli operatori tradizionali (=, <, <>, ecc.).

Per verificare la presenza o l’assenza di valori NULL bisogna utilizzare:

- IS NULL
- IS NOT NULL

Esempio:
*/

SELECT column_names
FROM table_name
WHERE column_name IS NULL;

--Questa query restituisce tutte le righe in cui column_name non contiene alcun valore.


/*
SQL permette di combinare più condizioni tramite operatori logici:

| Operatore | Significato                            |
| --------- | -------------------------------------- |
| `AND`     | Tutte le condizioni devono essere vere |
| `OR`      | Almeno una condizione deve essere vera |
| `NOT`     | Inverte una condizione                 |

L’operatore AND restituisce i record solo se tutte le condizioni sono soddisfatte.

Esempio:
*/

SELECT column1, column2
FROM table_name
WHERE condition1 AND condition2;

/*
L’operatore OR restituisce i record se almeno una delle condizioni è vera.

Esempio:
*/

SELECT *
FROM table_name
WHERE condition1 OR condition2;

/*
L’operatore NOT nega una condizione.

Esempio:
*/

SELECT *
FROM table_name
WHERE NOT condition1;

/*
Le parentesi permettono di raggruppare condizioni e definire l’ordine di valutazione logica.

Esempio:
*/

SELECT *
FROM table_name
WHERE condition1 AND (condition2 OR NOT condition3);

--In questo caso SQL valuta prima l’espressione contenuta tra parentesi.