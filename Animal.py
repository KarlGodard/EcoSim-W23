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
            moveaction.setendLocation((self.position_x + dx, self.position_y + dy))
    
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
    
    # def tempReact(self, surroundings):
    #     temp = surroundings.getTemp()
    #     # temp too high or low, animal dies
    #     if temp > 110 or temp < 0:
    #         rand = randrange(0, 1600)
    #         # so some animals die
    #     if (rand < min((temp - 110)**2, (temp)**2)):
    #         self.kill(self)

    def checkIsFertile(self):
        if self.currFood < (self.maxFood * 0.75) or self.currWater < (
                self.maxWater * 0.75):  #changed from 0.5
            self.isFertile = 0
        else:
            self.isFertile = 1
            # do age later






