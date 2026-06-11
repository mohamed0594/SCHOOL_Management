from database.base_donnees import BaseDonnees

class TeacherModel(BaseDonnees):
    def __init__(self):
        super().__init__()
        super().teachers()
        
    def ajouter_teachers(self, nom, matiere):
        self.curseur.execute(
            """
            INSERT INTO teachers (nom, matiere)
            VALUES (?, ?)
            """,
            (nom, matiere)
        )
        self.connexion.commit()

    def afficher_teachers(self):
        self.curseur.execute(
            """
            SELECT * FROM teachers
            """
        )
        return self.curseur.fetchall()

    def modifier_teachers(self, id, nom, matiere):
        self.curseur.execute(
            """
            UPDATE teachers
            SET nom = ?, matiere = ?
            WHERE id = ?
            """,
            (nom, matiere, id)
        )
        self.connexion.commit()

    def supprimer_teachers(self, id):
        self.curseur.execute(
            """
            DELETE FROM teachers
            WHERE id = ?
            """,
            (id,)
        )
        self.connexion.commit()
        
        self.fermeture()