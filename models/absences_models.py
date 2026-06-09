from database.base_principale import baseDonnees
class AbsencesModels(baseDonnees):
    def __init__(self):
        super().__init__()

    def Ajouter(self, student_id, subject_id, date, reason):
        self.curseur.execute("INSERT INTO absences(student_id, subject_id, date, reason) VALUES(?,?,?,?)",
                             (student_id, subject_id, date, reason))
        self.connexion.commit()
        
    def supprimer(self, id):
        self.curseur.execute("DELETE FROM absences WHERE id = ?", (id,))
        self.connexion.commit()

    def update(self, id, student_id, subject_id, date, reason):  
        self.curseur.execute(
            "UPDATE absences SET student_id = ?, subject_id = ?, date = ?, reason = ? WHERE id = ?",
            (student_id, subject_id, date, reason, id)
        )
        self.connexion.commit()

    def rechercher(self, id):
        self.curseur.execute("SELECT * FROM absences WHERE id = ?", (id,))
        return self.curseur.fetchone()
    def rechercher_par_etudiant(self, student_id):
        self.curseur.execute("SELECT * FROM absences WHERE student_id = ?", (student_id,))
        return self.curseur.fetchall()
    def rechercher_par_matiere(self, subject_id):
        self.curseur.execute("SELECT * FROM absences WHERE subject_id = ?", (subject_id,))
        return self.curseur.fetchall()
    def rechercher_par_etudiant_et_matiere(self, student_id, subject_id):
        self.curseur.execute("SELECT * FROM absences WHERE student_id = ? AND subject_id = ?", (student_id, subject_id))
        return self.curseur.fetchall()
    
