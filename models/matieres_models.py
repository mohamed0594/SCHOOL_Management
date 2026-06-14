from database.base_donnees import BaseDonnees
class MatiereModel(BaseDonnees):
    def __init__(self):
        super().__init__()
        super().subjects()

    def ajouter_matieres(self, nom, teacher_id):
            self.curseur.execute(
                """
                INSERT INTO subjects (nom, teacher_id)
                VALUES (?, ?)
                """,
                (nom, teacher_id)
            )
            self.connexion.commit()
    def afficher_matieres(self):
            self.curseur.execute(
                """
                SELECT * FROM subjects
                """
            )
            return self.curseur.fetchall()
    
    def modifier_matieres(self, id, nom, teacher_id):
            self.curseur.execute(
                """
                UPDATE subjects
                SET nom = ?, teacher_id = ?
                WHERE id = ?
                """,
                (nom, teacher_id, id)
            )
            self.connexion.commit()
    def supprimer_matieres(self, id):
            self.curseur.execute(
                """
                DELETE FROM subjects
                WHERE id = ?
                """,
                (id,)
            )
            self.connexion.commit()

            self.fermeture()

matiere_model = MatiereModel()