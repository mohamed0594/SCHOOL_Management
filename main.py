from config.constante import (
    menu,
    menu_connexion,
    menuPrincipal,
    menuProfesseurs,
    menuMatieres,
    menuNotes,
    menus_choice
)

from models.users_models import userModel
from models.students_models import student_model
from models.teachers_models import TeacherModel
from models.matieres_models import matiere_model
from models.notes_models import note_model
from models.absences_models import AbsenceModel

from services import students_services, notes_services, matiers_services, teachers_services

teacher_model = TeacherModel()
user = userModel()
absence_model = AbsenceModel()

print(menu)
print(menu_connexion)

# LOGIN 
while True:
 choix = input("Choisir une option : ")
 if choix == "0":
        print("Au revoir ")
        exit()
 
 elif choix == "1":

    print("Entrer vos informations de connexion")

    email = input("Email : ")
    password = input("Mot de passe : ")

    trouver = user.login(email, password)

    if not trouver:
        print("Utilisateur inconnu, réessayez !")
        exit()

    print("Connexion réussie")
    print("Bienvenue :", trouver[1])

    role = trouver[2]
    print("Rôle :", role)

    # BOUCLE PRINCIPALE 
    while True:

        print(menuPrincipal)
        option = input("Option du menu : ")

        # QUITTER 
        if option == "0":
            print("Au revoir ")
            break

        # ETUDIANTS 
        elif option == "1":

            while True:
                choix_etudiant = input("""
  1. Ajouter étudiant
  2. Afficher étudiants
  3. Modifier étudiant
  4. Supprimer étudiant
  5. Retour
  Votre choix : """)

                if choix_etudiant == "1":
                    students_services.add_student()

                elif choix_etudiant == "2":
                    students_services.afficher_display()

                elif choix_etudiant == "3":
                    id = input("ID : ")
                    students_services.modifier_students()
                

                elif choix_etudiant == "4":
                    students_services.supprimer_students(input("ID : "))
                   

                elif choix_etudiant == "5":
                    break

        # PROFESSEURS
        elif option == "2":

            while True:
                choix_prof = input("""
    1. Ajouter prof
    2. Afficher profs
    3. Modifier prof
    4. Supprimer prof
    5. Retour
    Votre choix : """)

                if choix_prof == "1":
                     
                     nom=input("Nom : ")
                     matiere=input("Matière : ")
                     
                     teacher_model.ajouter_teachers(nom, matiere)
                     print("Professeur ajouté")

                elif choix_prof == "2":
                    for p in teacher_model.afficher_teachers():
                        print(p)

                elif choix_prof == "3":
                    
                       id_note=   input("ID : ")
                       id_etudient= input("Nom : ")
                       id_matiere= input("Matière : ")
                   
                       teacher_model.modifier_teachers( id_note, id_etudient, id_matiere)
                       print("Professeur modifié")

                elif choix_prof == "4":
                    teacher_model.supprimer_teachers(input("ID : "))
                    print("Professeur supprimé")

                elif choix_prof == "5":
                    break

        #  MATIERES 
        elif option == "3":

            while True:
                choix_matiere = input("""
    1. Ajouter matière
    2. Afficher matières
    3. Modifier matière
    4. Supprimer matière
    5. Retour
    Votre choix : """)

                if choix_matiere == "1":
                 matiers_services.ajouter_matieres()

                elif choix_matiere == "2":
                 matiers_services.afficher_matieres()
                    

                elif choix_matiere == "3":
                   matiers_services.modifier_matieres()
                   

                #elif choix_etudiant == "4":
                   # id = input("ID : ")
                   # students_services.supprimer_students(id)

                if choix_matiere == "4":
                     matiers_services.supp_matieres()

                


                elif choix_matiere == "5":
                    break

        #  NOTES 
        elif option == "4":

            while True:
                choix_note = input("""
1. Ajouter note
2. Afficher notes
3. Modifier note
4. Supprimer note
5. Retour
Votre choix : """)

                if choix_note == "1":
                    notes_services.matieres_add()
                    
                elif choix_note == "2":
                    notes_services.afficher_notes()

                elif choix_note == "3":
                   notes_services.modifier_notes()
                elif choix_note == "4":
                   notes_services.supp_notes()

                elif choix_note == "5":
                    break

        # STATISTIQUES 
        elif option == "6":

            while True:
                choix_stat = input("""
1. Moyenne générale
2. Moyenne étudiant
3. Meilleur étudiant
4. Absences
5. Retour
Votre choix : """)

                if choix_stat == "1":
                    moyenne = note_model.moyenne_generale()
                    print(f"Moyenne générale : {moyenne:.2f}")

                elif choix_stat == "2":
                    student_id = input("ID étudiant : ")
                    moyenne = note_model.moyenne_etudiant(student_id)
                    print(f"Moyenne étudiant : {moyenne:.2f}")

                elif choix_stat == "3":
                    meilleur = note_model.meilleur_etudiant()
                    print(f"Meilleur : {meilleur[1]} {meilleur[2]}")
                    print(f"Moyenne : {meilleur[3]:.2f}")

                elif choix_stat == "4":
                    student_id = input("ID étudiant : ")
                    nombre = absence_model.compter_absences(student_id)
                    print(f"Absences : {nombre}")

                elif choix_stat == "5":
                    break

        else:
            print("Option invalide")
            