from models.teachers_models import TeacherModels

class TeacherService:

    def __init__(self):
        self.model = TeacherModels()

    def menu(self):
        print("""
--- SERVICE PROFESSEURS ---
1. Ajouter
2. Afficher
3. Supprimer
""")

        choice = input("Choix : ")

        if choice == "1":
            nom = input("Nom : ")
            matiere = input("Matière : ")

            self.model.Ajouter(nom, matiere)
            print("Prof ajouté")

        elif choice == "2":
            for t in self.model.Afficher():
                print(t)

        elif choice == "3":
            id = input("ID : ")
            self.model.Supprimer(id)
            print("Supprimé")