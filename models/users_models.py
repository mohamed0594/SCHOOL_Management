from database.base_principale import baseDonees

class UtilisateursModels(baseDonees):
    def __init__(self):
        super().__init__()

    def Ajouter(self, nom, role, password,  email):
        self.curseur.execute("INSERT INTO users(nom, role, password,  email) VALUES(?,?,?,?)",
                             (nom, role, password,  email))
        self.connexion.commit()
        
    def supprimer(self, id):
        self.curseur.execute("DELETE FROM users WHERE id = ?", (id,))
        self.connexion.commit()

    def update(self, id, nom, role, password,  email):  
        self.curseur.execute(
            "UPDATE users SET nom = ?, role = ?, password = ?,  email = ? WHERE id = ?",
            (nom, role, password,  email, id)
        )
        self.connexion.commit()

    def rechercher(self, id):
        self.curseur.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.curseur.fetchone()
    
    def se_connecter(self, email, password):
     self.curseur.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (email, password)
    )
     return self.curseur.fetchone()
    
    

    
    
    
    
    
   