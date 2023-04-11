from Simulation import Simulation
from AnimalParams import SimulationParams, MapParams, AnimalParams

simulationParams = SimulationParams()
simulationParams.simulationLength = 1000
simulationParams.simulationSpeed = 0  #delay in ms

mapParams = MapParams()
mapParams.sizeX = 50
mapParams.sizeY = 30
mapParams.percentWaterCoverage = 30
mapParams.numStartingPredators = 0
mapParams.numStartingPrey = 120
mapParams.temp = 70

predatorParams = AnimalParams()
predatorParams.maxFood = 100
predatorParams.maxWater = 100
predatorParams.minReproductiveAge = 15
predatorParams.reproductiveDelay = 15
predatorParams.waterSearchRadius = 5
predatorParams.foodSearchRadius = 5
predatorParams.reproductiveSearchRadius = 30
predatorParams.hungerIncreasePercentage = 0.03
predatorParams.thirstIncreasePercentage = 0.03
predatorParams.hungerDecreasePercentage = 0.50
predatorParams.thirstDecreasePercentage = 0.50
predatorParams.minReproductiveHunger = .50
predatorParams.minReproductiveThirst = .50

preyParams = AnimalParams()
preyParams.maxFood = 100
preyParams.maxWater = 100
preyParams.minReproductiveAge = 10
preyParams.reproductiveDelay = 4
preyParams.waterSearchRadius = 15
preyParams.foodSearchRadius = 15
preyParams.reproductiveSearchRadius = 15
preyParams.predatorSearchRadius = 6
preyParams.hungerIncreasePercentage = 0.03
preyParams.thirstIncreasePercentage = 0.03
preyParams.hungerDecreasePercentage = 0.50
preyParams.thirstDecreasePercentage = 0.50
preyParams.minReproductiveHunger = 0.50
preyParams.minReproductiveThirst = 0.50

simulation = Simulation(simulationParams, mapParams, predatorParams,
                        preyParams)
simulation.runSimulation()
