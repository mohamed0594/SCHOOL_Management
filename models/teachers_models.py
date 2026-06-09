from database.base_principale import BaseDonnees

class TeacherModels(BaseDonnees):

    def Ajouter(self, nom, matiere):
        self.curseur.execute(
            "INSERT INTO teachers(nom, matiere) VALUES (?,?)",
            (nom, matiere)
        )
        self.connexion.commit()

    def Afficher(self):
        self.curseur.execute("SELECT * FROM teachers")
        return self.curseur.fetchall()