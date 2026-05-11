/*
L'istruzione ORDER BY serve ad ordinare il result-set su una o più colonne
con due possibili criteri:

- ASC -> crescente
- DESC -> decrescente

Non è obbligatorio specificare il criterio di ordinamento, di default prende
il criterio crescente (ASC).
*/

SELECT column1, column2
FROM table_name
ORDER BY column1, column2 ASC|DESC;

/*
In questo esempio ordiniamo In base alla colonna Region (string) e con ulteriore
ordinamento decrescente in base alla colonna SurfaceArea (int).
Così facendo avremo un result-set ordinato in base alla regione, e le regioni uguali
ordinate in base alla superfice più ampia.
*/

SELECT *
FROM world.country
ORDER BY Region, SurfaceArea DESC;