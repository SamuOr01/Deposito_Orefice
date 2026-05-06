# In Python, filter() è una funzione integrata che consente di filtrare
# gli elementi di una sequenza (come una lista, una tupla o un insieme)
# utilizzando una funzione di filtro.

# Restituisce un iteratore che contiene solo gli elementi della sequenza
# che soddisfano la condizione specificata dalla funzione di filtro.
# La sintassi generale della funzione filter() è la seguente, dove funzione_di_filtro
# è la funzione che definisce la condizione di filtro e sequenza è la sequenza di elementi da filtrare.

def funzione_di_filtro():
    pass

# La funzione_di_filtro è una funzione che accetta un argomento e restituisce
# True o False a seconda che l'elemento debba essere incluso o escluso dalla
# sequenza risultante. Può essere una funzione regolare definita con def,
# ma è comune utilizzare una lambda function, per definire una funzione di
# filtro semplice e concisa direttamente nell'argomento della funzione filter().

sequenza = []
filter(funzione_di_filtro, sequenza)

# Definiamo una funzione chiamata is_even(x) che restituisce True se x è un numero pari
# e False altrimenti. La funzione filter() applica questa funzione di filtro is_even
# a ciascun elemento della lista numbers e restituisce solo gli elementi che soddisfano
# la condizione, cioè i numeri pari. La funzione filter() esegue automaticamente la chiamata
# is_even(x) per ogni elemento x nella sequenza numberse restituisce un iteratore con i soli
# elementi che soddisfano la condizione. Infine, abbiamo utilizzato la funzione list() per
# convertire l'iteratore restituito da filter() in una lista contenente i numeri pari filtrati.

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # Output: [2, 4, 6, 8, 10]