from models.users_models import UtilisateursModels

class AuthService:
    def __init__(self):
        self.user_model = UtilisateursModels()
        self.user_connecte = None

    # 🔐 Connexion utilisateur
    def login(self, email, password):
        user = self.user_model.se_connecter(email, password)

        if user:
            self.user_connecte = {
                "id": user[0],
                "nom": user[1],
                "role": user[2],
                "email": user[4]
            }
            print(f"✅ Connexion réussie : {user[1]} ({user[2]})")
            return self.user_connecte
        else:
            print("❌ Email ou mot de passe incorrect")
            return None

    # 🚪 Déconnexion
    def logout(self):
        if self.user_connecte:
            print(f"👋 Déconnexion de {self.user_connecte['nom']}")
            self.user_connecte = None
        else:
            print("⚠️ Aucun utilisateur connecté")

    # 🎭 Vérifier rôle
    def verifier_role(self, role):
        if not self.user_connecte:
            print("❌ Aucun utilisateur connecté")
            return False

        return self.user_connecte["role"] == role

    # 👤 Récupérer utilisateur connecté
    def get_user(self):
        return self.user_connecte