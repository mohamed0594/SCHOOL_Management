from services.auth_service import AuthService
from services.admin_menu import AdminMenu
from services.students_services import StudentService
from services.teachers_services import TeacherService
from services.subject_services import SubjectService
from services.grades_services import GradeService
from services.absences_services import AbsenceService

auth = AuthService()


def login_system():
    print("\n===== CONNEXION =====")
    email = input("Email: ")
    password = input("Mot de passe: ")

    user = auth.login(email, password)

    if not user:
        print("❌ Connexion échouée")
        return

    role = user["role"]

    if role == "admin":
        AdminMenu().run()

    elif role == "professeur":
        print("👉 Menu professeur à connecter plus tard")

    elif role == "etudiant":
        print("👉 Menu étudiant à connecter plus tard")

    else:
        print("❌ Rôle inconnu")


def main():
    while True:
        print("\n===== SYSTEME ECOLE =====")
        print("1. Connexion")
        print("0. Quitter")

        choix = input("Choix: ")

        if choix == "1":
            login_system()

        elif choix == "0":
            print("👋 Fermeture du système")
            break

        else:
            print("❌ Choix invalide")


if __name__ == "__main__":
    main()