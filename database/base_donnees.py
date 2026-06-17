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

    def moyenne_generale(self):
        self.curseur.execute("SELECT AVG(note) FROM notes")
        result = self.curseur.fetchone()[0]
        return result if result is not None else 0

    def moyenne_etudiant(self, student_id):
        self.curseur.execute(
            """
            SELECT AVG(note)
            FROM notes
            WHERE student_id = ?
            """,
            (student_id,)
        )
        result = self.curseur.fetchone()[0]
        return result if result is not None else 0

    def meilleur_etudiant(self):
        self.curseur.execute(
            """
            SELECT students.id, students.nom, students.prenom, AVG(notes.note) as moyenne
            FROM notes
            JOIN students ON students.id = notes.student_id
            GROUP BY students.id
            ORDER BY moyenne DESC
            LIMIT 1
            """
        )
        return self.curseur.fetchone()
    
    def fermeture(self):
        self.connexion.close()
    


