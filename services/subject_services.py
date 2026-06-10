from models.subjects_models import SubjectsModels

class SubjectService:
    def __init__(self):
        self.model = SubjectsModels()

    def ajouter_matiere(self):
        nom = input("Nom matière: ")
        description = input("Description: ")
        teacher_id = input("ID professeur: ")

        self.model.ajouter(nom, description, teacher_id)
        print("✅ Matière ajoutée")

    def lister_matieres(self):
        for s in self.model.lister():
            print(s)