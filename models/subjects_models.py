from database.base_principale import BaseDonnees


class SubjectsModels(BaseDonnees):

    def __init__(self):
        super().__init__()

    def Ajouter(self, nom, teacher_id):
        self.curseur.execute(
            """
            INSERT INTO subjects(nom, teacher_id)
            VALUES (?, ?)
            """,
            (nom, teacher_id)
        )
        self.connexion.commit()

    def Supprimer(self, identifiant):
        self.curseur.execute(
            """
            DELETE FROM subjects
            WHERE id = ?
            """,
            (identifiant,)
        )
        self.connexion.commit()

    def MiseAJour(self, identifiant, nom, teacher_id):
        self.curseur.execute(
            """
            UPDATE subjects
            SET nom = ?, teacher_id = ?
            WHERE id = ?
            """,
            (nom, teacher_id, identifiant)
        )
        self.connexion.commit()

    def Rechercher(self, identifiant):
        self.curseur.execute(
            """
            SELECT * FROM subjects
            WHERE id = ?
            """,
            (identifiant,)
        )
        return self.curseur.fetchone()

    def Afficher(self):
        self.curseur.execute(
            "SELECT * FROM subjects"
        )
        return self.curseur.fetchall()