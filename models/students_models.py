from database.base_principale import baseDonees

class StudentModels(baseDonees):
    def __init__(self):
        super().__init__()

    def ajouter(self, matricule, nom, prenom, age, classe):
        self.curseur.execute("""
            INSERT INTO students(matricule, nom, prenom, age, classe)
            VALUES (?, ?, ?, ?, ?)
        """, (matricule, nom, prenom, age, classe))
        self.connexion.commit()

    def supprimer(self, id):
        self.curseur.execute(
            "DELETE FROM students WHERE id = ?",
            (id,)
        )
        self.connexion.commit()

    def mettre_a_jour(self, id, matricule, nom, prenom, age, classe):
        self.curseur.execute("""
            UPDATE students
            SET matricule = ?, nom = ?, prenom = ?, age = ?, classe = ?
            WHERE id = ?
        """, (matricule, nom, prenom, age, classe, id))
        self.connexion.commit()

    def afficher(self):
        self.curseur.execute("SELECT * FROM students")
        return self.curseur.fetchall()

    def rechercher(self, id):
        self.curseur.execute(
            "SELECT * FROM students WHERE id = ?",
            (id,)
        )
        return self.curseur.fetchone()

    def rechercher_par_matricule(self, matricule):
        self.curseur.execute(
            "SELECT * FROM students WHERE matricule = ?",
            (matricule,)
        )
        return self.curseur.fetchone()