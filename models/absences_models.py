from database.base_donnees import BaseDonnees

class AbsenceModel(BaseDonnees):
    def __init__(self):
        super().__init__()
        super().absences()

    def ajouter_absences(self, student_id, status, date):
            self.curseur.execute(
                """
                INSERT INTO absences (student_id, status,date)
                VALUES (?, ?,  ?)
                """,
                (student_id, status,date)
            )
            self.connexion.commit()
    def afficher_absences(self):
            self.curseur.execute(
                """
                SELECT * FROM absences
                """
            )
            return self.curseur.fetchall()
    def modifier_absences(self, id, student_id, status, date):
            self.curseur.execute(
                """
                UPDATE absences
                SET student_id = ?,   status = ?, date = ?
                WHERE id = ?
                """,
                (student_id,  status, date, id)
            )
            self.connexion.commit()
    def supprimer_absences(self, id):
            self.curseur.execute(
                """
                DELETE FROM absences
                WHERE id = ?
                """,
                (id,)
            )
            self.connexion.commit()

            
    def compter_absences(self, student_id):
     self.curseur.execute(
        """
        SELECT COUNT(*)
        FROM absences
        WHERE student_id = ?
        AND status = 'Absent'
        """,
        (student_id,)
    )

     return self.curseur.fetchone()[0]