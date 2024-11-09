import json
from entite import Joueur,Bonus
class Game:
    def __init__(self,sauvegarde):
        self.load(sauvegarde)
    def registerBonus(self):
        """
        Enregistre les bonus dans le jeu 
        Attention, si l'ordre de l'enregistrement change, les sauvegardes seront invalides
        """
        
        self.bonus = []
        self.bonus.append(# Bonus classique
        [
            Bonus("Nouvelle souris",0,1),
            Bonus("Amis qui cliquent",600,5)
        ])

        
        # self.setNbBonusClassique()
        self.joueur.attributs["bonus"] = [0]*len(self.bonus[0])
    
    def setNbBonusClassique(self):
        """
        Permet de définir le nombre de bonus de classique
        """
        self.nbEffetClassique = len(self.bonus)
        for i in range(len(self.bonus)):
            if self.bonus[i].attributs["effet"]["op"] != "*":
                self.nbEffetClassique = i + 1
    def clic(self):
        """"
        Fait un clic dans le jeu
        """
        self.joueur.clic(self)
        print(self.joueur.attributs["score"])
    def load(self,sauvegarde):
        """
        Charge le jeu à partir d'une sauvegarde ou,
        fais une nouvelle partie
        """
        if sauvegarde != None:
            data = json.loads(sauvegarde)
            print("sauvegarde chargee")
            self.joueur:Joueur = Joueur(data["joueur"]["nom"],data["joueur"]["score"])
        else: # On fait cette zone la pour les essais
            self.joueur:Joueur = Joueur("Joueur",0)
        
        # On enregistre toute les informations qui ne sont pas dans une save
        self.registerBonus()

    def tryBuy(self,bonusIndex:int):
        """
        Essaie d'acheter un bonus
        Si possible : True, sinon False
        """
        # Comment faire cette partie ? Il faut que ça puisse acheter un bonus mais peu importe le type ? 
        prix = self.bonus[bonusIndex].getPrix()
        if self.joueur.attributs["score"] >= prix:
            self.joueur.ajouterBonus(bonusIndex)
            self.joueur.ajouterScore(-prix)
            print(self.joueur.attributs["bonus"])
            return True
        return False
    def save(self,fileName):
        """
        Sauvegarde le jeu dans le fichier précisé (fileName)
        """
        with open("saves/"+fileName,"w") as f:
            json.dump({"joueur":self.joueur.attributs},f)