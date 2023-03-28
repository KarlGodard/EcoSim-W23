class SensoryRange:

    def __init__(self,
                 nearbyAnimals=[],
                 nearbyPlants=[],
                 nearbyWater=[],
                 temp=-1):

        self.temp = temp
        self.nearbyPredators = []  # list of predator animal objects
        self.nearbyPrey = []  # list of predator animal objects
        self.nearbyPlants = nearbyPlants  # coordinate of nearest food
        self.nearbyWater = nearbyWater  # coordinate of nearest water 
        self.viableMates = []

    def setNearbyPredators(self, preds):
        self.nearbyPredators = preds

    def setNearbyPrey(self, prey):
        self.nearbyPrey = prey

    def setNearbyPlants(self, loc):
        self.nearbyPlants = loc

    def setNearbyWater(self, loc):
        self.nearbyWater = loc

    def setViableMates(self, mates):
        self.viableMates = mates

      
    def setTemp(self, temp):
        self.temp = temp

    def getNearbyPredators(self):
        return self.nearbyPredators

    def getNearbyPrey(self):
        return self.nearbyPrey

    def getNearbyPlants(self):
        return self.nearbyPlants

    def getNearbyWater(self):
        return self.nearbyWater

    def getViableMates(self, mates):
        return self.viableMates

      
    def getTemp(self):
        return self.temp
