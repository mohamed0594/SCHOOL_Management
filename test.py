from models.users_models import userModel

user = userModel()
user.ajouter_users("Mohamed", "admin", "kone@example.com", "password123")
print(user.afficher_users())
user.ajouter_users("Sara", "teacher", "sara@example.com", "password456")
print(user.afficher_users())
user.ajouter_users("fabien", "student", "fabien@example.com", "password789")
print(user.afficher_users())


