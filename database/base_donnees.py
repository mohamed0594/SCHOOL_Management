import sqlite3
class BaseDonnees:

    def __init__(self):
        self.connexion = sqlite3.connect('MyDatabase.db')
        self.curseur = self.connexion.cursor()

    def users(self):
        self.curseur.execute("""
                             CREATE TABLE IF NOT EXISTS users
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              nom TEXT NOT NULL,
                              role TEXT NOT NULL,
                              email TEXT NOT NULL UNIQUE,
                              mot_de_passe TEXT NOT NULL
                             )
                             """)
        self.connexion.commit()

    def students(self):
        self.curseur.execute(
                    """
                            CREATE TABLE IF NOT EXISTS students
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            matricule TEXT NOT NULL UNIQUE,
                            nom TEXT NOT NULL,
                            prenom TEXT NOT NULL,
                            age INTEGER NOT NULL,
                            classe TEXT NOT NULL
                            )

                            

        """
        )
        self.connexion.commit()

    def teachers(self):
        self.curseur.execute(
                    """
                            CREATE TABLE IF NOT EXISTS teachers
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nom TEXT NOT NULL,
                            matiere TEXT NOT NULL
                          )             

                    """
        )
        self.connexion.commit()
    
    def subjects(self):
        self.curseur.execute(
                    """
                            CREATE TABLE IF NOT EXISTS subjects
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nom TEXT NOT NULL,
                            teacher_id INTEGER NOT NULL,
                            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                          )             

        """
        )
        self.connexion.commit()
    def notes(self):
        self.curseur.execute(
                    """
                            CREATE TABLE IF NOT EXISTS notes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            student_id INTEGER NOT NULL,
                            subject_id INTEGER NOT NULL,
                            note REAL NOT NULL,
                            FOREIGN KEY (student_id) REFERENCES students(id),
                            FOREIGN KEY (subject_id) REFERENCES subjects(id)
                          )             

        """
        )
        self.connexion.commit()
    
    def absences(self):
        self.curseur.execute(
                    """
                            CREATE TABLE IF NOT EXISTS absences
                            (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            student_id INTEGER NOT NULL,
                            status TEXT NOT NULL,
                            date TEXT NOT NULL,
                            FOREIGN KEY (student_id) REFERENCES students(id)
                          )             

        """
        )
        self.connexion.commit()
    
    def fermeture(self):
        self.connexion.close()
    


