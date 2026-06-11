from database.base_donnees import BaseDonnees
class userModel(BaseDonnees):
    def __init__(self):
        super().__init__()
        super().users()

    def ajouter_users(self, nom,role, email, mot_de_passe):
            self.curseur.execute(
                """
                INSERT INTO users (nom, role, email, mot_de_passe)
                VALUES (?, ?, ?, ?)
                """,
                (nom, role, email, mot_de_passe)
            )
            self.connexion.commit()

    def afficher_users(self):
            self.curseur.execute(
                """
                SELECT * FROM users
                """
            )
            return self.curseur.fetchall()
    
    def modifier_users(self, id, nom, role, email, mot_de_passe):
            self.curseur.execute(
                """
                UPDATE users
                SET nom = ?, role = ?, email = ?, mot_de_passe = ?
                WHERE id = ?
                """,
                (nom, role, email, mot_de_passe, id)
            )
            self.connexion.commit()

    def supprimer_users(self, id):
            self.curseur.execute(
                """
                DELETE FROM users
                WHERE id = ?
                """,
                (id,)
            )
            self.connexion.commit()

            self.fermeture()
    def login(self, email, mot_de_passe):
            self.curseur.execute(
                """
                SELECT * FROM users
                WHERE email = ? AND mot_de_passe = ?
                """,
                (email, mot_de_passe)
            )
            return self.curseur.fetchone()

            