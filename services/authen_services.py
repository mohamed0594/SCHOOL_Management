from models.users_models import UtilisateursModels

class AuthService:

    def __init__(self):
        self.users = UtilisateursModels()

    def login(self, email, password):
        return self.users.find_user(email, password)