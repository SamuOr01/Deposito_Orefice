# Classe Utente
class Utente:
    def __init__(self, username):
        self.username = username

# Classe Figlia di Utente
class Admin(Utente):
    def __init__(self):
        super().__init__("admin")

    def reset_studenti(self, file_studenti, file_interventi, motivo):

        # Svuota file studenti
        with open(file_studenti, "w") as file:
            file.write("")

        # Log operazione
        with open(file_interventi, "a") as file:
            file.write(f"RESET ADMIN - Motivo: {motivo}\n")