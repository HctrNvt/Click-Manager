class SaveAble:
    def __init__(self) -> None:
        self.attributs = {}
        pass

class Entite(SaveAble):
    def __init__(self,id:str):
        super().__init__()
        self.attributs.update({"id":id})
    def getId(self):
        return self.attributs["id"]
class Bonus(Entite):
    """
    Bonus classique pour le joueur, ajoute des points quand on clic, simplement.
    """
    def __init__(self,id:str,prix:int,nb:int):
        super().__init__(id)
        self.attributs.update({"prix":prix})
        self.attributs.update({"nb":nb})
    def getNb(self):
        return self.attributs["nb"]
    def getPrix(self):
        return self.attributs["prix"]
    def getName(self):
        return self.attributs["id"]

class Joueur(Entite):
    def __init__(self,id:str,score:int):
        super().__init__(id)
        self.attributs.update({"score":score})
        self.attributs.update({"bonus":{}})

    def ajouterBonus(self,bonusIndex:int):
        """
        Ajoute un aux nombre de bonus du joueur.
        Si l'index est possible alors il n'y aura pas d'erreurs
        """
        bonusJoueur = self.attributs["bonus"]
        bonusJoueur[bonusIndex] += 1
    
    def clic(self,game):
        self.ajouterScore(1)
        nbDeBonusJoueur = self.attributs["bonus"]
        i = 0
        for y in game.bonus[0]: # Pour chaque bonus
            # Récupère les attribut de l'effet du bonus
            effet = y.getNb()
            
            # Applique l'effet en fonction (éviter la boucle for fait plaisir quand même)
            self.ajouterScore( effet * nbDeBonusJoueur[i] )
            
            i += 1

    def ajouterScore(self,score):
        self.attributs["score"] += score
    def setScore(self,score):
        self.attributs["score"] = score