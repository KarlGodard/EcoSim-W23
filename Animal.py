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

    #later: add animal species, and types of prey // possibly using inheritance

    # make sensory range a class variable, pass it through the action function

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

        #only two animal type so we got rid of speed
        #x_mag = random.randint(0, self.speed)
        #y_mag = self.speed - x_mag
        #dx = x_dir * x_mag
        #dy = y_dir * y_mag
        return self.move(dx, dy, self.xmax, self.ymax)

    def set_random_location(self):
        x_loc = random.randint(0, self.xmax - 1)
        y_loc = random.randint(0, self.ymax - 1)
        self.position_x = x_loc
        self.position_y = y_loc

    def eatPlant(self, surroundings):
        # nearbyFood is coordinate of nearest plant
        nearbyFood = surroundings.getNearbyFood()
        if nearbyFood == None:
            # returns None if cannot eat plant
            return None
        else:
            return [nearbyFood[0], 2]
            """
            canEat = True
            preds = surroundings.getNearbyPredators
            preys = surroundings.getNearbyPrey
            for i in range(len(preds)):
                predX = preds[i][0]
                predY = preds[i][1]
                if nearbyFood[0] == predX and nearbyFood[-1] == predY:
                    canEat = False
                    break
            for i in range(len(preys)):
                preyX = preys[i].position_x
                preyY = preys[i].position_y
                if nearbyFood[0] == preyX and nearbyFood[-1] == preyY:
                    canEat = False
                    break

            if canEat is True:
                # there is plant to eat, returns the coords
                eatReact = []
                self.currFood += (0.15 * self.maxFood)
                self.position_x = nearbyFood[0]
                self.position_y = nearbyFood[-1]
                eatReact.append(nearbyFood)
                eatReact.append(2)
                #returns the a list with [coords of plant, 2]
                # 2 means it's eating a plant
                return eatReact
            else:
                return None
            """

    def waterReact(self, surroundings):
        # check what's around
        canDrink = False
        nearbyWater = surroundings.getNearbyWater()
        print(nearbyWater)
        if nearbyWater == []:
            return None
        else:
            print("Drinking")
            canDrink = True

            # preds = surroundings.getNearbyPredators
            # preys = surroundings.getNearbyPrey
            # for i in len(preds):
            #     predX = preds[i].position_x
            #     predY = preds[i].position_y
            #     if nearbyWater[0] == predX and nearbyWater[-1] == predY:
            #         canDrink = False
            #         break
            # for i in len(preys):
            #     preyX = preys[i].position_x
            #     preyY = preys[i].position_y
            #     if nearbyWater[0] == preyX and nearbyWater[-1] == preyY:
            #         canDrink = False
            #         break

        if canDrink is True:
            # there is water to drink
            self.currWater += (0.25 * self.maxWater)
            self.position_x = nearbyWater[0][0]
            self.position_y = nearbyWater[0][1]
            # returns the coordinate of the water
            return nearbyWater
            # water level below 75% of maxWater, drink and level goes up 25%
        else:
            return None

    def tempReact(self, surroundings):
        temp = surroundings.getTemp()
        # temp too high or low, animal dies
        if temp > 110 or temp < 0:
            rand = randrange(0, 1600)
            # so some animals die
        if (rand < min((temp - 110)**2, (temp)**2)):
            self.kill(self)

    def checkIsFertile(self):
        if self.food < (self.maxFood * 0.75) or self.water < (
                self.maxWater * 0.75):  #changed from 0.5
            self.isFertile = 0
        else:
            self.isFertile = 1
            # do age later


