# I metodi di classe operano sulla classe e non sull'istanza

class Contatore:

    numero_istanze = 0

    def __init__(self):
        Contatore.numero_istanze += 1

    # Si dichiarano con il decoratore @classmethod e il paramertro cls (classe) permette
    # di accedere agli attributi di classe
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.mostra_numero_istanze}")

# Creazione delle istanze
c1 = Contatore()
c2 = Contatore()

# Può essere chiamato dalla classe
Contatore.mostra_numero_istanze() # Output: Sono state create 2 istanze

class Persona:
    def __init__(self, nome: str, età: int):
        self.nome = nome
        self.età = età

    @classmethod
    def init_from_string(cls, s:str):
        nome, età = s.split(",") # Stringa in arrivo "Mario,30"
        return cls(nome, int(età))

# Può essere chiamato dall'istanza
p = Persona.init_from_string("Mario,30")
print(p.nome, p.età)