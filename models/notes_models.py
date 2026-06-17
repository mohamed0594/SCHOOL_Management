from database.base_donnees import BaseDonnees


class NoteModel(BaseDonnees):

    def __init__(self):
        super().__init__()
        super().notes()

    # ================= CRUD NOTES =================

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
        self.curseur.execute("SELECT * FROM notes")
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

    # ================= STATISTIQUES =================

    def moyenne_generale(self):
        self.curseur.execute("SELECT AVG(note) FROM notes")
        result = self.curseur.fetchone()[0]
        return result if result is not None else 0

    def moyenne_etudiant(self, student_id):
        self.curseur.execute(
            """
            SELECT AVG(note)
            FROM notes
            WHERE student_id = ?
            """,
            (student_id,)
        )
        result = self.curseur.fetchone()[0]
        return result if result is not None else 0

    def meilleur_etudiant(self):
        self.curseur.execute(
            """
            SELECT students.id, students.nom, students.prenom, AVG(notes.note) as moyenne
            FROM notes
            JOIN students ON students.id = notes.student_id
            GROUP BY students.id
            ORDER BY moyenne DESC
            LIMIT 1
            """
        )
        return self.curseur.fetchone()


# instance globale
note_model = NoteModel()