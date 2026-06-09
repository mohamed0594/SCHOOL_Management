from models.grades_models import GradesModels
from models.students_models import StudentModels

class GradeService:

    def __init__(self):
        self.model = GradesModels()
        self.students = StudentModels()

    def menu(self):
        print("""
--- SERVICE NOTES ---
1. Ajouter note
2. Afficher notes
3. Moyenne étudiant
4. Meilleur étudiant
""")

        choice = input("Choix : ")

        if choice == "1":
            student_id = input("ID étudiant : ")
            subject_id = input("ID matière : ")
            note = float(input("Note : "))
            self.model.Ajouter(student_id, subject_id, note)

        elif choice == "2":
            for g in self.model.Afficher():
                print(g)

        elif choice == "3":
            student_id = input("ID étudiant : ")
            moyenne = self.model.CalculerMoyenne(student_id)
            print("Moyenne :", moyenne)

        elif choice == "4":
            students = self.students.Afficher()

            best = None
            best_moy = -1

            for s in students:
                moy = self.model.CalculerMoyenne(s[0])

                if moy > best_moy:
                    best_moy = moy
                    best = s

            print("Meilleur étudiant :", best, "Moyenne :", best_moy)