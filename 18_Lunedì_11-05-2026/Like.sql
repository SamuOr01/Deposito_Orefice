/*
L’operatore LIKE viene utilizzato in SQL per cercare un pattern
specifico all’interno di una stringa, spesso combinato con i
metacaratteri % e _.

Questo permette di effettuare ricerche parziali sui dati testuali invece
di confronti esatti.

Sintassi generale
*/

SELECT column1, column2
FROM table_name
WHERE columnN LIKE pattern;

/*
La clausola WHERE viene utilizzata per filtrare i record che corrispondono
al pattern definito.

Il simbolo % rappresenta:

zero caratteri
oppure una sequenza qualsiasi di caratteri

Esempio
*/

SELECT *
FROM Customers
WHERE CustomerName LIKE 'a%';

/*
Questa query seleziona tutti i clienti il cui nome:

- inizia con la lettera a
- oppure con A (a seconda della configurazione del database, che può essere
  case-sensitive o meno)

Il pattern 'a%' significa:

- a -> primo carattere fisso
- % -> qualsiasi sequenza di caratteri successivi

Esempi di corrispondenza:

- anna
- alessandro
- antonio
- a