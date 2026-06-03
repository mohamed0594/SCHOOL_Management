import sqlite3
class baseDonees:
    def __init__(self):
        self.connexion = sqlite3.connect("ecole.db")
        self.curseur = self.connexion.cursor()

# creation de la table users
    def users(self):
        self.curseur.execute(
        """
          CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            role TEXT NOT NULL

        )

        """
        )
# creation de la table studfents
    def students(self):
        self.curseur.execute(
            """
         CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricule  TEXT UNIQUE  NOT NULL,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            age  INTEGER TEXT NOT NULL,
            classe TEXT NOT NULL,

        """

        )
# creation de la table teachers
    def teachers(self):
        self.curseur.execute(
        """
         CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            matiere TEXT NOT NULL

        """
        )

# creation  de la table subjects

    def subjects(self):
        self.curseur.execute(
        """
           CREATE TABLE IF NOT EXISTS subjects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            teachers_id TEXT NOT NULL
            

        """
        )
    def grades(self):
        self.curseur.execute(
        """
        CREATE TABLE IF NOT EXISTS grades(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            subject_id TEXT NOT NULL,
            note TEXT NOT NULL,

        """
        )
# creation de la table absences
    def absences(self):
        self.curseur.execute(
        """
         CREATE TABLE IF NOT EXISTS absences(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            students_id TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL
        """
        )
