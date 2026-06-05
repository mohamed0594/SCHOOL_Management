from models.students_models import StudentModels
from utils.loger import logger

students = StudentModels()

menu = """
+-------------------------------------------------------------+
|                                                             |
|       BIENVENUE SUR MON SYSTEME DE GESTION SCOLAIRE         |
|                                                             |
+-------------------------------------------------------------+
"""

print(menu)

while True:
    print("1. Ajouter Etudiant")
    print("2. Supprimer Etudiant")
    print("3. MiseAJour Etudiant")
    print("4. Afficher Etudiant")
    print("5. Quitter")

    optionDeChoix = input("Votre option de choix : ")

    if optionDeChoix == "1":
        matricule = input("Entrer votre matricule : ")

        
        while True:
            nom = input("Veuillez entrer votre nom : ")

            if all(mots.isalpha() for mots in nom.split()):
                break
            else:
                print("Erreur : le nom doit contenir uniquement des lettres.")

        
        while True:
            prenom = input("veuillez entrer  votre prenom : ")
            if all(mot.isalpha() for mot in prenom.split()):
                break
            else:
                print("Erreur : le prénom doit contenir uniquement des lettres.")
        
        while True:
            age = input("Veuillez entrer votre âge : ")

            if age.isdigit():
                age = int(age)
                break
            else:
                print("Désolé : l'âge doit être un nombre entier.")

        classe = input("Entrer votre classe : ")

        students.Ajouter(matricule, nom, prenom, age, classe)

        print(f"L'étudiant {nom} {prenom} a été ajouté avec succès !")

    elif optionDeChoix == "2":
        identifiant = input("Entrer votre identifiant : ")
        students.Supprimer(identifiant)

        print(f"L'identifiant {identifiant} a été supprimé !")

    elif optionDeChoix == "3":
        nouveauId = input("Entrer l'identifiant à modifier : ")
        nouveauMatricule = input("Entrer le nouveau matricule : ")
        nouveauNom = input("Entrer le nouveau nom : ")
        nouveauPrenom = input("Entrer le nouveau prénom : ")
        nouveauAge = input("Entrer le nouvel âge : ")
        nouvelleClasse = input("Entrer la nouvelle classe : ")

        students.MiseAJour( nouveauId,nouveauMatricule, nouveauNom,nouveauPrenom,nouveauAge,nouvelleClasse )
 

        print(
            f"La mise à jour de {nouveauNom} {nouveauPrenom} a été effectuée avec succès !"
        )

    elif optionDeChoix == "4":
        for student in students.Afficher():
            print(student)

        print("Fin de la lecture ")

    elif optionDeChoix == "5":
        print("Au revoir mon ami(e) !")
        break

    else:
        print("L'option que vous avez entrée est invalide !")