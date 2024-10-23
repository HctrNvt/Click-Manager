import json
from entite import Joueur,BonusStatique,EffetStatique
class Game:
    def __init__(self,sauvegarde):
        self.load(sauvegarde)
    def registerBonus(self):
        self.bonus = []
        self.bonus.append(BonusStatique("Nouvelle souris",100,EffetStatique(1)))
        self.bonus.append(BonusStatique("Amis qui cliquent",850,EffetStatique(5)))
        self.bonus.append(BonusStatique("Souris en or",10000,EffetStatique(25)))
        
    def clique(self):
        self.joueur.clic()
    def load(self,sauvegarde):
        # On enregistre toute les informations qui ne sont pas dans une save
        self.registerBonus()
        
        # On charge la sauvegarde
        if sauvegarde != None:
            data = json.loads(sauvegarde)
            print("sauvegarde chargee")
            self.joueur = Joueur(data["joueur"]["nom"],data["joueur"]["score"])
    def save(self):
        pass