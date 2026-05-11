Use gestioneordini;

# Scrivi le query SQL per rispondere alle seguenti richieste:

# 1) - Visualizza, per ogni categoria, il numero totale di vendite effettuate.
SELECT categoria, COUNT(categoria)
from vendite
group by categoria;

# 2) - Mostra, per ogni categoria, il prezzo medio dei prodotti venduti.
select categoria, AVG(prezzo_unitario)
from vendite
GROUP BY categoria;

# 3) - Mostra il totale delle quantità vendute (SUM) per ciascun prodotto.
select prodotto, SUM(quantita)
from vendite
GROUP BY prodotto;

# 4) - Mostra il prezzo massimo e il prezzo minimo tra tutti i prodotti venduti.
SELECT MAX(prezzo_unitario), MIN(prezzo_unitario)
from vendite;

# 5) - Conta quante vendite sono state registrate nella tabella Vendite.
select count(id)
from vendite;

# 6) - I 5 prodotti più costosi (in base al prezzo_unitario)
SELECT prodotto, prezzo_unitario
from vendite
ORDER BY prezzo_unitario DESC
LIMIT 5;

# 7) - Mostra i nomi dei 3 prodotti con la quantità totale più bassa venduta (usa SUM e LIMIT).
