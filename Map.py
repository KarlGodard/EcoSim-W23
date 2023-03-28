from Tile import Tile
from Animal import Animal
from Predator import Predator
from Prey import Prey
from Visualization import Visualization
import random
import math
import numpy as np
import copy
import matplotlib.pyplot as plt

# different dictionaries for each variable and then
# we pass in a coordinate to determine what is there
# coordinates will list the characteristics of what
# is there


class Map:
    #called in Simulation
    def __init__(self, mapSize, startingTemp, rateOfTempChange,
                 startingAnimalDistribution):
        self.mapSize = mapSize  #tuple
        self.size_x = mapSize[0]
        self.size_y = mapSize[1]
        self.startTemp = startingTemp
        self.currTemp = startingTemp
        self.numAnimals = 0
        self.numPredators = 0
        self.numPrey = 0
        self.animal_id = 0
        self.map = [[Tile() for i in range(self.size_x)]
                    for j in range(self.size_y)]
        self.river_maker()
        self.pond_maker()
        self.pond_maker()
        self.pond_maker()

        #self.create_graph()

        self.IDtoAnimal = {}
        self.IDtoLoc = {}  # dictionary from animal IDs to locations
        self.current_order = [
        ]  # list of animal ID's: specifies order of action
        self.current_index = 0
        self.next_order = []
        self.predator_count = []
        self.prey_count = []
        self.predator_count.append(self.getNumPredators())
        self.prey_count.append(self.getNumPrey())

        self.initialize_animals()
        self.generate_initial_plants()

    def convertIDtoLoc(self, animal_id):
        return self.IDtoLoc[animal_id]

    def convertIDtoTile(self, animal_id):
        animal_loc = self.convertIDtoLoc(animal_id)
        return self.map[animal_loc[1]][animal_loc[0]]

    def convertIDtoAnimal(self, animal_id):
        return self.IDtoAnimal[animal_id]

    def locToTile(self, loc):
        return self.map[loc[1]][loc[0]]

    def locToAnimal(self, loc):
        return self.IDtoAnimal[self.locToTile(loc).animal_id]

    # function that makes a sine function that we
    # can pass back to tile to make curvy rivers
    def river_maker(self):
        coef = [random.random() for i in range(4)]
        if (coef[3] > 0.75):
            coef[3] = coef[3] - 0.5
        if (coef[3] < 0.25):
            coef[3] = coef[3] + 0.5
        if (coef[0] < 0.5):
            coef[0] = coef[0] + 0.5
        for i in range(self.size_y):
            #j = 0
            #j = random.choice(range(self.size_x))
            j = int(3 * coef[0] * (math.sin(coef[1] * i + coef[2])) +
                    coef[3] * self.size_x)
            if (j >= 0 and j < self.size_x):
                self.map[i][j].set_water()

        #return

    def pond_maker(self):
        # generate random spot for pond
        x_cord = int(random.randint(0, self.size_x - 8))
        y_cord = int(random.randint(0, self.size_y - 8))

        # size - height (5-8), width (5-8)
        height = int(random.randint(5, 8))
        width = int(random.randint(5, 8))

        for i in range(width):
            # generating extra dimensions so pond isn't square
            shift = int(random.randint(-2, 2))
            for j in range(height):
                if (y_cord + i < self.size_y
                        and x_cord + j + shift < self.size_x):
                    self.map[y_cord + i][x_cord + j + shift].set_water()

    def generate_initial_plants(self):
        self.generate_plants(.85)
        return

    def generate_plants(self, threshhold=.99):
        # if t = 0, use 0.90 for p threshoold. otherwise use 0.99
        for i in range(self.size_x):
            for j in range(self.size_y):
                if (self.currTemp >= 40 and self.currTemp <= 80) and (
                        self.map[j][i].get_terrain() == "E"):
                    #gets random number between 0 and 1
                    p = random.random()

                    if p > threshhold:
                        self.map[j][i].set_plant()

        return

    def delete_plant(self, loc):
        tile = self.locToTile(loc)
        #print("Plant deleted at ", loc)
        tile.has_plant = False
        tile.terrain = "E"
        return

    def initialize_animals(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                if self.map[j][i].has_water:
                    continue
                p1 = .1
                p2 = 0.05
                newpredator = (np.random.rand() < p1)  #bernoulli(p1)
                newprey = (np.random.rand() < p2)  #bernoulli(p2)
                location = (i, j)
                if (newpredator == 1):
                    newprey = False
                    self.create_predator(location)
                if (newprey == 1):
                    self.create_prey(location)
        self.current_order = copy.deepcopy(self.next_order)
        self.next_order = []
        return

    def create_predator(self, loc):
        # loc is pass in as "x, y"
        x = loc[0]
        y = loc[1]
        newPred = Predator(self.size_x, self.size_y, x, y, self.animal_id)
        self.IDtoAnimal[self.animal_id] = newPred
        self.IDtoLoc[self.animal_id] = loc
        self.next_order.append(self.animal_id)
        self.map[y][x].set_predator()

        #set animal_id
        self.map[y][x].animal_id = self.animal_id

        self.animal_id = self.animal_id + 1
        self.numAnimals = self.numAnimals + 1
        self.numPredators += 1

        return

    def create_prey(self, loc):
        x = loc[0]
        y = loc[1]

        newPrey = Prey(self.size_x, self.size_y, x, y, self.animal_id)
        self.IDtoLoc[self.animal_id] = loc
        self.IDtoAnimal[self.animal_id] = newPrey
        self.next_order.append(self.animal_id)
        self.map[y][x].set_prey()

        #set animal_id
        self.map[y][x].animal_id = self.animal_id

        self.animal_id = self.animal_id + 1
        self.numAnimals = self.numAnimals + 1
        self.numPrey += 1
        return

    def move_animal(self, animal_id, loc):
        animal = self.convertIDtoAnimal(animal_id)
        tile = self.convertIDtoTile(animal_id)
        newTile = self.locToTile(loc)
        if loc == self.IDtoLoc[animal_id]:
             return

        #clear old tile
        tile.animal = False
        tile.has_pred = False
        tile.has_prey = False
        tile.animal_id = -1
        tile.occupied = 0

        #update new tile'
        if (newTile.has_pred != 0 or newTile.has_prey != 0 or newTile.has_water != 0):
            #exit(1)
            print('Illegal action: movement onto occupied tile')

        newTile.animal_id = animal_id
        if animal.is_prey:
            newTile.has_prey = True
        else:
            newTile.has_pred = True

        newTile.occupied = True
        self.IDtoLoc[animal_id] = loc
        return

    def delete_animal(self, animal_id):
        tile = self.convertIDtoTile(animal_id)
        tile.has_pred = 0
        tile.has_prey = 0
        tile.occupied = False
        tile.animal_id = -1
        self.numAnimals = self.numAnimals - 1
      
        #print("Deleting animal " + str(animal_id))
        #print(self.current_order)
        if animal_id in self.current_order and self.current_order.index(animal_id) >= self.current_index:
           self.current_order.remove(animal_id)
        #print(self.current_order)

        #print(self.next_order)
        assert (len(self.next_order) == len(set(self.next_order)))
        if animal_id in self.next_order:
            self.next_order.remove(animal_id)
        #print(self.next_order)  

        if self.convertIDtoAnimal(animal_id).is_prey:
            self.numPrey -= 1
        else:
            self.numPredators -= 1

        self.convertIDtoAnimal(animal_id).alive = False

        self.IDtoAnimal.pop(animal_id)
        self.IDtoLoc.pop(animal_id)

        return

    def getNearbyPlants(self, animalID):
        loc = self.convertIDtoLoc(animalID)
        locs_with_food = []
        # search distance
        search_dist = 2
        min_x = max(0, loc[0] - search_dist)
        max_x = min(self.size_x, loc[0] + search_dist + 1)
        min_y = max(0, loc[1] - search_dist)
        max_y = min(self.size_y, loc[1] + search_dist + 1)
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                if self.locToTile((i, j)).has_plant == True:
                    locs_with_food.append((i, j))

        return locs_with_food

    def getNearbyPredators(self, animalID):
        loc = self.convertIDtoLoc(animalID)
        locs_with_predators = []

        search_dist = 2
        min_x = max(0, loc[0] - search_dist)
        max_x = min(self.size_x, loc[0] + search_dist + 1)
        min_y = max(0, loc[1] - search_dist)
        max_y = min(self.size_y, loc[1] + search_dist + 1)
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                if self.locToTile((i, j)).has_pred:
                    locs_with_predators.append((i, j))

        return locs_with_predators

    def getNearbyPrey(self, animalID):
        loc = self.convertIDtoLoc(animalID)
        locs_with_prey = []
        
        search_dist = 2
        min_x = max(0, loc[0] - search_dist)
        max_x = min(self.size_x, loc[0] + search_dist + 1)
        min_y = max(0, loc[1] - search_dist)
        max_y = min(self.size_y, loc[1] + search_dist + 1)
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                if self.locToTile((i, j)).has_prey:
                    locs_with_prey.append((i, j))

        return locs_with_prey

    def getNearbyWater(self, animalID):
        loc = self.convertIDtoLoc(animalID)
        locs_with_water = []
        # search distance
        search_dist = 2
        min_x = max(0, loc[0] - search_dist)
        max_x = min(self.size_x, loc[0] + search_dist + 1)
        min_y = max(0, loc[1] - search_dist)
        max_y = min(self.size_y, loc[1] + search_dist + 1)
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                if self.locToTile((i, j)).has_water:
                    locs_with_water.append((i, j))

        return locs_with_water
    def getViableMates(self, animal_id):
        animal = self.IDtoAnimal[animal_id]
        if not animal.checkIsFertile():
            return []
        loc = self.convertIDtoLoc(animal_id)
        locs_with_mate = []
        # search distance
        search_dist = 2
        min_x = max(0, loc[0] - search_dist)
        max_x = min(self.size_x, loc[0] + search_dist + 1)
        min_y = max(0, loc[1] - search_dist)
        max_y = min(self.size_y, loc[1] + search_dist + 1)
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                if self.map[j][i].is_animal():
                    other = self.IDtoAnimal[self.map[j][i].animal_id]
                    if other.checkIsFertile() and (other.isPrey == animal.isPrey) and other.is_female != animal.is_female:
                        locs_with_mate.append((i, j))
        return locs_with_mate
      
    def getTemp(self):
        return self.currTemp

    def getNextAnimal(self):
        if self.current_index >= len(self.current_order):
            self.current_index = 0
            self.current_order = copy.deepcopy(self.next_order)
            self.next_order = []
            return None

        self.current_index += 1
        return self.current_order[self.current_index - 1]

    def getNumAnimals(self):
        return self.numAnimals

    def getNumPredators(self):
        return self.numPredators

    def getNumPrey(self):
        return self.numPrey

    def create_graph(self):
        x_axis = []
        for i in range(0, 101):
            if (i % 2 == 0):
                x_axis.append(i)

        plt.plot(self.predator_count, label="Predator Count")
        plt.plot(self.prey_count, label="Prey Count")
        plt.legend(loc="upper left")
        plt.title("Population Distribution")
        plt.xlabel("Time")
        plt.ylabel("Population")
        #plt.ylim([0,100])
        plt.show()
