# Classe posto generico
class Posto:

    # Inizializzazione degli attibuti
    def __init__(self, numero: int, fila: str):
        self._numero = numero
        self._fila = fila
        # non occupato di default
        self._occupato = False

    # Prenota il posto se non è occupato
    def prenota(self):
        if not self.get_occupato():
            self.set_occupato(True)
            print(f"\nIl posto {self.get_numero()}{self.get_fila()} è stato prenotato\n")
            return self.get_occupato()
        else:
            print(f"\nIl posto {self.get_numero()}{self.get_fila()} è già occupato\n")
            return self.get_occupato()

    # Libera il posto se è occupato
    def libera(self):
        if self.get_occupato():
            print(f"\nIl posto {self.get_numero()}{self.get_fila()} è stato liberato\n")
            self.set_occupato(False)
            return self.get_occupato()
        else:
            print(f"\nIl posto {self.get_numero()}{self.get_fila()} non era occupato\n")
            return self.get_occupato()

    # Getter per il numero del posto
    def get_numero(self):
        return self._numero

    # Getter per la fila
    def get_fila(self):
        return self._fila

    # Getter per lo stato occupazione
    def get_occupato(self):
        return self._occupato

    # Setter per lo stato occupazione
    def set_occupato(self, stato):
        self._occupato = stato
        return self._occupato

    # Rappresentazione testuale dell'oggetto posto
    def __str__(self):
        if self.get_occupato():
            stato = "occupato"
        else:
            stato = "libero"
        return f"Posto: {self.get_numero()}, Fila: {self.get_fila()} ({stato})"

# Classe PostoVIP che eredita da Posto
class PostoVIP(Posto):

    # Inizializzazione degli attibuti
    def __init__(self, numero: int, fila: str):
        super().__init__(numero, fila)
        # Lista dei servizi extra
        self.__servizi_extra = ["Accesso al lounge", "Servizio in posto", "Pass per il backstage"]

    # Override del metodo prenota per il VIP
    def prenota(self):
        if super().prenota():
            print(f"Con il biglietto VIP, hai diritto ai seguenti servizi extra: {self.get_servizi_extra()}")

    # Getter per la lista dei servizi
    def get_servizi_extra(self):
        return self.__servizi_extra

# Classe PostoStandard con prezzo
class PostoStandard(Posto):

    # Inizializzazione degli attibuti
    def __init__(self, numero: int, fila: str, costo = 10.50):
        super().__init__(numero, fila)
        # Il prezzo del biglietto
        self.__costo = costo

    # Override prenotazione con conferma di acquisto
    def prenota(self):
        if super().prenota():
            scelta = input(
                f"Il prezzo del posto {self.get_numero()}{self.get_fila()} è {self.get_costo()}€, confermi? s/n "
            )
            print()
            if scelta.lower() != "s":
                self.set_occupato(False)
                print("\nPrenotazione annullata")

    # Getter per il costo
    def get_costo(self):
        return self.__costo

# Classe per gestire gli oggetti
class Teatro:

    # Inizializzazione degli attibuti
    def __init__(self, posti: list[Posto]):
        # Lista posti del teatro
        self.__posti = posti

    # Aggiunge un nuovo posto al teatro
    def aggiungi_posto(self, posto: Posto):
        self.get_lista_posti().append(posto)

    # Cerca e prenota un posto specifico
    def prenota_posto(self, numero: int, fila: str):
        for posto in self.get_lista_posti():
            if posto.get_numero() == numero and posto.get_fila() == fila.upper() :
                posto.prenota()
                return
        else:
            print("Posto non trovato\n")

    # Cerca e libera un posto specifico
    def libera_posto(self, numero: int, fila: str):
        for posto in self.get_lista_posti():
            if posto.get_numero() == numero and posto.get_fila() == fila.upper() :
                posto.libera()
                return
        else:
            print("Posto non trovato\n")

    # Stampa solo i posti occupati
    def stampa_posti_occupati(self):
        counter = 1
        print("\nI posti occupati sono:")
        for posto in self.get_lista_posti():
            if posto.get_occupato():
                print(f"{counter}) {posto}")
                counter += 1
        print()


    # Getter per la lista dei posti
    def get_lista_posti(self):
        return self.__posti


# Main

# Creazione dei posti
p1 = Posto(1, "A")
p2 = Posto(2, "A")

p3 = PostoVIP(3, "B")
p4 = PostoVIP(4, "B")

p5 = PostoStandard(5, "C", 12.0)
p6 = PostoStandard(6, "C", 10.5)

# Creazione teatro con una lista iniziale di posti
teatro = Teatro([p1, p2, p3, p4, p5, p6])

# Aggiunta di un nuovo posto
p7 = PostoStandard(7, "D", 8.0)
teatro.aggiungi_posto(p7)


while True:

    # Stampa la lista dei posti disponibili
    for i, posto in enumerate(teatro.get_lista_posti(), 1):
        print(f"{i}) {posto}")

    # Menu per l'utente
    scelta = input(
                    "\nCosa vuoi fare?"
                    "\n1) Prenotare un posto"
                    "\n2) Liberare un posto"
                    "\n3) Visualizzare i posti occupati"
                    "\n4) Esci\n\n"
                )

    match scelta:

        # Prenotazione di un posto
        case "1":
            numero = int(input("\nInserisci il numero del posto: "))
            fila = input("Inserisci la fila del posto: ")
            teatro.prenota_posto(numero, fila)

        # Liberare un posto
        case "2":
            numero = int(input("\nInserisci il numero del posto da liberare: "))
            fila = input("Inserisci la fila del posto da liberare: ")
            teatro.libera_posto(numero, fila)

        # Stampa dei posti occupati
        case "3":
            teatro.stampa_posti_occupati()

        # Esce dal programma
        case "4":
            print("\nArrivederci!")
            break

        # input non valido
        case _:
            print("\nScelta non valida. Riprova.")
            continue