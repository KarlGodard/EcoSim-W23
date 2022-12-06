class Action:
    def __init__(self, actionType=None):
        self.type = actionType

    def setActionType(self, actionType):
        self.type = actionType

class EatAction(Action):
    def __init__(self):
        self.type = "eat"
        self.foodType = None
        self.foodLocation = (0,0)

    def setFoodLocation(self, foodLocation):
        self.foodLocation = foodLocation

    def setFoodType(self, foodType):
        self.foodType = foodType

    def getFoodType(self):
        return self.foodType

    def getFoodLocation(self):
        return self.foodLocation

class MoveAction(Action):
    def __init__(self):
        self.type = "move"
        self.startLocation = (0,0)
        self.endLocation = (0,0)

    def setstartLocation(self, startLocation):
        self.startLocation = startLocation

    def setendLocation(self, endLocation):
        self.endLocation = endLocation

    def getstartLocat(self):
        return self.startLocation

    def getendLocation(self):
        return self.endLocation

class ReproduceAction(Action):
    def __init__(self):
        self.type = "reproduce"
        self.startLocation = (0,0)
        self.endLocation = (0,0)
        self.animalType = None

    def setstartLocation(self, startLocation):
        self.startLocation = startLocation

    def setendLocation(self, endLocation):
        self.endLocation = endLocation

    def setAnimalType(self, animalType):
        self.animalType = animalType

    def getstartLocat(self):
        return self.startLocation

    def getendLocation(self):
        return self.endLocation

    def getAnimalType(self):
        return self.animalType



class DrinkAction(Action):
    def __init__(self):
        self.type = "drink"

class DieAction(Action):
    def __init__(self):
        self.type = "die"