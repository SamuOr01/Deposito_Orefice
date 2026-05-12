/*
L’operatore IN viene utilizzato per verificare se un valore appartiene a un insieme di valori specificati.

In pratica, rappresenta una scorciatoia per più condizioni OR, rendendo la query più compatta e leggibile.

Sintassi generale
*/

SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);

--Esempio
SELECT *
FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');

/*
Questa query restituisce tutti i clienti che si trovano in uno dei seguenti Paesi:

- Germania
- Francia
- Regno Unito
*/

/*
Uno degli utilizzi più potenti di IN è con una subquery (query annidata),
cioè una query dentro un’altra query.

Sintassi:
*/

SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT statement);

--Esempio con subquery
SELECT *
FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);

/*
Questa query:

- prende tutti i Paesi presenti nella tabella Suppliers;
- restituisce i clienti che provengono da quei Paesi.

In questo caso SQL esegue due passaggi:

- esegue la subquery:
    SELECT Country FROM Suppliers;

- usa il risultato come lista di valori per la query principale.
*/


/*
NOT IN fa l’opposto: esclude i valori specificati.

Esempio:
*/

SELECT *
FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');

--Questa query restituisce tutti i clienti che non provengono da questi Paesi.