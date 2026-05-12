/*
Gli alias in SQL servono per assegnare un nome temporaneo a elementi
di una query, come:

- colonne
- tabelle
- risultati di funzioni o espressioni

Questo nome temporaneo viene utilizzato solo durante l’esecuzione
della query e non modifica la struttura del database.

Gli alias sono utili in diverse situazioni:

- quando una query coinvolge più tabelle;
- quando si utilizzano funzioni o calcoli;
- quando i nomi delle colonne sono lunghi o poco leggibili;
- quando si combinano più colonne in un’unica espressione.

Per creare un alias si utilizza la parola chiave AS.

Sintassi generale:
*/

SELECT column_name AS alias_name
FROM table_name AS alias_table;