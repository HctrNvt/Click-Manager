import tkinter as tk

class Application:
    elements = []
    def __init__(self,game):
        self.game = game
        
        self.root = tk.Tk() 
        self.root.title("Clicker")
        self.root.geometry("600x600")
        # Création de la page de base
        self.main()
    def main(self):
        self.clear()

        # Création d'un bouton
        self.button = tk.Button(self.root, text="Cliquez ici", command=self.clic)
        self.elements.append(self.button)
        
        self.amelioration = tk.Button(self.root, text="Boutique", command=self.boutique)
        self.elements.append(self.amelioration)
        
        # Création d'un label pour afficher le résultat
        self.label_result = tk.Label(self.root, text="")
        self.elements.append(self.label_result)
        
        self.pack()
        self.updateCounter()
    def boutique(self):
        self.clear()
        self.button = tk.Button(self.root, text="Retour", command=self.main)
        self.elements.append(self.button)
        
        self.buttona = tk.Button(self.root, text=self.game.bonus[0].attributs["id"], command=lambda: self.buy(0))
        self.elements.append(self.buttona)
        
        self.button1 = tk.Button(self.root, text=self.game.bonus[1].attributs["id"], command=lambda: self.buy(1))
        self.elements.append(self.button1)
        
        self.button2 = tk.Button(self.root, text=self.game.bonus[2].attributs["id"], command=lambda: self.buy(2))
        self.elements.append(self.button2)
        
        self.button3 = tk.Button(self.root, text=self.game.bonus[3].attributs["id"], command=lambda: self.buy(3))
        self.elements.append(self.button3)
        
        self.button4 = tk.Button(self.root, text=self.game.bonus[4].attributs["id"], command=lambda: self.buy(4))
        self.elements.append(self.button4)
        
        self.button5 = tk.Button(self.root, text=self.game.bonus[5].attributs["id"], command=lambda: self.buy(5))
        self.elements.append(self.button5)
        
        
        self.pack()
    def pack(self):
        for element in self.elements:
            element.pack()
    def clear(self):
        self.elements.clear()
        for i in self.root.winfo_children():
            i.destroy()
    def updateCounter(self):
        self.label_result["text"] = self.game.joueur.attributs["score"]
    def clic(self):
        self.game.clic()
        self.updateCounter()
    def buy(self,index):
        print("buy")
        self.game.tryBuy(index)
