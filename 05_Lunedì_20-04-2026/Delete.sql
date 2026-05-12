/*
L’istruzione DELETE viene utilizzata per eliminare uno o più record esistenti all’interno di una tabella.

La sintassi generale è:
*/

DELETE FROM table_name
WHERE condition;

/*
La clausola WHERE permette di specificare quali righe devono essere eliminate.

Nella maggior parte dei casi DELETE viene utilizzato insieme a WHERE per evitare
di cancellare accidentalmente tutti i dati della tabella.

Esempio:
*/

DELETE FROM Customers
WHERE CustomerName = 'Mario Rossi';

/*
Questa query elimina soltanto il record relativo al cliente chiamato Mario Rossi.

Se omettiamo la clausola WHERE, SQL eliminerà tutti i record presenti nella tabella.

Esempio:
*/

DELETE FROM Customers;

/*
Questa istruzione:

- elimina tutte le righe della tabella Customers;
- mantiene però intatta la struttura della tabella.

Di conseguenza:

- le colonne restano presenti;
- i tipi di dato non cambiano;
- la tabella continua a esistere nel database.
*/