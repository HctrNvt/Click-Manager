import json
from entite import Joueur,Bonus,Effet
class Game:
    def __init__(self,sauvegarde):
        self.load(sauvegarde)
    def registerBonus(self):
        self.bonus = [] # Si on change l'ordre d'enregistrement, les saves seront corrompus
        self.bonus.append(Bonus("Nouvelle souris",100,Effet("+",1)))
        self.bonus.append(Bonus("Amis qui cliquent",850,Effet("+",5)))
        self.bonus.append(Bonus("Souris en or",10000,Effet("+",25)))
        
        self.joueur.attributs["bonus"] = [0]*len(self.bonus)
    def clic(self):
        self.joueur.clic(self)
        print(self.joueur.attributs["score"])
    def load(self,sauvegarde):
        # On charge la sauvegarde
        if sauvegarde != None:
            data = json.loads(sauvegarde)
            print("sauvegarde chargee")
            self.joueur:Joueur = Joueur(data["joueur"]["nom"],data["joueur"]["score"])
        else: # On fait cette zone la pour les essais
            self.joueur:Joueur = Joueur("Joueur",0)
        
        # On enregistre toute les informations qui ne sont pas dans une save
        self.registerBonus()

    def tryBuy(self,bonusIndex:int):
        prix = self.bonus[bonusIndex].attributs["prix"]
        if self.joueur.attributs["score"] >= prix:
            self.joueur.ajouterBonus(bonusIndex)
            self.joueur.ajouterScore(-prix)
            return True
        return False
    def save(self,fileName):
        with open("saves/"+fileName,"w") as f:
            json.dump({"joueur":self.joueur.attributs},f)