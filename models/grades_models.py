from database.base_principale import BaseDonnees

class GradesModels(BaseDonnees):

    def __init__(self):
        super().__init__()

    def Ajouter(self, student_id, subject_id, note):
        self.curseur.execute(
            """
            INSERT INTO grades(student_id, subject_id, note)
            VALUES (?, ?, ?)
            """,
            (student_id, subject_id, note)
        )
        self.connexion.commit()

    def Supprimer(self, identifiant):
        self.curseur.execute(
            "DELETE FROM grades WHERE id = ?",
            (identifiant,)
        )
        self.connexion.commit()

    def MiseAJour(self, identifiant, note):
        self.curseur.execute(
            "UPDATE grades SET note = ? WHERE id = ?",
            (note, identifiant)
        )
        self.connexion.commit()

    def Afficher(self):
        self.curseur.execute("SELECT * FROM grades")
        return self.curseur.fetchall()

   
    def CalculerMoyenne(self, student_id):
        self.curseur.execute(
            """
            SELECT AVG(note)
            FROM grades
            WHERE student_id = ?
            """,
            (student_id,)
        )

        resultat = self.curseur.fetchone()

        if resultat and resultat[0] is not None:
            return round(resultat[0], 2)

        return 0