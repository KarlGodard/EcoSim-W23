import random
from random import randrange
from SensoryRange import SensoryRange
from Action import DieAction
from Action import EatAction
from Action import MoveAction
from Action import ReproduceAction
from Action import DrinkAction


class Animal:

    def __init__(self, xmax, ymax, position_x=None, position_y=None):
        self.currFood
        self.maxFood
        self.currWater
        self.maxWater
        self.is_female = random.choice[0, 1]
        self.isPrey
        self.isFertile = 0

        if position_x == None:
            self.set_random_location()
        else:
            self.position_x = position_x
            self.position_y = position_y
        self.alive = 1
        self.xmax = xmax
        self.ymax = ymax
        self.age = 0
        self.reprDelay = 0

    def move(self, dx, dy, xmax, ymax):
        # print out of bounds statement for edges
        self.position_x = (self.position_x + dx) % xmax
        self.position_y = (self.position_y + dy) % ymax
        return (self.position_x, self.position_y)

    def kill(self):
        self.alive = 0

    def check_state(self):
        if self.currFood <= 0 or self.currWater <= 0:
            self.kill()

    def random_move(self, invalid_locs=[]):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])

        while (dx + self.position_x, dy + self.position_y) in invalid_locs:
            dx = random.choice([-1, 0, 1])
            dy = random.choice([-1, 0, 1])

        return self.move(dx, dy, self.xmax, self.ymax)

    def set_random_location(self):
        x_loc = random.randint(0, self.xmax - 1)
        y_loc = random.randint(0, self.ymax - 1)
        self.position_x = x_loc
        self.position_y = y_loc

    def getOpenTiles(self, surroundings):
        loc = (self.position_x, self.position_y)
        locs_empty_tile = []
        # search distance
        search_dist = 1
        min_x = max(0, loc[0] - search_dist)
        max_x = min(self.size_x, loc[0] + search_dist + 1)
        min_y = max(0, loc[1] - search_dist)
        max_y = min(self.size_y, loc[1] + search_dist + 1)
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                newTile = self.locToTile((i, j))
                if newTile.has_pred == 0 and newTile.has_prey == 0 and newTile.has_water == 0:
                    locs_empty_tile.append((i, j))

        return locs_empty_tile

    def eatPlant(self, surroundings):
        action_list = []
        # nearbyFood is coordinate of nearest plant
        nearbyPlants = surroundings.getNearbyPlants()

        if nearbyPlants == []:
            # returns None if cannot eat plant
            return action_list
        for loc in nearbyPlants:
            #eat plant if location is found adjacent to the animal
            if (max(abs(loc[0] - self.position_x),
                    abs(loc[1] - self.position_y)) <= 1):
                self.currFood += (0.25 * self.maxFood)
                # returns the coordinate of the water
                action_eat = EatAction()
                action_eat.setFoodType("plant")
                action_eat.setFoodLocation(loc)
                action_list.append(action_eat)
                return action_list

        #move towards the nearest food location
        #TODO: move towards NEAREST plant, not just the first plant observed
        invalid_locs = surroundings.getNearbyPrey(
        ) + surroundings.getNearbyPredators() + surroundings.getNearbyWater()

        moveaction = self.genMoveAction(nearbyPlants[0], invalid_locs)
        if moveaction is not None:
            action_list.append(moveaction)
        return action_list

    def genMoveAction(self, target, invalid_locs):
        dx = -1
        dy = -1
        if target[0] > self.position_x:
            dx = 1
        elif target[0] == self.position_x:
            dx = 0
        if target[1] > self.position_y:
            dy = 1
        elif target[1] == self.position_y:
            dy = 0
        destination = (self.position_x + dx, self.position_y + dy)

        if destination not in invalid_locs:
            moveaction = MoveAction()
            moveaction.setstartLocation((self.position_x, self.position_y))
            moveaction.setendLocation(
                (self.position_x + dx, self.position_y + dy))

            self.position_x += dx
            self.position_y += dy
            return moveaction
        return None

    def waterReact(self, surroundings):
        # check what's around
        action_list = []
        nearbyWater = surroundings.getNearbyWater()
        if nearbyWater == []:

            return action_list

        for loc in nearbyWater:
            if (max(abs(loc[0] - self.position_x),
                    abs(loc[1] - self.position_y)) <= 1):
                self.currWater += (0.25 * self.maxWater)
                # returns the coordinate of the water
                action_drink = DrinkAction()
                action_list.append(action_drink)
                return action_list

        invalid_locs = surroundings.getNearbyPrey(
        ) + surroundings.getNearbyPredators() + surroundings.getNearbyWater()

        moveaction = self.genMoveAction(nearbyWater[0], invalid_locs)
        if moveaction is not None:
            action_list.append(moveaction)

        return action_list

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
