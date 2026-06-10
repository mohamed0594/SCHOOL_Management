from database.base_principale import baseDonees

class TeacherModels(baseDonees):
    def __init__(self):
        super().__init__()

    def Ajouter(self, nom, prenom, email, password):
        self.curseur.execute("INSERT INTO teachers(nom, prenom, email, password) VALUES(?,?,?,?)",
                             (nom, prenom, email, password))
        self.connexion.commit()
        
    def supprimer(self, id):
        self.curseur.execute("DELETE FROM teachers WHERE id = ?", (id,))
        self.connexion.commit()

    def update(self, id, nom, prenom, email, password):  
        self.curseur.execute(
            "UPDATE teachers SET nom = ?, prenom = ?, email = ?, password = ? WHERE id = ?",
            (nom, prenom, email, password, id)
        )
        self.connexion.commit()

    def rechercher(self, id):
        self.curseur.execute("SELECT * FROM teachers WHERE id = ?", (id,))
        return self.curseur.fetchone()
    def login_conexion(self, email, password):
        self.curseur.execute(
            "SELECT * FROM teachers WHERE email = ? AND password = ?",
            (email, password)
        )
        return self.curseur.fetchone()
    
    