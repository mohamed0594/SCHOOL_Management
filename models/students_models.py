from database.base_donnees import BaseDonnees

class StudentModel(BaseDonnees):
    def __init__(self):
        super().__init__()
        super().students()

    def ajouter_students(self, matricule, nom, prenom, age, classe, email, password):
       
        self.curseur.execute(
            """
            INSERT INTO students (matricule, nom, prenom, age, classe)
            VALUES (?, ?, ?, ?, ?)
            """,
            (matricule, nom, prenom, age, classe)
        )
       
        
        self.curseur.execute(
            """
            INSERT INTO users (nom, role, email, mot_de_passe)
            VALUES (?, ?, ?, ?)
            """,
            (f"{nom} {prenom}", "Etudiant", email, password)
        )
       
        self.connexion.commit()

    def afficher_students(self):
        self.curseur.execute(
            """
            SELECT * FROM students
            """
        )
        return self.curseur.fetchall()

    def modifier_students(self, id, matricule, nom, prenom, age, classe):
      
        self.curseur.execute(
            """
            UPDATE students
            SET matricule = ?, nom = ?, prenom = ?, age = ?, classe = ?
            WHERE id = ?
            """,
            (matricule, nom, prenom, age, classe, id)
        )
        self.connexion.commit()

    def supprimer_students(self, id):
        self.curseur.execute(
            """
            DELETE FROM students
            WHERE id = ?
            """,
            (id,)
        )
        self.connexion.commit()

student_model = StudentModel()