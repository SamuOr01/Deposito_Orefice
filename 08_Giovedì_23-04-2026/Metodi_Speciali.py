# In Python esistono alcuni metodi chiamati metodi speciali che derivano
# da una classe genirca superiore permettendo agli oggetti di distinguersi
# potendo dare delle specifiche all'interno della classe

# Questi metodi hanno una sintassi particolare con due underscore
# prima e dopo il nome (es. __str__)

# __str__: Rappresentazione testuale leggibile per l'utente di un oggetto
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"{self.titolo} scritto da {self.autore}"

l1 = Libro("Il Signore degli Anelli", "Tolkien")
print(l1)

# __repr__: Rappresentazione testuale tecnica per lo sviluppatore di un oggetto
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    def __repr__(self):
        return f"Studente(nome={self.nome}, voto={self.voto})"

s = Studente("Mario", 28)
print(s) # Studente(nome=Mario, voto=28)
repr(s) # "Studente(nome=Mario, voto=28)"

# __len__: Permette di definire cosa succede quando si usa len() su un oggetto
class Squadra:
    def __init__(self, giocatori):
        self.giocatori = giocatori

    def __len__(self):
        return len(self.giocatori)

team = Squadra(["Marco", "Luca", "Anna"])
print(len(team))

# __eq__: Quando si confrontano due oggetti con l'operatore ==
class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def __eq__(self, altro):
        return self.nome == altro.nome and self.prezzo == altro.prezzo

p1 = Prodotto("Penna", 2)
p2 = Prodotto("Penna", 2)

print(p1 == p2)

# __getattribute__: Viene chiamato ad ogni accesso ad un attributo di un oggetto,
# bisogna usarlo con attenzione perché se si accede direttamente agli attributi
# all’interno del metodo si rischia una ricorsione infinita
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __getattribute__(self, attributo):
        print(f"Sto accedendo all'attributo: {attributo}")
        return super().__getattribute__(attributo)

p = Persona("Mario", 30)

# accesso agli attributi
print(p.nome)
print(p.eta)