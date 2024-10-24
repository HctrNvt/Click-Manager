import tkinter as tk

class Application:
    elements = []
    def __init__(self,game):
        self.game = game
        
        self.root = tk.Tk() 
        self.root.title("Clicker")
        self.root.geometry("800x800")
        # Création d'un label
        self.label = tk.Label(self.root, text="Entrez quelque chose :")
        self.elements.append(self.label)
        
        # Création d'une entrée de texte
        self.entry = tk.Entry(self.root, width=30)
        self.elements.append(self.entry)

        # Création d'un bouton
        self.button = tk.Button(self.root, text="Cliquez ici", command=self.clic)
        self.elements.append(self.button)
        
        self.amelioration = tk.Button(self.root, text="Amélioration", command=self.buy)
        self.elements.append(self.amelioration)
        
        # Création d'un label pour afficher le résultat
        self.label_result = tk.Label(self.root, text="")
        self.elements.append(self.label_result)
        
        self.pack()
    def pack(self):
        for element in self.elements:
            element.pack()
    def updateCounter(self):
        self.label_result["text"] = self.game.joueur.attributs["score"]
    def clic(self):
        self.game.clic()
        self.updateCounter()
    def buy(self):
        self.game.tryBuy(0)
        self.updateCounter()
