from models.students_models import student_model
from utils.logger import logging

def add_student():
    matricule = input("Matricule : ")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    age = input("Âge : ")
    classe = input("Classe : ")
    
    student_model.ajouter_students(matricule, nom, prenom, age, classe)
    print("Étudiant ajouté")
    logging.info(f"Étudiant ajouté : {matricule} - {nom} {prenom}")

def afficher_display():
   
    etudiants = student_model.afficher_students()
    if not etudiants:
        print("Aucun étudiant trouvé.")
    else:
        for e in etudiants:
            print(e)

def modifier_students():
    id = input("ID de l'étudiant à modifier : ")
    mat = input("Nouveau Matricule : ")
    nom = input("Nouveau Nom : ")
    prenom = input("Nouveau Prénom : ")
    age = input("Nouvel Âge : ")
    classe = input("Nouvelle Classe : ")
    
    
    student_model.modifier_students(id, mat, nom, prenom, age, classe)
    print("Étudiant modifié avec succès.")
    logging.info(f"Étudiant ID {id} modifié.")

def supprimer_all():
    confirmation = input("Voulez-vous vraiment TOUT supprimer ? (oui/non) : ")
    if confirmation.lower() == 'oui':
        
        student_model.supprimer_all_students() 
        print("Tous les étudiants ont été supprimés.")
        logging.warning("Tous les étudiants ont été supprimés de la base.")
    else:
        print("Action annulée.")