from database.base_principale import BaseDonnees


class StudentModels(BaseDonnees):
    def __init__(self):
        super().__init__()
# creation de CRUD students

    def Ajouter(self, matricule, nom, prenom, age, classe):
        self.curseur.execute(
    
        """
         INSERT INTO students(matricule, nom, prenom, age, classe)
         VALUES (?,?,?,?,?)
         

        """,(matricule, nom, prenom, age, classe)
        
        )
        self.connexion.commit()
    def Supprimer(self, id):
        self.curseur.execute(
        """
            DELETE FROM students 
            WHERE id = ?


        """, (id,)
        )
        self.connexion.commit()
    
    def MiseAJour(self, id , matricule, nom, prenom, age, classe):
        self.curseur.execute(
        """
            UPDATE students 
            set matricule = ? ,  nom = ? , prenom  = ? ,  age = ?, classe = ?
            WHERE id = ? 


        """,( matricule, nom, prenom, age , classe, id)
        )
        self.connexion.commit()

    def Afficher(self):
        self.curseur.execute("SELECT * FROM students")
        return self.curseur.fetchall()
    
