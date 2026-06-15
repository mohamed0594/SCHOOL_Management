from config.constante import (
    menu,
    menu_connexion,
    menuPrincipal,
    menuProfesseurs,
    menuMatieres,
    menuNotes
)

from models.users_models import userModel
from models.students_models import student_model
from models.teachers_models import TeacherModel
from models.matieres_models import matiere_model
from models.notes_models import note_model


teacher_model = TeacherModel()
user = userModel()

print(menu)
print(menu_connexion)

choix = input("Choisir une option : ")

if choix == "1":

    print("Entrer vos informations de connexion")

    email = input("Email : ")
    password = input("Mot de passe : ")

    trouver = user.login(email, password)

    if not trouver:
        print("Utilisateur inconnu reesayer! ")
        exit()

    print("Connexion réussie")
    print("Bienvenue :", trouver[1])

    print(menuPrincipal)

    option = input("Option du menu : ")

   
    if option == "1":

        print("""
===== GESTION DES ETUDIANTS =====
1. Ajouter étudiant
2. Afficher étudiants
3. Modifier étudiant
4. Supprimer étudiant
5. Quitter
""")

        choix_etudiant = input("Votre choix : ")

        if choix_etudiant == "1":

            matricule = input("Matricule : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            age = input("Âge : ")
            classe = input("Classe : ")

            student_model.ajouter_students(
                matricule,
                nom,
                prenom,
                age,
                classe
            )

            print("Étudiant ajouté")

        elif choix_etudiant == "2":

            etudiants = student_model.afficher_students()

            if not etudiants:
                print("Aucun étudiant trouvé")

            else:
                for etudiant in etudiants:
                    print(etudiant)

        elif choix_etudiant == "3":

            id = input("ID : ")
            matricule = input("Matricule : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            age = input("Âge : ")
            classe = input("Classe : ")

            student_model.modifier_students(
                id,
                matricule,
                nom,
                prenom,
                age,
                classe
            )

            print("Étudiant modifié")

        elif choix_etudiant == "4":

            id = input("ID : ")

            student_model.supprimer_students(id)

            print("Étudiant supprimé")
        elif choix_etudiant =="5":
            print("Vous etes hors du programme")
            exit()

        else:
            print("Choix invalide")

    elif option == "2":

        print(menuProfesseurs)

        choix_prof = input("Votre choix : ")

        if choix_prof == "1":

            nom = input("Nom : ")
            matiere = input("Matière : ")

            teacher_model.ajouter_teachers(
                nom,
                matiere
            )

            print("Professeur ajouté")

        elif choix_prof == "2":

            profs = teacher_model.afficher_teachers()

            if not profs:
                print("Aucun professeur trouvé")

            else:
                for prof in profs:
                    print(prof)

        elif choix_prof == "3":

            id = input("ID : ")
            nom = input("Nom : ")
            matiere = input("Matière : ")

            teacher_model.modifier_teachers(
                id,
                nom,
                matiere
            )

            print("Professeur modifié")

        elif choix_prof == "4":

            id = input("ID : ")

            teacher_model.supprimer_teachers(id)

            print("Professeur supprimé")
        
        elif choix_prof == "5":
            print(" vous etes hors du programme! ")
            exit()


        else:
            print("Choix invalide")

    elif option == "3":

        print(menuMatieres)

        choix_matiere = input("Entrer votre choix : ")

        if choix_matiere == "1":

            nom = input("Entrer le nom de votre matière : ")
            id_teacher = input("Entrer l'identifiant du professeur : ")

            matiere_model.ajouter_matieres(
                nom,
                id_teacher
            )

            print("Matière ajoutée")

        elif choix_matiere == "2":

            matieres = matiere_model.afficher_matieres()

            if not matieres:
                print("Aucune matière trouvée")

            else:
                for matiere in matieres:
                    print(matiere)

        elif choix_matiere == "3":

            id = input("ID : ")
            nom = input("Nom : ")
            id_teacher = input("ID professeur : ")

            matiere_model.modifier_matieres(
                id,
                nom,
                id_teacher
            )

            print("Matière modifiée")

        elif choix_matiere == "4":

            id = input("ID : ")

            matiere_model.supprimer_matieres(id)

            print("Matière supprimée")
        
        elif choix_matiere == "5":
            print("vous etes hors du programme !")
            exit()
        

        else:
            print("Choix invalide")

    elif option == "4":

        print(menuNotes)

        choix_note = input("Votre choix : ")

        if choix_note == "1":

            student_id = input("ID étudiant : ")
            subject_id = input("ID matière : ")
            note = input("Note : ")

            note_model.ajouter_notes(
                student_id,
                subject_id,
                note
            )

            print("Note ajoutée")

        elif choix_note == "2":

            notes = note_model.afficher_notes()

            if not notes:
                print("Aucune note trouvée")

            else:
                for note in notes:
                    print(note)

        elif choix_note == "3":

            id_note = input("ID note : ")
            student_id = input("ID étudiant : ")
            subject_id = input("ID matière : ")
            note = input("Note : ")

            note_model.modifier_notes(
                id_note,
                student_id,
                subject_id,
                note
            )

            print("Note modifiée")

        elif choix_note == "4":

            id_note = input("ID note : ")

            note_model.supprimer_notes(id_note)

            print("Note supprimée")

        elif choix_note == "5":
            print(" vous etes hors du programme")
            exit()

        else:
            print("Choix invalide")

    else:
        print("Option invalide")

else:
    print("Au revoir")