Use libreria;

#Esercizio 1 – INNER JOIN + WHERE + LIKE
# Visualizzare l’elenco dei libri venduti in almeno un negozio, mostrando:
# titolo del libro, autore, data_vendita, negozio.
# Includere solo i libri il cui autore contiene la stringa “King” (indipendentemente da maiuscole/ minuscole).
SELECT libri.titolo, libri.autore, vendite.data_vendita, vendite.negozio
from libri
INNER JOIN vendite
	ON libri.id = vendite.id_libro
WHERE libri.autore LIKE "%King%";

# Esercizio 2 – LEFT JOIN + WHERE + BETWEEN
# Visualizzare tutti i libri, anche quelli che non hanno ancora vendite registrate, mostrando per ciascuno:
# titolo, anno_pubblicazione, prezzo, data_vendita (se presente).
# Filtrare i risultati per anno_pubblicazione compreso tra 2000 e 2010.
SELECT libri.titolo, libri.anno_pubblicazione, libri.prezzo, vendite.data_vendita
from libri
LEFT JOIN vendite
	ON libri.id = vendite.id_libro
WHERE libri.anno_pubblicazione
	BETWEEN 2000 AND 2010
ORDER BY libri.anno_pubblicazione, libri.prezzo ASC;

# Esercizio 3 – INNER JOIN + WHERE + IN
# Visualizzare i dati dei libri venduti nei negozi appartenenti a una lista specifica:
# ("9 Oriole Lane", "98558 Milwaukee Point", "98016 Esch Trail").
# Mostrare titolo, negozio, quantita, prezzo totale (quantita * prezzo).
SELECT libri.titolo, vendite.quantita, (vendite.quantita * libri.prezzo) AS prezzo_totale, vendite.negozio
FROM libri
INNER JOIN vendite
	ON libri.id = vendite.id_libro
WHERE vendite.negozio
	IN ("9 Oriole Lane", "98558 Milwaukee Point", "98016 Esch Trail");

# Esercizio 4 – RIGHT JOIN + WHERE + LIKE + BETWEEN
# Mostrare tutti i record di vendita, anche quelli che fanno riferimento a libri non più presenti nella
# tabella Libri (caso anomalo).
# Mostrare: titolo (se esiste), data_vendita, prezzo, quantita.
# Includere solo le vendite: avvenute tra il 2020-01-01 e il 2022-12-31
# presso negozi il cui nome contiene la parola “Drive” (case-insensitive).
SELECT libri.titolo, vendite.data_vendita, libri.prezzo, vendite.quantita
FROM libri
RIGHT JOIN vendite
	ON libri.id = vendite.id_libro
WHERE (vendite.data_vendita BETWEEN '2020-01-01' AND '2022-12-31')
  AND (vendite.negozio LIKE '%Drive%');

# Esercizio 5 – INNER JOIN + WHERE combinato
# Mostrare titolo, autore, prezzo e data_vendita dei libri:
# con genere IN (‘Fantasy’, ‘Horror’, ‘Drama’) (ignora i libri con >1 genere)
# pubblicati dopo il 2015,
# venduti in negozi il cui nome contiene ‘Plaza’,
# ordinati dal più recente al più vecchio.
SELECT libri.titolo, libri.autore, libri.prezzo, vendite.data_vendita
FROM libri
INNER JOIN vendite
	ON libri.id = vendite.id_libro
WHERE (libri.genere IN ("Fantasy", "Horror", "Drama"))
	AND (libri.anno_pubblicazione > 2015)
    AND (vendite.negozio LIKE "%Plaza%")
ORDER BY vendite.data_vendita DESC;