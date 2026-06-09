from database.base_principale import baseDonnees
class SubjectsModels(baseDonnees):
    def __init__(self):
        super().__init__()

    def Ajouter(self, nom, description):
        self.curseur.execute("INSERT INTO subjects(nom, description) VALUES(?,?)",
                             (nom, description))
        self.connexion.commit()
        
    def supprimer(self, id):
        self.curseur.execute("DELETE FROM subjects WHERE id = ?", (id,))
        self.connexion.commit()

    def update(self, id, nom, description):  
        self.curseur.execute(
            "UPDATE subjects SET nom = ?, description = ? WHERE id = ?",
            (nom, description, id)
        )
        self.connexion.commit()

    def rechercher(self, id):
        self.curseur.execute("SELECT * FROM subjects WHERE id = ?", (id,))
        return self.curseur.fetchone()
    