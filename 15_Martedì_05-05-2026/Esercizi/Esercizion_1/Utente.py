# classe Genitore Utente
class Utente():
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    # Getter
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password