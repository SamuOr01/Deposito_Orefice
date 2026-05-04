# l'incapsulamento serve a proteggere attributi e metodi delle classi attraverso dei modificatori di accesso

# In Python si una una nomenclatura delle variabili:

# Attributi Privati (__attributo): Preponendo due underscore (__) al nome di un attributo, questo diventa privato,
# il che significa che non può essere accesso direttamente dall'esterno della classe. Per accedere o modificare un
# attributo privato, si usano i metodi getter e setter.

# Attributi Protetti (_attributo): Preponendo un underscore (_) al nome di un attributo, questo viene considerato
# protetto. Si tratta più di una convenzione che di una funzionalità linguistica, indicando che l'attributo dovrebbe
# essere usato solo all'interno della classe e delle sue sottoclassi.

# Metodi Getter e Setter: Sono metodi che permettono di ottenere (get) e modificare (set) gli attributi privati di una
# classe. Questi metodi forniscono un controllo maggiore sull'accesso e la modifica dei dati.


# Attributi Privati
class Computer:
    def __init__(self, processore):

        # Attributo privato
        self.__processore = processore

    def get_processore(self):
        return self.__processore

    def set_processore(self, processore):
        self.__smonta()
        self.__processore = processore

    # Metodo Privato
    def __smonta():
        print("Computer smontato")

c = Computer("Intel Ultra 7")

print(c.get_processore())
c.set_processore("AMD Ryzen 7")
print(c.get_processore())

# Gli attributi privati possono essere modificati solo all'interno della classe o con i setter,
# se proviamo a modificarlo all'esterno vedremo che Python stampa solo
# il valore memorizzato con set
c.__processore = "AMD Ryzen 5"
print(c.get_processore())


# Attributi protected
class Animale:
    def __init__(self, nome):
        self._nome = nome

    def fai_verso(self):
        print(f"{self._nome} fa un verso generico")

    def get_nome(self):
        return self._nome

class Cane(Animale):

    def fai_verso(self):
        print(f"{self._nome} sta abbaiando")

class Gatto(Animale):

    def fai_verso(self):
        print(f"{self._nome} sta miagolando")


animale = Animale("Pippo")
cane = Cane("Fido")
gatto = Gatto("Ture")

# Gli attributi protetti sono meno restrittivi rispetto ai privati. Servono di più agli sviluppatori per far capire che
# dovrebbero essere usati solo all'interno delle classi e delle sottoclassi.
# Non viene quindi impedito l'accesso dall'esterno
print(animale.fai_verso())
print(cane.fai_verso())
print(gatto.fai_verso())

print(animale.get_nome())


# Property
class Studente:

    def __init__(self, nome, voto):
        self.nome = nome
        self.__voto = voto

    # property serve per definire il getter come se fosse un attributo dell'oggetto
    @property
    def voto(self):
        print("voto getter")
        return self.__voto

    # @nome_property.setter serve per definire il setter controlla come viene modificato
    # il valore di un attributo dell'oggetto
    @voto.setter
    def voto(self, nuovo_voto):
        if 0 <= nuovo_voto <= 30:
            self.__voto = nuovo_voto
        else:
            print("voto non valido")

s = Studente("Emy", 8)
print(s.voto)

s.voto = -5
s.voto = 30
print(s.voto)

# Esiste anche @nome_property.deleter che serve per definire il metodo che stabilisce cosa succede
# quando si elimina una property con del