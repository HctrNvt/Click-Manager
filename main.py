from app import Application
import game
app = Application(game.Game(None))
if __name__ == "__main__":
    app.root.mainloop()
