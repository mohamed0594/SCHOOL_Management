from database.base_principale import baseDonees



class UtilisateursModels(baseDonees):
    def __init__(self):
        super().__init__()

    def Ajouter(self, nom, role):
        self.curseur.execute("INSERT INTO users(nom, role) VALUES(?,?)",
                             (nom, role))
        
    def supprimer(self,id  ):
        self.curseur.execute("DELETE FROM  users WHERE id = ? "
                             ,(id,))
        self.connexion.commit()

    def update(self,id, nom, role ):
        self.curseur.execute("UPDATE users set id = ?, nom = ?, role = ?"
                             
                             ,(id, nom, role))
        
    def Afficher(self):
        self.curseur.execute("SELECT * FROM users ")


        

    

    


    




