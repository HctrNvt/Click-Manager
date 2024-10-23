class SaveAble:
    self.attributs = []
    def __init__(self) -> None:
        pass

class Entite:
    def __init__(self,nom):
        self.nom = nom
    def getNom(self):
        return self.nom

class Joueur(Entite):
    def __init__(self,nom,score):
        super().__init__(nom)
        self.score = score
    def ajouterScore(self,score):
        self.score += score