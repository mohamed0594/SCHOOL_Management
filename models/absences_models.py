from database.base_principale import baseDonees

class AbsencesModels(baseDonees):
    def __init__(self):
        super().__init__()

    def ajouter(self, student_id, date, status):
        self.curseur.execute("""
            INSERT INTO absences(student_id, date, status)
            VALUES (?, ?, ?)
        """, (student_id, date, status))
        self.connexion.commit()

    def supprimer(self, id):
        self.curseur.execute(
            "DELETE FROM absences WHERE id = ?",
            (id,)
        )
        self.connexion.commit()

    def update(self, id, student_id, date, status):
        self.curseur.execute("""
            UPDATE absences
            SET student_id = ?, date = ?, status = ?
            WHERE id = ?
        """, (student_id, date, status, id))
        self.connexion.commit()

    def rechercher(self, id):
        self.curseur.execute(
            "SELECT * FROM absences WHERE id = ?",
            (id,)
        )
        return self.curseur.fetchone()

    def rechercher_par_etudiant(self, student_id):
        self.curseur.execute(
            "SELECT * FROM absences WHERE student_id = ?",
            (student_id,)
        )
        return self.curseur.fetchall()
    def compter_absences(self, student_id):
     self.curseur.execute("""
        SELECT COUNT(*) FROM absences
        WHERE student_id = ?
    """, (student_id,))
     return self.curseur.fetchone()[0]
    