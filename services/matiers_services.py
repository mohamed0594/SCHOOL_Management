from models.matieres_models import matiere_model
from utils.logger import logging


def ajouter_matieres():
       matiere_model.ajouter_matieres(
                        input("Nom : "),
                        input("ID prof : ")
                    )
       print("Matière ajoutée")


def afficher_matieres():
       for m in matiere_model.afficher_matieres():
                        print(m)


def modifier_matieres():
         matiere_model.modifier_matieres(
                        input("ID : "),
                        input("Nom : "),
                        input("ID prof : ")
                    )
         print("Matière modifiée")

def supp_matieres():
        matiere_model.supprimer_matieres(input("ID : "))
        print("Matière supprimée")



        
       
      
