from database.base_principale import baseDonees
class GradesModels(baseDonees):
    def __init__(self):
        super().__init__()

    def Ajouter(self, student_id, subject_id, grade):
        self.curseur.execute("INSERT INTO grades(student_id, subject_id, grade) VALUES(?,?,?)",
                             (student_id, subject_id, grade))
        self.connexion.commit()
        
    def supprimer(self, id):
        self.curseur.execute("DELETE FROM grades WHERE id = ?", (id,))
        self.connexion.commit()

    def update(self, id, student_id, subject_id, grade):  
        self.curseur.execute(
            "UPDATE grades SET student_id = ?, subject_id = ?, grade = ? WHERE id = ?",
            (student_id, subject_id, grade, id)
        )
        self.connexion.commit()

    def rechercher(self, id):
        self.curseur.execute("SELECT * FROM grades WHERE id = ?", (id,))
        return self.curseur.fetchone()
    def rechercher_par_etudiant(self, student_id):
        self.curseur.execute("SELECT * FROM grades WHERE student_id = ?", (student_id,))
        return self.curseur.fetchall()
    def rechercher_par_matiere(self, subject_id):
        self.curseur.execute("SELECT * FROM grades WHERE subject_id = ?", (subject_id,))
        return self.curseur.fetchall()
    def rechercher_par_etudiant_et_matiere(self, student_id, subject_id):
        self.curseur.execute("SELECT * FROM grades WHERE student_id = ? AND subject_id = ?", (student_id, subject_id))
        return self.curseur.fetchone()
    
    