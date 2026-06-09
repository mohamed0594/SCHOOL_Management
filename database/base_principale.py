import sqlite3

class BaseDonnees:
    def __init__(self):
        self.connexion = sqlite3.connect("MaDataBaseprincipale.db")
        self.curseur = self.connexion.cursor()
        self.users()
        self.students()
        self.teachers()
        self.subjects()
        self.grades()
        self.absences()

        self.connexion.commit()

    # creation de la table users
    def users(self):
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                role TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE
            )
        """)
    
    # creation de la table studfents
    def students(self):
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricule TEXT UNIQUE NOT NULL,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                age INTEGER NOT NULL,
                classe TEXT NOT NULL
            )
        """)

    # creation de la table teachers
    def teachers(self):
        self.curseur.execute(
        """
            CREATE TABLE IF NOT EXISTS teachers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                matiere TEXT NOT NULL
            )
        """
        )

    # creation  de la table subjects
    def subjects(self):
     self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS subjects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            teacher_id INTEGER NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        )
    """)

    def grades(self):
      self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS grades(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject_id INTEGER NOT NULL,
            note REAL NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(subject_id) REFERENCES subjects(id)
        )
    """)
              
      
    # creation de la table absences
    def absences(self):
        self.curseur.execute(
        """
            CREATE TABLE IF NOT EXISTS absences(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                students_id TEXT NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """
        )