/*
L’istruzione UPDATE viene utilizzata per modificare i dati già
presenti all’interno di una tabella.

Con UPDATE possiamo aggiornare uno o più valori di record esistenti
senza doverli eliminare e reinserire.

La sintassi generale è:
*/

UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;

/*
La clausola SET serve a specificare quali colonne devono essere modificate
e quali nuovi valori devono essere assegnati.

La sintassi è:
*/

SET column_name = value

/*
È possibile aggiornare:

- una singola colonna;
- più colonne contemporaneamente.

Esempio:
*/

UPDATE Customers
SET City = 'Rome'
WHERE CustomerID = 1;

--Questa query modifica il valore della colonna City del cliente con CustomerID = 1.

/*
La clausola WHERE è estremamente importante nelle query UPDATE, perché
permette di selezionare quali record devono essere modificati.

Senza WHERE, SQL aggiornerà tutte le righe della tabella.

Esempio pericoloso:
*/

UPDATE Customers
SET City = 'Berlin';

/*
Questa query imposterà la città Berlin per tutti i clienti della tabella.

Per questo motivo è buona pratica:

- verificare sempre la condizione;
- eseguire prima una SELECT per controllare i record interessati.
*/