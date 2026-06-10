from database.base_principale import baseDonees

class SubjectsModels(baseDonees):
    def __init__(self):
        super().__init__()

    def Ajouter(self, nom, description, teacher_id):
     self.curseur.execute(
        """
        INSERT INTO subjects(nom, description, teacher_id)
        VALUES (?, ?, ?)
        """,
        (nom, description, teacher_id)
    )
     self.connexion.commit()

    def supprimer(self, id):
        self.curseur.execute(
            "DELETE FROM subjects WHERE id = ?",
            (id,)
        )
        self.connexion.commit()

    def update(self, id, nom, description, teacher_id):
     self.curseur.execute(
        """
        UPDATE subjects
        SET nom = ?, description = ?, teacher_id = ?
        WHERE id = ?
        """,
        (nom, description, teacher_id, id)
    )
     self.connexion.commit()
     self.connexion.commit()

    def rechercher(self, id):
        self.curseur.execute(
            "SELECT * FROM subjects WHERE id = ?",
            (id,)
        )
        return self.curseur.fetchone()

    def lister(self):
        self.curseur.execute(
            "SELECT * FROM subjects"
        )
        return self.curseur.fetchall()