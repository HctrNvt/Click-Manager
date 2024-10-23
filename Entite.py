class SaveAble:
    def __init__(self) -> None:
        self.attributs = {}
        pass

class Entite(SaveAble):
    def __init__(self,id):
        super().__init__()
        self.attributs.update({"id":id})
    def getId(self):
        return self.attributs["id"]

class Effet(Entite):
    def __init__(self,opérateur,bonus):
        super().__init__("Effet")
        if opérateur == "+":
            self.attributs.update({"+":bonus})
        elif opérateur == "*":
            self.attributs.update({"*":bonus})

# C'est un bonus que le joueur peut acheter 
# Il s'applique quand le joueur clic, PAS passif
class BonusStatique(Entite):
    def __init__(self,id,prix,effet:Effet):
        super().__init__(id)
        self.attributs.update({"prix":prix})
        self.attributs.update({"effet":effet.attributs})

class Joueur(Entite):
    def __init__(self,id,score):
        super().__init__(id)
        self.attributs.update({"score":score})
        self.attributs.update({"bonus":{}})

    def ajouterBonus(self,bonus):
        """Ajoute un bonus au joueur. Si le bonus est déjà présent, ajoute +1 à son compteur.
        Sinon, l'ajoute avec un compteur de 1."""
        if bonus.getId() in self.attributs["bonus"]:
            self.attributs["bonus"][bonus.getId()] += 1
        else:
            self.attributs["bonus"][bonus.getId()] = 1
    def clic(self):
        self.ajouterScore(1)
    def ajouterScore(self,score):
        self.attributs["score"] += score
