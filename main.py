from models.students_models import StudentModels

students = StudentModels()

menu ="""

+-------------------------------------------------------------+
|                                                             |
|       BIENVENUE SUR MON SYSTEME DE GESTION SCOLAIRE         |
|                                                             |
+-------------------------------------------------------------+

"""

print(menu)
while True:
    print("1. Ajouter Etudiantt") 
    print("2. Supprimer Etudiant")
    print("3. MiseAJour Etudiant")
    print("4. Afficher Etudiant")
    print("5. Quitter ")

    optionDeChoix = input("Votre option de choix :")

    if optionDeChoix == "1":
         matricule = input("Entrer votre matricule: ")  
         nom = input("Entrer votre nom: ")  
         prenom = input("Entrer votre prenom: ")  
         age = input("Entrer votre age: ")  
         classe = input("Entrer votre classe: ")  

         students.Ajouter(matricule,nom, prenom, age, classe)

         print(f" L'Etudiant {nom} {prenom} a ete ajouter avec sucess!")


    elif     optionDeChoix == "2":
         identifiant = input("Entrer votre identifiant")
         students.Supprimer(identifiant)
         print(f"L'identifiant {identifiant} a ete supprimer !")

    elif optionDeChoix == "3":
         nouveauId = input(" Entrer le nouveau identifiant a modifier ")
         nouveauMatricule = input(" Entrer le tout nouveau matricule ")
         nouveauNom = input(" Entrer le nouveau nom")
         nouveauPrenom =  input(" Entrer le nouveau prenom")
         nouveauAge =  input(" Entrer le nouveau age")
         nouveleClasse =  input(" Entrer l votre nouvelle classe")

         students.MiseAJour(nouveauId,nouveauMatricule, nouveauNom,nouveauPrenom,nouveauAge, nouveleClasse)
         print(f"la mise ajour de {nouveauNom}{nouveauPrenom} a ete modifier avec sucess!")

    elif  optionDeChoix == "4":
         for student in students.Afficher():
             print(student)

    elif optionDeChoix == "5":
     break

    else:
        print("l'option que vous avez entrer est invalide ! ...")




    



