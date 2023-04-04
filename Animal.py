import random
from random import randrange
from SensoryRange import SensoryRange
from Action import DieAction
from Action import EatAction
from Action import MoveAction
from Action import ReproduceAction
from Action import DrinkAction


class Animal:

    def __init__(self):
        pass

    def move(self, dx, dy, xmax, ymax):
        # print out of bounds statement for edges
        self.positionX = (self.positionX + dx) % xmax
        self.positionY = (self.positionY + dy) % ymax
        return (self.positionX, self.positionY)

    def kill(self):
        self.alive = 0

    def checkState(self):
        if self.currFood <= 0 or self.currWater <= 0:
            self.kill()

    def randomMove(self, invalidLocs=[]):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])

        while (dx + self.positionX, dy + self.positionY) in invalidLocs:
            dx = random.choice([-1, 0, 1])
            dy = random.choice([-1, 0, 1])

        return self.move(dx, dy, self.xmax, self.ymax)

    def setRandomLocation(self):
        xLoc = random.randint(0, self.xmax - 1)
        yLoc = random.randint(0, self.ymax - 1)
        self.positionX = xLoc
        self.positionY = yLoc

    def getOpenTiles(self, surroundings):
        loc = (self.positionX, self.positionY)
        locsEmptyTile = []
        # search distance
        searchDist = 1
        minX = max(0, loc[0] - searchDist)
        maxX = min(self.xmax, loc[0] + searchDist + 1)
        minY = max(0, loc[1] - searchDist)
        maxY = min(self.ymax, loc[1] + searchDist + 1)
        for i in range(minX, maxX):
            for j in range(minY, maxY):
                if (i,j) not in surroundings.getNearbyPrey() and (i,j) not in surroundings.getNearbyPredators() and (i,j) not in surroundings.getNearbyWater():
                    locsEmptyTile.append((i, j))

        return locsEmptyTile

    
  
   


    def genMoveAction(self, target, invalidLocs):
        dx = -1
        dy = -1
        if target[0] > self.positionX:
            dx = 1
        elif target[0] == self.positionX:
            dx = 0
        if target[1] > self.positionY:
            dy = 1
        elif target[1] == self.positionY:
            dy = 0
        destination = (self.positionX + dx, self.positionY + dy)

        if destination not in invalidLocs:
            moveaction = MoveAction()
            moveaction.setstartLocation((self.positionX, self.positionY))
            moveaction.setendLocation(
                (self.positionX + dx, self.positionY + dy))

            self.positionX += dx
            self.positionY += dy
            return moveaction
        return None

    def waterReact(self, surroundings):
        # check what's around
        actionList = []
        nearbyWater = surroundings.getNearbyWater()
        if nearbyWater == []:

            return actionList

        for loc in nearbyWater:
            if (max(abs(loc[0] - self.positionX),
                    abs(loc[1] - self.positionY)) <= 1):
                self.currWater += (0.25 * self.maxWater)
                # returns the coordinate of the water
                drinkAction = DrinkAction()
                actionList.append(drinkAction)
                return actionList

        invalidLocs = surroundings.getNearbyPrey(
        ) + surroundings.getNearbyPredators() + surroundings.getNearbyWater()

        moveaction = self.genMoveAction(nearbyWater[0], invalidLocs)
        if moveaction is not None:
            actionList.append(moveaction)

        return actionList

    def checkIsFertile(self):
        if self.currFood < (self.maxFood * 0.75) or self.currWater < (
                self.maxWater * 0.75
        ) or self.age < 10 or self.reprDelay < 5:  #changed from 0.5
            self.isFertile = 0
        else:
            self.isFertile = 1

        return self.isFertile

    def resetReprDelay(self):
        self.reprDelay = 0
