# In Python, filter() è una funzione integrata che permette di selezionare alcuni
# elementi da una sequenza, come una lista, una tupla o un insieme, in base a una
# determinata condizione.

# Questa condizione viene definita tramite una funzione di filtro, che viene applicata
# a ogni elemento della sequenza: vengono mantenuti solo quelli che la soddisfano.

# Il risultato di filter() non è una lista, ma un iteratore, cioè un oggetto che produce
# gli elementi filtrati uno alla volta. Per ottenere una lista, è quindi necessario convertirlo
# esplicitamente, ad esempio usando list().

# In generale, la funzione filter() prende in input una funzione (che rappresenta la condizione)
# e una sequenza di elementi su cui applicarla.

def funzione_di_filtro():
    pass

# La funzione di filtro è una funzione che prende in input un elemento della sequenza e restituisce
# un valore booleano, cioè True o False, a seconda che quell’elemento debba essere incluso o escluso
# nel risultato finale.

# Questa funzione può essere definita normalmente con def, ma spesso si preferisce usare una lambda
# function, perché permette di scrivere condizioni semplici in modo più rapido e direttamente all’interno
# della chiamata a filter().

sequenza = []
filter(funzione_di_filtro, sequenza)

# Definiamo una funzione is_even(x) che restituisce True se il numero x è pari e False in caso contrario.
# La funzione filter() utilizza questa funzione di filtro applicandola a ciascun elemento della lista
# numbers, mantenendo solo quelli che soddisfano la condizione, cioè i numeri pari.

# In pratica, filter() chiama automaticamente is_even(x) per ogni elemento della sequenza e restituisce un
# iteratore contenente solo gli elementi per cui la funzione restituisce True.

# Infine, l’iteratore viene convertito in una lista tramite la funzione list(), ottenendo così la lista
# finale dei numeri pari filtrati.

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # Output: [2, 4, 6, 8, 10]