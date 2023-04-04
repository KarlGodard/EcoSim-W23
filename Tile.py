class Tile:

    def __init__(self, temp=60, terrain="E", water=False, plant=False):
        self.terrain = terrain
        self.occupied = False
        self.animal = False
        self.animalID = -1
        # this is in Fahrenheit because we are Americans
        self.temp = temp
        self.hasWater = water
        self.hasPlant = plant
        self.hasPred = 0
        self.hasPrey = 0

    def getTerrain(self):
        return self.terrain

    def get_organism(self):
        if self.hasPred:
            self.occupied = True
            return "P"
        elif self.hasPrey:
            self.occupied = True
            return "p"
        elif self.hasPlant:
            self.occupied = True
            return "F"
        else:
            self.occupied = False
            return "E"

    # this is a bigger function to just search what lives there

    def isPred(self):
        return self.hasPred

    def isPrey(self):
        return self.hasPrey

    def isPlant(self):
        return self.hasPlant

    def isWater(self):
        return self.hasWater

    def setWater(self):
        self.hasWater = True
        self.occupied = True
        self.terrain = "W"
        return

    def setPlant(self):
        self.hasPlant = True
        self.occupied = True
        self.terrain = "F"
        return

    def setPredator(self):
        self.animal = True
        self.hasPred = self.hasPred + 1
        self.occupied = True
        self.terrain = "P"
        return

    def setPrey(self):
        self.animal = True
        self.hasPrey = self.hasPrey + 1
        self.occupied = True
        self.terrain = "p"
        return

    def isAnimal(self):
        return self.hasPred or self.hasPrey
