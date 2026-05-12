/*
La clausola ORDER BY viene utilizzata per ordinare i dati restituiti da una query SQL.

L’ordinamento può essere effettuato su una o più colonne e può seguire due criteri:

ASC → ordine crescente;
DESC → ordine decrescente.

La sintassi generale è:
*/

SELECT column1, column2
FROM table_name
ORDER BY column1 ASC|DESC;

/*
Per impostazione predefinita, SQL utilizza l’ordinamento crescente (ASC),
quindi specificarlo non è obbligatorio.

Esempio di ordinamento crescente:
*/

SELECT *
FROM world.country
ORDER BY Name ASC;

--Questa query restituisce i Paesi ordinati alfabeticamente in base alla colonna Name.

--Esempio di ordinamento decrescente:

SELECT *
FROM world.country
ORDER BY Population DESC;

--In questo caso i risultati vengono ordinati dalla popolazione più alta alla più bassa.

/*
ORDER BY permette anche di ordinare i risultati utilizzando più colonne contemporaneamente.

SQL applica gli ordinamenti nell’ordine in cui le colonne vengono specificate:

- ordina secondo la prima colonna;
- in caso di valori uguali, utilizza la seconda colonna;
- e così via.

La sintassi è:
*/

SELECT column1, column2
FROM table_name
ORDER BY column1, column2;


--Esempio pratico:
SELECT *
FROM world.country
ORDER BY Region, SurfaceArea DESC;

/*
Questa query:

- ordina i record in base alla colonna Region;
- per le righe appartenenti alla stessa regione, ordina ulteriormente i risultati in base alla colonna SurfaceArea in ordine decrescente.

Di conseguenza, all’interno di ogni regione compariranno prima i Paesi con superficie maggiore.
*/

/*
L’ordinamento si comporta diversamente a seconda del tipo di dato:

- stringhe → ordinamento alfabetico;
- numeri → ordinamento numerico;
- date → ordinamento cronologico.

Esempi:

| Tipo    | Esempio                    |
| ------- | -------------------------- |
| Stringa | `ORDER BY Name`            |
| Numero  | `ORDER BY Population DESC` |
| Data    | `ORDER BY BirthDate ASC`   |
*/