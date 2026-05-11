/*
L'istruzione WHERE è definita una "clausula", serve per mettere una condizione
in modo da filtrare i record che andranno nel result-set.
*/

SELECT column1, column2
FROM table_name
WHERE condition;

/*
Le condizioni possono essere di vario tipo e vanno scritte insieme all'operatore WHERE,
ad esempio con valori stringa che vanno scritti tra singoli apici come ('testo').
*/

SELECT *
FROM world.country
WHERE Region ='Antarctica';

--Un altro esempio può essere con un valore numerico:

SELECT *
FROM world.country
WHERE Population=0;

/*
Le operazioni che si possono fare come condizione sono:

- = -> uguale;
- > -> maggiore di;
- < -> minore di;
- >= -> maggiore uguale di;
- <= -> minore uguale di;
- <> -> non uguale(in alcune versione di SQL si scrive "!=", in altre ancora
        accetta entrambe le scritture come in MySQL);
- BETWEEN -> tra un certo intervallo ("BETWEEN 0 and 10", valori compresi);
- LIKE -> cerca un pattern, ovvero cerca una eguaglianza parziale o totale
          specificando il pattern fisso da trovare e le parti del dato variabili
          con un metacarattere come il "%" (esempio: "City LIKE 's%' " per trovare
          i valori che iniziano con "s" o "S");
- IN -> per specificare più valori possibili (esempio "IN (0, 1000)");
*/

/*
Un campo con valore NULL è un campo senza valore che è diverso da un valore zero
o da un campo che contiene spazi.
Un campo con un valore NULL è un campo che è stato lasciato vuoto durante la
creazione di record.
Non è possibile verificare i valori NULL con operatori di confronto (come =, < o <>).
Bisogna usare gli operatori IS NULL & IS NOT NULL.
*/

SELECT column_names
FROM table_name
WHERE column_name IS NULL;

/*
Questi operatori permettono di combinare più condizioni, stanno ad indicare:

- AND -> visualizza il record se tutte le condizioni da sono soddisfatte;
- OR -> visualizza il record se almeno una condizione è soddisfatta;
- NOT -> visualizza il record se la condizione NON sono soddisfatte;
*/

SELECT column1, column2
FROM table_name
WHERE condition1 AND condition2 AND condition3;

/*
Questi operatori possono essere affiancati da parentesi per indicare un gruppo
di condizioni
*/

SELECT *
FROM table_name
WHERE condition1 AND (condition2 OR NOT condition3);