from models.students_models import StudentModels

class StudentService:
    def __init__(self):
        self.model = StudentModels()

    def ajouter_etudiant(self):
        matricule = input("Matricule: ")
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = input("Âge: ")
        classe = input("Classe: ")

        self.model.ajouter(matricule, nom, prenom, age, classe)
        print("✅ Étudiant ajouté")

    def lister_etudiants(self):
        for s in self.model.afficher():
            print(s)

    def supprimer_etudiant(self):
        id = input("ID étudiant: ")
        self.model.supprimer(id)
        print("✅ Supprimé")