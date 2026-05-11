/*
L'istruzione DELETE serve per eliminare i record esistenti in una tabella.
Viene tendenzialmente usato insieme a WHERE per filtrare i record da eliminare
altrimenti eliminerebbe tutti i record della tabella.
*/

DELETE FROM table_name
WHERE condition;
/*
Questa istruzione va ad eliminare solo i record, la struttura della tabella
rimane invariata pure se elimiano tutti i record senza specificare una condizione.
*/

DELETE FROM Customers
WHERE CustomerName='Mario Rossi';