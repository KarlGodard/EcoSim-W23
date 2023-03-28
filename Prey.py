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
                 position_x=None,
                 position_y=None,
                 animalID=None):
        self.currFood = random.randint(37, 75)
        self.maxFood = 75
        self.currWater = 75
        self.maxWater = 75
        self.is_female = random.choice([0, 1])
        self.is_prey = 1
        self.is_fertile = 0
        self.animalID = animalID
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
        

    def reproduce(self, surroundings):
        nearbyMates = surroundings.getNearbyMates()
        for i in nearbyMates:
            
            # can mate: opposite genders, both fertile, other didnt move
            # neither animal moves
            # animal is reproducing
            action_list = []
            reproduce_action = ReproduceAction()
            reproduce_action.setAnimalType(self, "pred")

            open_tiles = self.getOpenTiles(surroundings)
            reproduce_action.setendLocation(random.choice(open_tiles))
            reproduce_action.setPartnerLocation(i)
          
            action_list.append(reproduce_action)

            
            self.reprDelay = 0;
            return action_list
            

    def preyReact(self, animal_sr):
        #print(self.currFood)
        # make use_resource function: use food and water (small amts) for any action; call it here

        self.currWater -= self.maxWater * 0.05
        self.currFood -= self.maxFood * 0.05
        current_action_list = []

        self.check_state()  #check if it is alive
        #self.tempReact(animal_sr)
        if self.alive == 0:
            #del(self) #don't need this anymore
            die_action = DieAction()
            current_action_list.append(die_action)
            return current_action_list
            # tell sim to delete self

        if self.currFood < (0.75 * self.maxFood):
            action_list = self.eatPlant(
                animal_sr
            )  #should be a list with coords of plant and 2, or None if nothing was eaten

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
                
            

        # if nothing happens, will randomly move

        move_action = MoveAction()
        currLocation = (self.position_x, self.position_y)

        invalid_locs = animal_sr.getNearbyPrey(
        ) + animal_sr.getNearbyPredators() + animal_sr.getNearbyWater(
        ) + animal_sr.getNearbyPlants()

        self.random_move(invalid_locs)

        endLocation = (self.position_x, self.position_y)
        if endLocation not in invalid_locs:
            move_action.setstartLocation(currLocation)
            move_action.setendLocation(endLocation)
            current_action_list.append(move_action)

        return current_action_list
