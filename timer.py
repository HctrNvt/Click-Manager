class Temps:
    def __init__(self, temps):
        self.temps = temps
    def getTemps(self):
        return self.temps
    def tick(self):
        # Passe le temps d'une unité
        self.temps += 1