# gender, age, time since last birth
# maybe: offspring cap
# check isFertile
# age and time since last birth
# will update with time/age once time is established
# if isFertile and surrounding animal is opp sex then reproduce


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
        self.isPrey = 0
        self.isFertile = 0
        self.animalId = animalID
        if position_x == None:
            self.set_random_location()
        else:
            self.position_x = position_x
            self.position_y = position_y
        self.alive = 1
        self.xmax = xmax
        self.ymax = ymax

    def eatPrey(self, surroundings):
        # a list of preys
        nearbyPrey = surroundings.getNearbyPrey()
        if nearbyPrey:  # list is not empty
            eatReact = []
            preyEaten = nearbyPrey[0]
            self.currFood += (0.20 * self.maxFood)
            xCoord = preyEaten[0]
            yCoord = preyEaten[1]
            coords = (xCoord, yCoord)  #make tuple of the coords
            eatReact.append(coords)
            eatReact.append(1)
            # returns a list of [(xCoord, yCoord), 1]
            # 1 means it's eating a prey
            return eatReact
            """
            eatReact = []
            canEat = False
            preyIndex = 0
            nearbyPreds = surroundings.getNearbyPredators()
            
            for i in range(len(nearbyPrey)):
                madeIt = True
                preyX = nearbyPrey[i][0]
                preyY = nearbyPrey[i][1]
                for j in range(len(nearbyPreds)):
                    currX = nearbyPreds[j][0]
                    currY = nearbyPreds[j][1]
                    if preyX == currX and preyY == currY:
                        madeIt = False
                        break
                if madeIt is True:
                    canEat = True
                    preyIndex = i
                    break
            
            if canEat is False:
                self.eatPlant(surroundings)
            else:
                preyEaten = nearbyPrey[preyIndex]
                self.currFood += (0.20 * self.maxFood)
                xCoord = preyEaten[0]
                yCoord = preyEaten[1]
                coords = (xCoord, yCoord) #make tuple of the coords
                eatReact.append(coords)
                eatReact.append(1)
                # returns a list of [(xCoord, yCoord), 1]
                # 1 means it's eating a prey
                return eatReact
                """
        else:
            # no prey available, try eating a plant
            return self.eatPlant(surroundings)
            # if not eating, will return None

    def reproductionPredReact(self, surroundings):
        if not self.checkIsFertile:
            # if it's not fertile, it will return
            return None

        nearbyPreds = surroundings.getNearbyPredators
        for i in nearbyPreds:
            if (i.is_female != self.is_female) and (i.checkIsFertile):
                # can mate: opposite genders, both fertile, other didnt move
                # neither animal moves
                return True
            else:
                # mating conditions do not work, return False
                return False

    def predReact(self, animal_sr):
        # make use_resource function: use food and water (small amts) for any action; call it here

        # food and water will decrease by 10% no matter what
        self.currWater -= self.maxWater * 0.1
        #self.currFood -= self.maxFood * 0.1
        current_action_list = []

        self.check_state()  #check if it is alive
        #self.tempReact()
        if self.alive == 0:
            die_action = DieAction()
            current_action_list.append(die_action)
            return current_action_list
            # tell sim to delete self
        """
        if self.currFood < (0.75 * self.maxFood):
            eat = self.eatPrey(animal_sr) #should be a list with coords and 1 or 2 depending on pred or prey eaten, or None if nothing was eaten
            if (eat is not None):
                # was able to eat
                # tell sim to delete prey, move pred to prey tile
                eat_action = EatAction()
                eat_action.setFoodLocation(eat[0])
                if eat[1] == 1:
                    eat_action.setFoodType("prey")
                else:
                    eat_action.setFoodType("plant")
                current_action_list.append(eat_action)

                move_action = MoveAction()
                currLocation = (self.position_x, self.position_y)
                move_action.setstartLocation(currLocation)
                move_action.setendLocation(eat[0])
                current_action_list.append(move_action)
                return current_action_list
        """
        if self.currWater < (.75 * self.maxWater):
            coords = self.waterReact(animal_sr)
            if (coords is not None):
                # was able to drink
                drink_action = DrinkAction()
                current_action_list.append(drink_action)

                move_action = MoveAction()
                currLocation = (self.position_x, self.position_y)
                move_action.setstartLocation(self, currLocation)
                move_action.setendLocation(self, coords)
                current_action_list.append(move_action)
                return current_action_list
        """
        if self.reproductionReact() == True:
            # animal is reproducing
            reproduce_action = ReproduceAction
            reproduce_action.setAnimalType(self, "pred")
            current_action_list.append(reproduce_action)
            return current_action_list

        else:
        """
        # no action taken, so animal just moves
        move_action = MoveAction()
        currLocation = (self.position_x, self.position_y)
        #self.random_move()

        invalid_locs = animal_sr.getNearbyPrey(
        ) + animal_sr.getNearbyPredators() + animal_sr.getNearbyWater()
        self.random_move(invalid_locs)

        endLocation = (self.position_x, self.position_y)
        move_action.setstartLocation(currLocation)
        move_action.setendLocation(endLocation)
        current_action_list.append(move_action)

        #send out desired action to sim
        return current_action_list


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
        self.isPrey = 1
        self.isFertile = 0
        self.animalID = animalID
        if position_x == None:
            self.set_random_location()
        else:
            self.position_x = position_x
            self.position_y = position_y
        self.alive = 1
        self.xmax = xmax
        self.ymax = ymax

    def reproductionPreyReact(self, surroundings):
        if not self.checkIsFertile:
            # if it's not fertile, it will return
            return None
        nearbyPrey = surroundings.getNearbyPrey()

        for i in nearbyPrey:
            # can mate
            if (i.is_female != self.is_female) and (i.checkIsFertile):
                return True
            else:
                #cannot mate
                return None

    def preyReact(self, animal_sr):
        # make use_resource function: use food and water (small amts) for any action; call it here

        self.currWater -= self.maxWater * 0.1
        #self.currFood -= self.maxFood * 0.1
        current_action_list = []

        self.check_state()  #check if it is alive
        #self.tempReact(animal_sr)
        if self.alive == 0:
            #del(self) #don't need this anymore
            die_action = DieAction()
            current_action_list.append(die_action)
            return current_action_list
            # tell sim to delete self
        """
        if self.currFood < (0.75 * self.maxFood):
            eat = self.eatPlant(animal_sr) #should be a list with coords of plant and 2, or None if nothing was eaten
            if (eat is not None):
                # was able to eat
                # tell sim to delete prey, move pred to prey tile
                eat_action = EatAction()
                eat_action.setFoodLocation(self, eat[0])
                eat_action.setFoodType(self, "plant")
                current_action_list.append(eat_action)

                move_action = MoveAction()
                currLocation = (self.position_x, self.position_y)
                move_action.setstartLocation(self, currLocation)
                move_action.setendLocation(self, eat[0])
                current_action_list.append(move_action)
                return current_action_list
        
        """
        if self.currWater < (.75 * self.maxWater):
            coords = self.waterReact(animal_sr)
            if (coords is not None):
                # was able to drink
                drink_action = DrinkAction()
                current_action_list.append(drink_action)

                move_action = MoveAction()
                currLocation = (self.position_x, self.position_y)
                move_action.setstartLocation(self, currLocation)
                move_action.setendLocation(self, coords)
                current_action_list.append(move_action)
                return current_action_list
        """
        elif self.reproductionPreyReact(animal_sr) == True:
            # check if can reproduce, will be true if yes
            reproduce_action = ReproduceAction
            reproduce_action.setAnimalType(self, "prey")
            current_action_list.append(reproduce_action)
            return current_action_list

        """

        # if nothing happens, will randomly move

        move_action = MoveAction()
        currLocation = (self.position_x, self.position_y)

        invalid_locs = animal_sr.getNearbyPrey(
        ) + animal_sr.getNearbyPredators()

        self.random_move(invalid_locs)

        endLocation = (self.position_x, self.position_y)
        move_action.setstartLocation(currLocation)
        move_action.setendLocation(endLocation)
        current_action_list.append(move_action)

        return current_action_list
