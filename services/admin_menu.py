from services.students_services import StudentService
from services.teachers_services import TeacherService
from services.subject_services import SubjectService
from services.grades_services import GradeService
from services.absences_services import AbsenceService
class AdminMenu:
    def __init__(self):
        self.students = StudentService()
        self.teachers = TeacherService()
        self.subjects = SubjectService()
        self.grades = GradeService()
        self.absences = AbsenceService()

    # =========================
    # MENU PRINCIPAL ADMIN
    # =========================
    def run(self):
        while True:
            print("\n==========================")
            print("      MENU ADMIN         ")
            print("==========================")
            print("1. Gérer étudiants")
            print("2. Gérer professeurs")
            print("3. Gérer matières")
            print("4. Gérer notes")
            print("5. Gérer absences")
            print("6. Statistiques")
            print("0. Déconnexion")

            choix = input("Choix: ")

            if choix == "1":
                self.menu_students()

            elif choix == "2":
                self.menu_teachers()

            elif choix == "3":
                self.menu_subjects()

            elif choix == "4":
                self.menu_grades()

            elif choix == "5":
                self.menu_absences()

            elif choix == "6":
                self.menu_stats()

            elif choix == "0":
                print("👋 Déconnexion admin")
                break

            else:
                print("❌ Choix invalide")

    # =========================
    # ETUDIANTS
    # =========================
    def menu_students(self):
        print("\n--- Étudiants ---")
        print("1. Ajouter")
        print("2. Lister")
        print("3. Supprimer")

        c = input("Choix: ")

        if c == "1":
            self.students.ajouter_etudiant()

        elif c == "2":
            self.students.lister_etudiants()

        elif c == "3":
            self.students.supprimer_etudiant()

    # =========================
    # PROFESSEURS
    # =========================
    def menu_teachers(self):
        print("\n--- Professeurs ---")
        print("1. Ajouter")
        print("2. Lister")
        print("3. Supprimer")

        c = input("Choix: ")

        if c == "1":
            self.teachers.ajouter_professeur()

        elif c == "2":
            self.teachers.lister_professeurs()

        elif c == "3":
            self.teachers.supprimer_professeur()

    # =========================
    # MATIERES
    # =========================
    def menu_subjects(self):
        print("\n--- Matières ---")
        print("1. Ajouter")
        print("2. Lister")

        c = input("Choix: ")

        if c == "1":
            self.subjects.ajouter_matiere()

        elif c == "2":
            self.subjects.lister_matieres()

    # =========================
    # NOTES
    # =========================
    def menu_grades(self):
        print("\n--- Notes ---")
        print("1. Ajouter note")
        print("2. Voir notes étudiant")
        print("3. Moyenne étudiant")

        c = input("Choix: ")

        if c == "1":
            self.grades.ajouter_note()

        elif c == "2":
            self.grades.voir_notes_etudiant()

        elif c == "3":
            self.grades.moyenne_etudiant()

    # =========================
    # ABSENCES
    # =========================
    def menu_absences(self):
        print("\n--- Absences ---")
        print("1. Ajouter absence")
        print("2. Compter absences")

        c = input("Choix: ")

        if c == "1":
            self.absences.ajouter_absence()

        elif c == "2":
            self.absences.compter_absences()

    # =========================
    # STATISTIQUES (simple pour maintenant)
    # =========================
    def menu_stats(self):
        print("\n--- Statistiques ---")
        print("Fonction à développer :")
        print("- meilleur étudiant")
        print("- moyenne générale")
        print("- total absences")