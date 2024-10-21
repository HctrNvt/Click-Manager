class Entite:
    def __init__(self,nom):
        self.nom = nom
    def getNom(self):
        return self.nom

class Joueur(Entite):
    def __init__(self,nom):
        super().__init__(nom)