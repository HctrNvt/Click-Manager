import tkinter as tk

class Application:
    elements = []
    def __init__(self):
        self.root = tk.Tk() 
        self.root.title("Clicker")
        self.root.geometry("300x200")

        # Création d'un label
        self.label = tk.Label(self.root, text="Entrez quelque chose :")
        self.elements.append(self.label)
        

        # Création d'une entrée de texte
        self.entry = tk.Entry(self.root, width=30)
        self.elements.append(self.entry)

        # Création d'un bouton
        self.button = tk.Button(self.root, text="Cliquez ici", command=self.on_button_click)
        self.elements.append(self.button)

        # Création d'un label pour afficher le résultat
        self.label_result = tk.Label(self.root, text="")
        self.elements.append(self.label_result)
        
        self.pack()
    def pack(self):
        for element in self.elements:
            element.pack()
    def on_button_click(self):
        user_input = self.entry.get()
        self.label_result.config(text=f"Vous avez écrit : {user_input}")
