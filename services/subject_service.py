from models.subjects_models import SubjectsModels

class SubjectService:

    def __init__(self):
        self.subjects = SubjectsModels()

    def menu(self):
        print("""
--- SERVICE MATIÈRES ---
1. Ajouter
2. Afficher
3. Supprimer
""")

        choix = input("Action : ")

        if choix == "1":
            nom = input("Nom matière : ")
            teacher_id = input("ID prof : ")
            self.subjects.Ajouter(nom, teacher_id)
            print("Matière ajoutée")

        elif choix == "2":
            for s in self.subjects.Afficher():
                print(s)

        elif choix == "3":
            id = input("ID : ")
            self.subjects.Supprimer(id)