
class SimulationParams():
    def __init__(self):
        self.simulationLength = 25
        self.simluationSpeed = 800
        

class MapParams():
    def __init__(self):
        self.sizeX = 50
        self.sizeY = 30
        self.percentWaterCoverage = 30
        self.numStartingPredators = 50
        self.numStartingPrey = 50
        self.temp = 70

class AnimalParams():
    def __init__(self):
        self.maxFood = 100
        self.maxWater = 100
        self.minReproductiveAge = 5
        self.reproductiveDelay = 5
        self.waterSearchRadius = 2
        self.foodSearchRadius = 2
        self.reproductiveSearchRadius = 2
        self.hungerIncreasePercentage = .03
        self.thirstIncreasePercentage = .03
        self.hungerDecreasePercentage = .25
        self.thirstDecreasePercentage = .25
        self.minReprocutiveHunger = .50
        self.minReproductiveThirst = .50
        
