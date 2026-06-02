import sqlite3

connexion = sqlite3.connect("ecole.db")
curseur = connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE NOT NULL,
    prenom TEXT NOT NULL,
    matricule TEXT NOT NULL,
    age INTEGER,
    classe TEXT NOT NULL
)
""")

connexion.commit()


# AJOUTE DES ETUDIANTS 
def ajouter():
    nom = input("Veuillez entrer votre nom : ")
    prenom = input("Veuillez entrer votre prenom : ")
    matricule = input("Veuillez entrer votre matricule : ")
    age = input("Veuillez entrer votre âge : ")
    classe = input("Veuillez entrer votre classe : ")

    curseur.execute("""
        INSERT INTO students(nom, prenom , matricule,age,  classe)
        VALUES (?, ?, ?, ?,?)
    """, (nom, prenom, matricule, age ,  classe))

    connexion.commit()
    print(" Vous avez ajouté un étudiant")


# LISTER
def liste_des_students():
    curseur.execute("SELECT * FROM students")
    etudiants = curseur.fetchall()

    print("Voici la liste des étudiants :")

    for etudiant in etudiants:
        print(etudiant)

# rappel aux fonctions
ajouter()
liste_des_students()



connexion.close()