import tkinter as tk

class Application:
    elements = []
    def __init__(self,game):
        self.game = game
        
        self.root = tk.Tk() 
        self.root.title("Clicker")
        self.root.geometry("600x600")
        
        self.main()
    def main(self):
        """
        Charge la page de base pour l'application
        """
        self.clear()

        # Création d'un bouton
        self.button = tk.Button(self.root, text="Cliquez ici", command=self.clic)
        self.elements.append(self.button)
        
        # Le score du joueur
        self.label_result = tk.Label(self.root, text="")
        self.elements.append(self.label_result)
        
        # Bouton pour ouvrir la boutique
        self.amelioration = tk.Button(self.root, text="Boutique", command=self.boutique)
        self.elements.append(self.amelioration)
        
        self.pack()
        self.updateCounter()
    def boutique(self):
        """
        Charge la page de la boutique pour l'application
        """
        self.clear()
        
        self.button = tk.Button(self.root, text="Retour", command=self.main)
        self.elements.append(self.button)
        
        # Le score du joueur
        self.label_result = tk.Label(self.root, text="")
        self.elements.append(self.label_result)
        
        # On ajoute tout les bonus dans la fenêtre
        i = 0
        for y in self.game.bonus[0]:
            self.elements.append(tk.Button(self.root,
                                    text=y.getName()+" "+str(y.getPrix()),
                                    command=lambda i=i: self.buy(i)))
            i += 1
        
        self.pack()
        self.updateCounter()
    def pack(self):
        for element in self.elements:
            element.pack()
    def clear(self):
        """
        Supprime tout les elements de la page
        """
        self.elements.clear()
        for i in self.root.winfo_children():
            i.destroy()
    def updateCounter(self):
        """
        Met à jour le compteur du joueur sur la page \n
        Besoin : un label qui s'appelle label_result
        """
        self.label_result["text"] = self.game.joueur.attributs["score"]
    def clic(self):
        self.game.clic()
        self.updateCounter()
    def buy(self,index):
        self.game.tryBuy(index)
        self.updateCounter()
