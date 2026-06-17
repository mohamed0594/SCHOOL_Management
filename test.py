from models.users_models import userModel

from models.users_models import userModel

user = userModel()

user.ajouter_users(
    "Admin", "admin", "admin@gmail.com", "12345"
)

user.ajouter_users(
    "Prof","teachers", "prof@gmail.com", "1234"
)

user.ajouter_users(
    "Etudiant", "students","student@gmail.com","123"
)

print(user.afficher_users())