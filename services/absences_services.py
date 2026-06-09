from models.absences_models import AbsencesModels

class AbsenceService:

    def __init__(self):
        self.model = AbsencesModels()

    def menu(self):
        print("""
--- SERVICE ABSENCES ---
1. Ajouter absence
2. Afficher absences
""")

        choice = input("Choix : ")

        if choice == "1":
            student_id = input("Student ID : ")
            date = input("Date : ")
            status = input("Justifiée / Non justifiée : ")

            self.model.Ajouter(student_id, date, status)

        elif choice == "2":
            for a in self.model.Afficher():
                print(a)