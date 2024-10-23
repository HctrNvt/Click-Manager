import json
from entite import Joueur
class Game:
    def __init__(self,sauvegarde):
        self.load(sauvegarde)
    def load(self,sauvegarde):
        data = json.loads(sauvegarde)
        print("sauvegarde chargee")
        self.joueur = Joueur(data["joueur"]["nom"],data["joueur"]["score"])
        
    def save(self):
        pass