/*
Si considerino le seguenti due tabelle con 20 dati l’una:

1.Clienti ( 
2.	id INT,
3. 	nome VARCHAR(100),
4. 	città VARCHAR(100)
5. )

1.Ordini (
2.	id INT,
3. 	id_cliente INT,
4. 	data_ordine DATE,
5.	importo DECIMAL(7,2)
6. ) 

Le due tabelle sono collegate dalla relazione tra Clienti.id e Ordini.id_cliente.

Esercizio 1 – INNER JOIN Obiettivo: 
Visualizza l’elenco dei clienti che hanno effettuato almeno un ordine.
Per ciascuno, mostra: nome del cliente, data dell’ordine e importo.

Esercizio 2 – LEFT JOIN Obiettivo:
Visualizza tutti i clienti, inclusi quelli che non hanno mai effettuato ordini.
Mostra per ciascuno: nome del cliente, data dell’ordine (se presente) e importo (se presente).

Esercizio 3 – RIGHT JOIN Obiettivo:
Visualizza tutti gli ordini, anche quelli che non hanno un cliente associato (caso anomalo).
Mostra per ciascuno: nome del cliente (se esiste), data dell’ordine e importo.
*/

# Esercizio 1

SELECT DISTINCT nome, data_ordine, importo
FROM gestioneordini.clienti
INNER JOIN gestioneordini.ordini ON clienti.id = ordini.id_cliente;

# Esercizio 2

SELECT DISTINCT nome, data_ordine, importo
FROM gestioneordini.clienti
LEFT JOIN gestioneordini.ordini ON clienti.id = ordini.id_cliente;

# Esercizio 3

SELECT DISTINCT nome, data_ordine, importo
FROM gestioneordini.clienti
RIGHT JOIN gestioneordini.ordini ON clienti.id = ordini.id_cliente;