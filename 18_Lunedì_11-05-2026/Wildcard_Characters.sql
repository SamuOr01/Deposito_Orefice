/*
I metacaratteri (o wildcards) sono simboli speciali utilizzati in SQL
per rappresentare uno o più caratteri all’interno di una stringa.

Vengono usati principalmente nelle condizioni WHERE insieme all’operatore LIKE,
e permettono di effettuare ricerche “flessibili” sui dati testuali.

I due metacaratteri più comuni sono:

- "%" -> zero o più caratteri ("bl%" = bl, black, blue e blob);
- "_" -> un singolo carattere ("h_t" = hot, hat e hit);

Altri metacaratteri più avanzati richiedono l’uso di espressioni regolari, "REGEXP_LIKE(colonna, pattern)"

- "[]" -> ogni singolo carattere all'interno delle parentesi ("h[oa]t" = hot e hat);
- "^" -> qualsiasi carattere non compreso tra parentesi ("h[^oa]t" = hit);
- "-" -> qualsiasi carattere all'interno del range specificato ("c[a-b]t" = cat e cbt);

I metacaratteri possono essere combinati per creare pattern più complessi

Ad esempio '_r%' significa:

- "_" -> qualsiasi primo carattere;
- "r" -> seconda lettera fissa;
- "%" -> qualsiasi sequenza successiva.

Corrisponde quindi a valori come:

- tree
- crab
- grape

(purché la seconda lettera sia r)
*/