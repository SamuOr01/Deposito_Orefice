/*
In italiano metacaratteri, sono dei caratteri che servono per sostituire
uno o più caratteri in una stringa.
Vengono utilizzati nelle condizioni come WHERE e LIKE sono:

- "%" -> zero o più caratteri ("bl%" = bl, black, blue e blob);
- "_" -> un singolo carattere ("h_t" = hot, hat e hit);

Il resto dei metacaratteri hanno bisogno della funzione "REGEXP_LIKE(colonna, pattern)"

- "[]" -> ogni singolo carattere all'interno delle parentesi ("h[oa]t" = hot e hat);
- "^" -> qualsiasi carattere non compreso tra parentesi ("h[^oa]t" = hit);
- "-" -> qualsiasi carattere all'interno del range specificato ("c[a-b]t" = cat e cbt);

I metacaratteri possono essere usati in combinazione come ad esempio '_r%' che
rappresenta valori con almeno una r al secondo carattere.
*/