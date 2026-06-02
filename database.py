import sqlite3

connexion = sqlite3.connect("ecole.db")
curseur = connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE NOT NULL,
    prenom TEXT NOT NULL,
    matricule TEXT NOT NULL,
    age INTEGER NOT NULL,
    classe TEXT NOT NULL
)
""")

connexion.commit()


# AJOUTE DES ETUDIANTS
def ajouter():

    while True:
        nom = input("Veuillez entrer votre nom : ")

        if nom.isalpha():
            break
        else:
            print("Erreur de saisie du nom.")

    prenom = input("Veuillez entrer votre prenom : ")
    matricule = input("Veuillez entrer votre matricule : ")

    while True:
        age = input("Veuillez entrer votre age : ")

        if age.isdigit():
            age = int(age)
            break
        else:
            print("Désolé(e) : l'âge doit être un nombre entier")

    classe = input("Veuillez entrer votre classe : ")

    curseur.execute("""
        INSERT INTO students(nom, prenom, matricule, age, classe)
        VALUES (?, ?, ?, ?, ?)
    """, (nom, prenom, matricule, age, classe))

    connexion.commit()
    print("Vous avez ajouté un étudiant")


# LISTER
def liste_des_students():
    curseur.execute("SELECT * FROM students")
    etudiants = curseur.fetchall()

    print("\nVoici la liste des étudiants :")

    for etudiant in etudiants:
        print(etudiant)


# SUPPRIMER
def suppression_etudiants():
    identifiant_etudiants = input("Entrer l'identifiant à supprimer : ")

    curseur.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (identifiant_etudiants,))

    connexion.commit()
    print("Étudiant supprimé")


# MISE À JOUR
def mise_a_jour():

    id_etudiant = input("id de l'étudiant à modifier : ")

    nouveau_nom = input("Veuillez entrer votre nouveau nom : ")
    nouveau_prenom = input("Veuillez entrer votre nouveau prenom : ")
    nouveau_matricule = input("Veuillez entrer votre nouveau matricule : ")

    while True:
        nouveau_age = input("Veuillez entrer votre nouvel âge : ")

        if nouveau_age.isdigit():
            nouveau_age = int(nouveau_age)
            break
        else:
            print("L'age doit etre un nombre.")

    nouvelle_classe = input("Veuillez entrer votre nouvelle classe : ")

    curseur.execute("""
        UPDATE students
        SET nom = ?, prenom = ?, matricule = ?, age = ?, classe = ?
        WHERE id = ?
    """, ( nouveau_nom, nouveau_prenom, nouveau_matricule, nouveau_age, nouvelle_classe,  id_etudiant
    ))

    connexion.commit()
    print("La mise à jour a été effectuée avec succès !")


# RECHERCHER
def rechercher_un_etudiant():

    matricule = input("Entrer le matricule de l'étudiant : ")

    curseur.execute("""
        SELECT * FROM students
        WHERE matricule = ?
    """, (matricule,))

    etudiant = curseur.fetchone()

    if etudiant:
        print("\nÉtudiant trouvé :")
        print(etudiant)
    else:
        print("Aucun étudiant trouvé.")


menu = """
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''|
   BIENVENUE SUR MON SYSTEME AUTOMATISÉE DE GESTION SCOLAIRE
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''|
"""

print(menu)

while True:

    print("===== VOICI LE MENU DE L'ECOLE =====")
    print("1. Ajouter")
    print("2. Liste des etudiants")
    print("3. Supprimer un etudiant")
    print("4. Mise à jour d'un etudiant")
    print("5. Rechercher un etudiant")
    print("6. Quitter")

    option = input("Veuillez choisir : ")

    if option == "1":
        ajouter()

    elif option == "2":
        liste_des_students()

    elif option == "3":
        suppression_etudiants()

    elif option == "4":
        mise_a_jour()

    elif option == "5":
        rechercher_un_etudiant()

    elif option == "6":
        print("Au revoir !")
        break

    else:
        print("Ton choix est invalide ")


connexion.close()