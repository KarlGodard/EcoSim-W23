from Animal import Animal
import random
from random import randrange
from SensoryRange import SensoryRange
from Action import DieAction
from Action import EatAction
from Action import MoveAction
from Action import ReproduceAction
from Action import DrinkAction


class Predator(Animal):

    def __init__(self,
                 xmax,
                 ymax,
                 position_x=None,
                 position_y=None,
                 animalID=None):
        self.currFood = random.randint(50, 100)
        self.maxFood = 100
        self.currWater = 100
        self.maxWater = 100
        self.is_female = random.choice([0, 1])
        self.is_prey = 0
        self.is_fertile = 0
        self.animalId = animalID
        if position_x == None:
            self.set_random_location()
        else:
            self.position_x = position_x
            self.position_y = position_y
        self.alive = 1
        self.xmax = xmax
        self.ymax = ymax
        self.age = 0

    def eatPrey(self, surroundings):
        # a list of preys
        action_list = []
        # nearbyFood is coordinate of nearest plant
        nearbyPrey = surroundings.getNearbyPrey()

        if nearbyPrey == []:
            # returns None if cannot eat plant
            return action_list
        for loc in nearbyPrey:
            #eat plant if location is found adjacent to the animal
            if (max(abs(loc[0] - self.position_x),
                    abs(loc[1] - self.position_y)) <= 1):
                self.currFood += (0.25 * self.maxFood)
                # returns the coordinate of the water
                action_eat = EatAction()
                action_eat.setFoodType("animal")
                action_eat.setFoodLocation(loc)
                action_list.append(action_eat)
                return action_list

        #move towards the nearest food location
        invalid_locs = surroundings.getNearbyPrey(
        ) + surroundings.getNearbyPredators() + surroundings.getNearbyWater()
      
        moveaction = self.genMoveAction(nearbyPrey[0], invalid_locs)
        if moveaction is not None:
            action_list.append(moveaction)
        return action_list


  
    def reproduce(self, surroundings):
        nearbyPreds = surroundings.getNearbyPredators()
        for i in nearbyPreds:
            if (i.is_female != self.is_female) and (i.checkIsFertile):
                # can mate: opposite genders, both fertile, other didnt move
                # neither animal moves
                # animal is reproducing
                action_list = []
                reproduce_action = ReproduceAction()
                reproduce_action.setAnimalType(self, "pred")

                open_tiles = self.getOpenTiles(surroundings)
                reproduce_action.setendLocation(random.choice(open_tiles))
              
                action_list.append(reproduce_action)
                return action_list
            else:
                # mating conditions do not work, return False
                return []

    def predReact(self, animal_sr):
        # make use_resource function: use food and water (small amts) for any action; call it here

        # food and water will decrease by 10% no matter what
        self.currWater -= self.maxWater * 0.1
        self.currFood -= self.maxFood * 0.1
        current_action_list = []

        self.check_state()  #check if it is alive
        #self.tempReact()
        if not self.alive:
            die_action = DieAction()
            current_action_list.append(die_action)
            return current_action_list
            # tell sim to delete self

        if self.currFood < (0.75 * self.maxFood):
            action_list = self.eatPrey(
                animal_sr
            )  #should be a list with coords and 1 or 2 depending on pred or prey eaten, or None if nothing was eaten
            if action_list:
                return action_list

        if self.currWater < (.75 * self.maxWater):
            action_list = self.waterReact(animal_sr)

            if action_list:
                return action_list
        

        if self.checkIsFertile():
            action_list = self.reproduce(animal_sr)

            if action_list:
                return action_list
                
            return action_list

        
        
        # no action taken, so animal just moves
        move_action = MoveAction()
        currLocation = (self.position_x, self.position_y)
        #self.random_move()

        invalid_locs = animal_sr.getNearbyPrey(
        ) + animal_sr.getNearbyPredators() + animal_sr.getNearbyWater()
        self.random_move(invalid_locs)

        
        endLocation = (self.position_x, self.position_y)
        if endLocation not in invalid_locs:
          move_action.setstartLocation(currLocation)
          move_action.setendLocation(endLocation)
          current_action_list.append(move_action)

        #send out desired action to sim
        return current_action_list
