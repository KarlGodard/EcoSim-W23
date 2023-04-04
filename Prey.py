from Animal import Animal
import random
from random import randrange
from SensoryRange import SensoryRange
from Action import DieAction
from Action import EatAction
from Action import MoveAction
from Action import ReproduceAction
from Action import DrinkAction


class Prey(Animal):

    def __init__(self,
                 xmax,
                 ymax,
                 positionX=None,
                 positionY=None,
                 animalID=None):
        self.currFood = random.randint(37, 75)
        self.maxFood = 75
        self.currWater = 75
        self.maxWater = 75
        self.isFemale = random.choice([0, 1])
        self.isPrey = 1
        self.isFertile = 0
        self.animalID = animalID
        if positionX == None:
            self.setRandomLocation()
        else:
            self.positionX = positionX
            self.positionY = positionY
        self.alive = 1
        self.xmax = xmax
        self.ymax = ymax
        self.age = 0
        self.reprDelay = 0

    def reproduce(self, surroundings):
        nearbyMates = surroundings.getNearbyMates()
        for i in nearbyMates:

            # can mate: opposite genders, both fertile, other didnt move
            # neither animal moves
            # animal is reproducing
            actionList = []
            reproduceAction = ReproduceAction()
            reproduceAction.setAnimalType("prey")

            openTiles = self.getOpenTiles(surroundings)
            reproduceAction.setBirthLocation(random.choice(openTiles))
            reproduceAction.setPartnerLocation(i)

            actionList.append(reproduceAction)

            self.reprDelay = 0
            return actionList

    def preyReact(self, animalSr):
        #print(self.currFood)
        # make use_resource function: use food and water (small amts) for any action; call it here

        # self.currWater -= self.maxWater * 0.05
        # self.currFood -= self.maxFood * 0.05
        currentActionList = []

        self.checkState()  #check if it is alive
        #self.tempReact(animal_sr)
        # if self.alive == 0:
        #     #del(self) #don't need this anymore
        #     dieAction = DieAction()
        #     currentActionList.append(dieAction)
        #     return currentActionList
        #     # tell sim to delete self

        # if self.currFood < (0.75 * self.maxFood):
        #     actionList = self.eatPlant(
        #         animalSr
        #     )  #should be a list with coords of plant and 2, or None if nothing was eaten

        #     if actionList:
        #         return actionList

        # if self.currWater < (.75 * self.maxWater):
        #     actionList = self.waterReact(animalSr)
        #     if actionList:
        #         return actionList

        # if self.checkIsFertile():
        #     actionList = self.reproduce(animalSr)

        #     if actionList:
        #         return actionList

        # if nothing happens, will randomly move

        moveAction = MoveAction()
        currLocation = (self.positionX, self.positionY)

        invalidLocs = animalSr.getNearbyPrey(
        ) + animalSr.getNearbyPredators() + animalSr.getNearbyWater(
        ) + animalSr.getNearbyPlants()

        self.randomMove(invalidLocs)

        endLocation = (self.positionX, self.positionY)
        if endLocation not in invalidLocs:
            moveAction.setstartLocation(currLocation)
            moveAction.setendLocation(endLocation)
            currentActionList.append(moveAction)

        return currentActionList
