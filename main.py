from models.students_models import StudentModels
from services.auth_service import AuthService
from config.constantes import menuPrincipale

students = StudentModels()
auth_service = AuthService()

print(menuPrincipale)

email = input("Entrer votre email : ")
password = input("Entrer votre mot de passe : ")

user = auth_service.login(email, password)

if not user:
    print("Email ou mot de passe incorrect")
    exit()

print(f"\nBienvenue {user[1]}")
print(f"Rôle : {user[2]}\n")

# MENU PRINCIPAL
while True:

    print("""
=== MENU PRINCIPAL ===
1. Service Étudiants
2. Service Professeurs
3. Service Matières
4. Service Notes
5. Service Absences
6. Quitter
""")

    choix = input("Choix : ")

    # ================= ETUDIANTS =================
    if choix == "1":
        if user[2] in ["admin", "etudiant"]:

            print("""
--- SERVICE ETUDIANTS ---
1. Ajouter
2. Afficher
3. Modifier
4. Supprimer
""")

            action = input("Action : ")

            if action == "1":
                matricule = input("Matricule : ")
                nom = input("Nom : ")
                prenom = input("Prenom : ")
                age = int(input("Age : "))
                classe = input("Classe : ")

                students.Ajouter(matricule, nom, prenom, age, classe)

            elif action == "2":
                for s in students.Afficher():
                    print(s)

            elif action == "3":
                id = input("ID : ")
                matricule = input("Matricule : ")
                nom = input("Nom : ")
                prenom = input("Prenom : ")
                age = int(input("Age : "))
                classe = input("Classe : ")

                students.MiseAJour(id, matricule, nom, prenom, age, classe)

            elif action == "4":
                id = input("ID : ")
                students.Supprimer(id)

    # ================= QUITTER =================
    elif choix == "6":
        print("Au revoir ")
        break

    else:
        print("Choix invalide")