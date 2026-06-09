from models.users_models import UtilisateursModels

users = UtilisateursModels()

users.Ajouter(
    "Administrateur",
    "admin",
    "admin123",
    "admin@example.com"
)

print("Utilisateur ajouté avec succès")
