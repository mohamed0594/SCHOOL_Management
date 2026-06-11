from database.base_donnees import BaseDonnees
class NoteModel(BaseDonnees):
    def __init__(self):
        super().__init__()
        super().notes()

    def ajouter_notes(self, student_id, subject_id, note):
            self.curseur.execute(
                """
                INSERT INTO notes (student_id, subject_id, note)
                VALUES (?, ?, ?)
                """,
                (student_id, subject_id, note)
            )
            self.connexion.commit()
    def afficher_notes(self):
            self.curseur.execute(
                """
                SELECT * FROM notes
                """
            )
            return self.curseur.fetchall()
    def modifier_notes(self, id, student_id, subject_id, note):
            self.curseur.execute(
                """
                UPDATE notes
                SET student_id = ?, subject_id = ?, note = ?
                WHERE id = ?
                """,
                (student_id, subject_id, note, id)
            )
            self.connexion.commit()
    def supprimer_notes(self, id):
            self.curseur.execute(
                """
                DELETE FROM notes
                WHERE id = ?
                """,
                (id,)
            )
            self.connexion.commit()

            self.fermeture()