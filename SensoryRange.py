class SensoryRange:
    def __init__(self, nearbyAnimals=[], nearbyFood=[],nearbyWater=[], temp=-1):

        self.temp = temp
        self.nearbyPredators = [] # list of predator animal objects
        self.nearbyPrey = [] # list of predator animal objects
        self.nearbyFood = nearbyFood # coordinate of nearest food
        self.nearbyWater = nearbyWater # coordinate of nearest water

    def setNearbyPredators(self, preds):
        self.nearbyPredators = preds

    def setNearbyPrey(self, prey):
        self.nearbyPrey = prey

    def setNearbyFood(self, loc):
        self.nearestFood = loc

    def setNearbyWater(self, loc):
        self.nearestWater = loc

    def setTemp(self, temp):
        self.temp = temp


    def getNearbyPredators(self):
        return self.nearbyPredators

    def getNearbyPrey(self):
        return self.nearbyPrey

    def getNearbyFood(self):
        return self.nearbyFood

    def getNearbyWater(self):
        return self.nearbyWater

    def getTemp(self):
        return self.temp