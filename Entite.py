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

class Effet(Entite):
    def __init__(self,opérateur:str,bonus:int):
        super().__init__("Effet")
        self.attributs.update({"op":opérateur})
        self.attributs.update({"nb":bonus})

# C'est un bonus que le joueur peut acheter 
# Il s'applique quand le joueur clic, PAS passif
class Bonus(Entite):
    def __init__(self,id:str,prix:int,effet:Effet):
        super().__init__(id)
        self.attributs.update({"prix":prix})
        self.attributs.update({"effet":effet.attributs})

class Joueur(Entite):
    def __init__(self,id:str,score:int):
        super().__init__(id)
        self.attributs.update({"score":score})
        self.attributs.update({"bonus":{}})

    def ajouterBonus(self,bonusIndex:int):
        """Ajoute un bonus au joueur. Si le bonus est déjà présent, ajoute +1 à son compteur.
        Sinon, l'ajoute avec un compteur de 1."""
        bonusJoueur = self.attributs["bonus"]
        bonusJoueur[bonusIndex] += 1
    
    def clic(self,game):
        bonuss = self.attributs["bonus"]
        for i in range(len(bonuss)): # Pour chaque bonus
            if bonuss[i] > 0:
                effet = game.bonus[i].attributs["effet"] # Récupère les attribut de l'effet du bonus
                # Applique l'effet en fonction
                if effet["op"] == "+":
                    self.ajouterScore( effet["nb"] * bonuss[i] )
                if effet["op"] == "*":
                    self.multiplieScore( effet["nb"] * bonuss[i] )
        self.ajouterScore(1)
    def ajouterScore(self,score):
        self.attributs["score"] += score
    def multiplieScore(self,score):
        self.attributs["score"] *= score