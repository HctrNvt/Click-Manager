from app import Application
import game


def loadSave(fileName):
    with open("saves/"+fileName,"r") as f:
        return f.read()

app = Application(game.Game(None))
if __name__ == "__main__":
    app.root.mainloop()
