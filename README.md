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
* percentWaterCoverage - controls percentage of water tiles on the map (functionality not yet implemented)
* numStartingPredators, numStartingPrey - controls size of intitial population of predators and prey
* temp - global map temperature, intended to affect plant growth (functionality not yet implemented)

**Predator/Prey Params**
* maxFood - maximum food level for animal
* maxWater - maximum water level for animal
* minReproductiveAge - minimum number of iterations after an animal is born before it can reproduce
* reproductiveDelay - minimum number of iterations before an animal can reproduce again
* waterSearchRadius - distance in tiles in which an animal can sense water
* reproductiveSearchRadius - distance in tiles in which an animal can detect viable mates
* hungerIncreasePercentage/hungerDecreasePercentage - rate at which animal hunger increases (note: increase in hunger = decrease in food level)
* thirstIncreasePercentage/thirstDecreasePercentage - rate at which animal thirst increases (note: increase in thirst = decrease in water level)
* minReproductiveHunger - minimum food level at which an animal can reproduce
* minReproductiveThirst - minimum water level at which an animal can reproduce



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

#### Simulation.py

In this file you'll find a class with three functions (in addition to the constructor), simulationLoop, visualize, and runSimulation.

runSimulation is the function that is called from main to begin the simulation. Within this function is a while loop that controls the length of the simulation. Variable t (time) starts at 0 and is incremented at each iteration of the simulation until the simulation reaches the duration specified. During each iteration of this loop, one iteration of the simulation is run (with simulationLoop()), and the current state of the simulation is animated (with visualize()).

In the simulationLoop function, there is a while loop that iterates through all the animals currently alive in the simulation. For each animal, data pertaining to that animals surroundings are collected into a SensoryRange object, and that information is then passed to the animal, which decides which action it wishes to take. 

After deciding which actions it wishes to take, the animal communicates this information in the form of an Action object. The simulationLoop function then updates the simulation based on these actions (remove animals that have been eaten, move animals that have been moved, etc).

The simulationLoop function then moves on to the next animal in the queue and repeats the above actions. 

Once all animals have been given the opportunity to act, new plants are generated randomly onto the map (with generatePlants())

Lastly, the visualize() function passes data about the state of the map to the Visualization class, which then proceeds with drawing that information to the user's screen. 


#### Animals

Now, look to Animal, Predator and Prey classes. The Animal class is the parent class of Predator and Prey (for more on inheritence, see https://www.geeksforgeeks.org/inheritance-in-python/)

Scroll first through the Animal class to view the various functions that describe functionality shared between predators and prey. Then pick either the Predator or Prey class and scroll down to view the PredRead or PreyReact function. In this function you'll find the logic that dictates how an animal behaves at each step of the information.

Each function takes a parameter called animalSr, which contains information about the map contained within that animal's sensory range. In the first few lines, you can see that the animal's current water and food levels decrease at the start of its turn. The function then progresses through a series of checks to determine what action the animal should take; if the animal is hungry and food is available, the animal should prioritize eating. If this is not the case, we then check if the animal is thirsty and water is available. We proceed likewise through searching for viable mates, and if none of the above options are available the animal picks a random direction to move in. 

Regardless of what action the animal decides to make, it stores the information about its decision in an Action object, which it passes through the return statement back to Simulation.py, which handles executing the consequences of that action (deleting food off the map, spawning new animal, etc).

### Map

The map at its core is a 2-dimensional array (list) of Tile objects. Whenever we want to update something on the map, we first index into the appropriate place in the map and then update the stored information at that tile.

Note that map is indexed first with the y-coordinate followed by the x-coordinate. For example, to access the tile at (x,y), we use

```
self.map[y][x]
```

For the purposes of tracking animals across the map, each animal is given a unique identifier, its animalID. The first animalID assigned is 0, and the next animalID is incremented every time a new animal is created. With this unique identifier, we can now have a dictionary that maps each animalID to its underlying animal object, and this animalID can be used to easily reference that object at all other places throughout the map class. 

The map file contains a number of other functions that aid with maintaining the proper state of the map. These include functions for:
* Adding/deleting animals
* Moving animals
* Generating water on the map
* Retrieving information about the animals/plants within a certain region of the map

The Map class also importantly maintains information about the order in which animals are set to act. It does this with two separate arrays, currentOrder and nextOrder. To picture why two separate arrays are useful, imagine first using only one array. In this array we would have a list of animals, as well as a counter that keeps of where in the array the currently acting animal is. Everytime an animal is born or dies, we have to add onto or remove from this array, meaning that an animal could end at a totally different index in the array from where it started. And instead of simply incrementing the counter each turn, an animal could die on its own turn, meaning the animal would be removed from the list and the counter should stay in place. 

To make simplify this issue, we maintain two separate lists, one for the current iteration of the simulation and one for the next iteration of the simulation. At the start of an iteration, the currentOrder list contains the animalId's of all animals in the simulation. We then progress through currentOrder one animal at a time. If the animal lives, its appended to the nextOrder list. When an animal is born, it is added to the nextOrder list. When an animal that has already acted is killed, it is removed from nextOrder. When an animal that has not yet acted is killed, it is removed from currentOrder so that its not given the chance to act. When the current animal is killed, the counter simply is incremented to the next animal in current order, and the killed animal is not added to nextOrder. In this way, the current state of all the animals alive in the simulation is more easily maintained. 

### Common confusion points


Animal queueing (current_order vs next_order):






