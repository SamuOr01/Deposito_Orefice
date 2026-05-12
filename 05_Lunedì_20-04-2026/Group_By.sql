/*
La clausola GROUP BY viene utilizzata per raggruppare le righe che possiedono
lo stesso valore in una o più colonne.

È spesso usata insieme alle funzioni di aggregazione, cioè funzioni che eseguono
calcoli su gruppi di dati, come:

- COUNT() -> conta i valori;
- SUM() -> somma i valori;
- AVG() -> calcola la media;
- MAX() -> restituisce il valore massimo;
- MIN() -> restituisce il valore minimo.

La sintassi generale è:
*/

SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);

/*
Quando utilizziamo GROUP BY, SQL divide le righe della tabella in gruppi basati
sui valori della colonna specificata.

Successivamente, le funzioni di aggregazione vengono applicate separatamente a ogni gruppo.
*/

SELECT Country, COUNT(CustomerID)
FROM Customers
GROUP BY Country;

/*
Questa query:

- raggruppa i clienti in base alla colonna Country;
- conta quanti clienti appartengono a ciascun Paese tramite COUNT(CustomerID).

Il risultato sarà una tabella con:

- il nome del Paese;
- il numero di clienti presenti in quel Paese.
*/

/*
La clausola GROUP BY viene spesso combinata con ORDER BY per ordinare i gruppi ottenuti.

Esempio:
*/

SELECT Country, COUNT(CustomerID)
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;

/*
Questa query:

- raggruppa i clienti per Paese;
- conta il numero di clienti per ogni gruppo;
- ordina il risultato in ordine decrescente in base al numero di clienti.

Di conseguenza, i Paesi con più clienti compariranno per primi.

Anche se scriviamo la query in un certo ordine, SQL elabora le clausole seguendo una logica precisa:

- FROM -> seleziona la tabella;
- WHERE -> filtra le righe;
- GROUP BY -> crea i gruppi;
- SELECT -> genera il result-set;
- ORDER BY -> ordina il risultato finale.

Comprendere questo flusso è importante per capire il comportamento delle query più complesse.
*/