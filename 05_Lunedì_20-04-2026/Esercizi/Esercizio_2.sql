/*
Esercizio sui comandi SQL: GROUP BY, ORDER BY e INSERT INTO
Si consideri un database che contiene informazioni su una libreria.
Nel database è presente una tabella chiamata Libri con la seguente struttura:
Libri ( 
	id INT PRIMARY KEY,
    titolo VARCHAR(100), 
    autore VARCHAR(100), 
    genere VARCHAR(50), 
    prezzo DECIMAL(5,2), 
    anno_pubblicazione INT
    )
    
1) Inserimento dati (INSERT INTO)
Inserire almeno 6 nuovi libri nella tabella Libri usando il comando SQL INSERT INTO.
I libri devono appartenere a generi e autori diversi, ed essere pubblicati in anni differenti.

2) Aggregazione e raggruppamento (GROUP BY)
Scrivere una query che, usando il comando GROUP BY, mostri per ogni genere:
- il numero totale di libri presenti;
- il prezzo medio dei libri appartenenti a quel genere.
La query dovrà restituire il risultato ordinato alfabeticamente per genere.

3) Ordinamento risultati (ORDER BY)
Scrivere una query che elenchi tutti i libri pubblicati dopo l’anno 2010
ordinati in modo decrescente per anno di pubblicazione e,
in caso di anno uguale, in ordine crescente per prezzo.
*/

#1
INSERT INTO Libri (id, titolo, autore, genere, prezzo, anno_pubblicazione) VALUES
(1, 'Il nome della rosa', 'Umberto Eco', 'Romanzo', 12.50, 1980),
(2, '1984', 'George Orwell', 'Distopico', 10.00, 2011),
(3, 'Il Signore degli Anelli', 'J.R.R. Tolkien', 'Fantasy', 25.00, 1954),
(4, 'La solitudine dei numeri primi', 'Paolo Giordano', 'Romanzo', 14.00, 2013),
(5, 'Harry Potter e la pietra filosofale', 'J.K. Rowling', 'Fantasy', 18.00, 1997),
(6, 'Sapiens', 'Yuval Noah Harari', 'Saggio', 20.00, 2011);

#2
# raggruppa i libri per genere
# conta quanti libri ci sono per ciascun genere
# calcola il prezzo medio
SELECT genere, COUNT(titolo) AS numero_libri, AVG(prezzo) AS prezzo_medio
FROM Libri
# ordina i risultati in ordine alfabetico per genere
GROUP BY genere
ORDER BY genere ASC;

#3
# seleziona i libri pubblicati dopo il 2010
SELECT titolo, anno_pubblicazione, prezzo
FROM Libri
# li ordina: prima per anno (dal più recente al più vecchio) poi, a parità di anno, per prezzo (dal più economico al più caro)
WHERE anno_pubblicazione > 2010
ORDER BY anno_pubblicazione DESC, prezzo ASC;