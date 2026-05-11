/*
Sono delle funzioni che eseguono un calcolo restituendo un valore specifico:

- COUNT() -> restituisce il numero di record selezionati;
- AVG() -> restituisce il valore medio di una colonna con valori numerici;
- SUM() -> restituisce la somma totale di una colonna con valori numerici;

Tutte e tre le funzioni hanno lo stesso tipo di sintassi e possono
essere associate a delle condizioni con WHERE:
*/

SELECT SUM(column_name)
FROM table_name
WHERE condition;