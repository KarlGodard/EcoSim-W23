# EcoSim Tutorial (work in progress)

### Quickstart
To run the simulation:

```
python3 main.py
```



### Simulation Parameters:

In the main.py file, there are many parameters you can change to modify the simulation.

**Simulation Params**
* simulationLength - the number of iterations the simulation runs for
* simulationSpeed - delay in ms added between each frame in the simulation


**Map Params**
* sizeX, sizeY - size of simulation grid
* percentWaterCoverage
* numStartingPredators, numStartingPrey
* temp

**Predator/Prey Params**
* maxFood
* naxWater
* minReproductiveAge
* reproductiveDelay
* waterSearchRadius
* reproductiveSearchRadius
* hungerIncreasePercentage/hungerDecreasePercentage
* thirstIncreasePercentage/
* minReproductiveHunger
* minReproductiveThirst



### Key Objects in EcoSim

* Simulation - the main control center of the simulation, coordinates information between the animals, the map, and the vizualization

* Map - maintains the current state of the simulation, holds a grid (2-dimensional array) of Tile objects

* Tile - one discrete unit of space in the simulation, stores the presence of animals, food, and water at that location

* Animal - the parent class of the Predator and Prey classes, stores common properties of the two

* Predator - animal at the top of the food chain, eats Prey

* Prey - animal at the middle of the food chain, eaten by Predators and eats plants

* SensoryRange - an object that stores all the sensory information available to an animal during its decision making process

* Action - holds information about the type of action that an animal wishes to carry out on its turn

* AnimalParams - a data structure that holds modifiable parameters for animals




### Getting oriented with the simulation

First, check out the file Simulation.py

In this file you'll find a class with three functions (in addition to the constructor), simulationLoop, visualize, and runSimulation.

runSimulation is the function that is called from main to begin the simulation. Within this function is a while loop that controls the length of the simulation. Variable t (time) starts at 0 and is incremented at each iteration of the simulation until the simulation reaches the duration specified. During each iteration of this loop, one iteration of the simulation is run (with simulationLoop()), and the current state of the simulation is animated (with visualize()).

In the simulationLoop function, there is a while loop that iterates through all the animals currently alive in the simulation. For each animal, data pertaining to that animals surroundings are collected into a SensoryRange object, and that information is then passed to the animal, which decides which action it wishes to take. 

After deciding which actions it wishes to take, the animal communicates this information in the form of an Action object. The simulationLoop function then updates the simulation based on these actions (remove animals that have been eaten, move animals that have been moved, etc).

The simulationLoop function then moves on to the next animal in the queue and repeats the above actions. 

Once all animals have been given the opportunity to act, new plants are generated randomly onto the map (with generatePlants())

Lastly, the visualize() function passes data about the state of the map to the Visualization class, which then proceeds with drawing that information to the user's screen. 




Now, look to Animal class and either the Predator or Prey class.

Next, review the Map class

Finally, look to the Visualization class


### Common confusion points


Animal queueing (current_order vs next_order):






