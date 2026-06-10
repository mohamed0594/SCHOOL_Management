from models.teacher_models import TeacherModels

class TeacherService:
    def __init__(self):
        self.model = TeacherModels()

    def ajouter_professeur(self):
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        email = input("Email: ")
        password = input("Password: ")

        self.model.ajouter(nom, prenom, email, password)
        print("✅ Professeur ajouté")

    def lister_professeurs(self):
        for t in self.model.lister():
            print(t)

    def supprimer_professeur(self):
        id = input("ID professeur: ")
        self.model.supprimer(id)
        print("✅ Supprimé")