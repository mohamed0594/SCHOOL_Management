from models.absence_models import AbsenceModels

class AbsenceService:

    def __init__(self):
        self.model = AbsenceModels()

    def menu(self):
        print("""
--- SERVICE ABSENCES ---
1. Ajouter
2. Afficher
""")

        choix = input("Choix : ")

        if choix == "1":
            student_id = input("ID étudiant : ")
            date = input("Date : ")
            status = input("Statut : ")
            self.model.Ajouter(student_id, date, status)

        elif choix == "2":
            for a in self.model.Afficher():
                print(a)