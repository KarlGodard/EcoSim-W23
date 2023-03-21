from Map import Map
from Animal import Animal
from Predator import Predator
from Prey import Prey
from SensoryRange import SensoryRange
import random
from IPython.display import clear_output
import matplotlib.pyplot as plt
import numpy as np
from Visualization import Visualization
import time
import pygame
# animal movement showing up on the grid
# animal interaction
# boundaries for map and animal movement
# generate map


class Simulation():

    def __init__(self,
                 mapSize=(300, 200),
                 startingTemp=70,
                 rateOfTempChange=1,
                 numStartingAnimals=50,
                 startingAnimalDistribution=[0.5, 0.5],
                 simulationLength=100):

        self.mapSize = mapSize
        # self.percentWaterTiles = percentWaterTiles
        self.startingTemp = startingTemp
        self.rateOfTempChange = rateOfTempChange
        self.numStartingAnimals = numStartingAnimals
        self.startingAnimalDistribution = startingAnimalDistribution
        self.simulationLength = simulationLength
        # self.visualization = Visualization()
        self.map = Map(self.mapSize, self.startingTemp, self.rateOfTempChange,
                       self.startingAnimalDistribution)

        self.iteration = 0

        self.visualization = Visualization(self.mapSize)

    def simulationLoop(self, t):
        # Map.get_next_animal() -> either animal object or None
        
        animal = self.map.getNextAnimal()
        while animal != None:
            animal_sr = SensoryRange()

            #get data surrounding animal
            nearby_plants = self.map.getNearbyPlants(animal)
            animal_sr.setNearbyPlants(nearby_plants)
            nearby_predators = self.map.getNearbyPredators(animal)
            nearby_prey = self.map.getNearbyPrey(animal)
            animal_sr.setNearbyPredators(nearby_predators)
            animal_sr.setNearbyPrey(nearby_prey)
            nearby_tiles = self.map.getNearbyWater(animal)

            animal_sr.setNearbyWater(nearby_tiles)
            temp = self.map.getTemp()
            animal_sr.setTemp(temp)

            #pass data to animal and receive actions
            animal_obj = self.map.convertIDtoAnimal(animal)
            if animal_obj.is_prey:
                actions = animal_obj.preyReact(animal_sr)
            else:
                actions = animal_obj.predReact(animal_sr)

            #carry out actions

            survives = True
            for action in actions:

                if (action.type == "eat"):
                    if action.foodType == "animal":

                        id = self.map.map[action.foodLocation[1]][
                            action.foodLocation[0]].animal_id
                        print("Animal " + str(id) + " eaten by " + str(animal))
                        if id == animal:
                            print("Error: animal eats itself")
                        self.map.delete_animal(id)
                    elif action.foodType == "plant":
                        self.map.delete_plant(action.foodLocation)

                elif (action.type == "move"):
                    if (self.map.locToTile(action.endLocation).has_prey or self.map.locToTile(action.endLocation).has_pred):
                        continue
                    
                    self.map.move_animal(animal, action.endLocation)
                    #position x, position y

                elif (action.type == "reproduce"):
                    self.map.create_animal(animal, action.endLocation)

                elif (action.type == "drink"):
                    pass  #no action needed
                elif (action.type == "die"):
                    print("Animal " + str(animal) + " died")
                    self.map.delete_animal(animal)
                    survives = False
                    break  #remove from map, delete animal
                else:
                    print("Invalid action type")
                    exit(1)

            if survives:
                self.map.next_order.append(animal)

            #end of animal loop
            animal = self.map.getNextAnimal()

        #Food
        self.map.generate_plants()

        #Other Miscellanous
        #self.map.environmental_change()

    def visualize(self):
        animalMap = []
        for row in self.map.map:
            rowData = []
            for tile in row:
                if tile.is_prey():
                    rowData.append("prey")
                elif tile.is_pred():
                    rowData.append("pred")
                elif tile.has_plant:
                    rowData.append("plant")
                elif tile.has_water:
                    rowData.append("water")
                else:
                    rowData.append("grass")

            animalMap.append(rowData)

        ## update visualization here
        self.visualization.update_map(animalMap)
        self.map.predator_count.append(self.map.getNumPredators())
        self.map.prey_count.append(self.map.getNumPrey())

        ## Time before switching screens
        #pygame.time.wait(500)

    def run_simulation(self):

        num_predators = [self.map.getNumPredators()]
        num_prey = [self.map.getNumPrey()]
        time_graph = [0]

        self.visualize()

        t = 0
        while t < self.simulationLength:
            self.simulationLoop(t)
            t += 1
            # Visualize Current Simulation State
            time_graph.append(t)
            num_predators.append(self.map.getNumPredators())
            num_prey.append(self.map.getNumPrey())

            self.visualize()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        self.map.create_graph()
