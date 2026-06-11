from config.constante import menu, menu_connexion, menuPrincipal
from models.users_models import userModel
from models.students_models import StudentModel, student_model

 
user = userModel()
student = StudentModel()
print(menu)


print(menu_connexion)
choix = input("choisir une option : ")

   
if choix == "1":
        print("entrer vos infos de connexion")

        email = input("Entrer votre email : ")
        password = input("Entrer votre mot de passe : ")

        trouver = user.login(email, password)

        if not trouver:
            print("Utilisateur inconnu ")

        else:
            print("\nConnexion réussie !")
            print("Bienvenue :", trouver[1])
print(menuPrincipal)
option = input("Option des menus : ")
if option == "1":
       input("Entrer votre matricule")
       input("Entrer votre nom")
       input("Entrer votre prenom")
       input("Entrer votre age")
       input("Entrer votre classe")

       student_model =student_model.ajouter_students()
     

elif option == "2":
     student_model.afficher_students()

elif  option == "3":
    student_model.modifier_students()
elif option == "4":
     student_model.supprimer_students()
else:
     print("option invalide ")

     
     
     
     




