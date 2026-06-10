from database.base_principale import baseDonees

class GradesModels(baseDonees):
    def __init__(self):
        super().__init__()

    # ✅ Ajouter une note (0 à 20)
    def ajouter(self, student_id, subject_id, note):
        if note < 0 or note > 20:
            print("❌ Note invalide (doit être entre 0 et 20)")
            return

        self.curseur.execute("""
            INSERT INTO grades(student_id, subject_id, note)
            VALUES (?, ?, ?)
        """, (student_id, subject_id, note))
        self.connexion.commit()

    # ❌ Supprimer une note
    def supprimer(self, id):
        self.curseur.execute(
            "DELETE FROM grades WHERE id = ?",
            (id,)
        )
        self.connexion.commit()

    # ✏️ Modifier une note
    def update(self, id, student_id, subject_id, note):
        if note < 0 or note > 20:
            print("❌ Note invalide")
            return

        self.curseur.execute("""
            UPDATE grades
            SET student_id = ?, subject_id = ?, note = ?
            WHERE id = ?
        """, (student_id, subject_id, note, id))
        self.connexion.commit()

    # 🔎 Rechercher une note par id
    def rechercher(self, id):
        self.curseur.execute(
            "SELECT * FROM grades WHERE id = ?",
            (id,)
        )
        return self.curseur.fetchone()

    # 📚 Notes d’un étudiant
    def rechercher_par_etudiant(self, student_id):
        self.curseur.execute(
            "SELECT * FROM grades WHERE student_id = ?",
            (student_id,)
        )
        return self.curseur.fetchall()

    # 📘 Notes d’une matière
    def rechercher_par_matiere(self, subject_id):
        self.curseur.execute(
            "SELECT * FROM grades WHERE subject_id = ?",
            (subject_id,)
        )
        return self.curseur.fetchall()

    # 📊 Note précise étudiant + matière
    def rechercher_par_etudiant_et_matiere(self, student_id, subject_id):
        self.curseur.execute("""
            SELECT * FROM grades
            WHERE student_id = ? AND subject_id = ?
        """, (student_id, subject_id))
        return self.curseur.fetchone()

    # 📈 Calcul moyenne d’un étudiant
    def calculer_moyenne(self, student_id):
        self.curseur.execute("""
            SELECT AVG(note) FROM grades
            WHERE student_id = ?
        """, (student_id,))
        
        result = self.curseur.fetchone()[0]
        return result if result is not None else 0