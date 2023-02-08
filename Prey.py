import Animal

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
        
        # elif self.reproductionPreyReact(animal_sr) == True:
        #     # check if can reproduce, will be true if yes
        #     reproduce_action = ReproduceAction()
        #     reproduce_action.setAnimalType(self, "prey")
        #     current_action_list.append(reproduce_action)
        #     return current_action_list


        # if nothing happens, will randomly move

        move_action = MoveAction()
        currLocation = (self.position_x, self.position_y)

        invalid_locs = animal_sr.getNearbyPrey(
        ) + animal_sr.getNearbyPredators() + animal_sr.getNearbyWater(
        ) + animal_sr.getNearbyPlants()

        self.random_move(invalid_locs)

        endLocation = (self.position_x, self.position_y)
        move_action.setstartLocation(currLocation)
        move_action.setendLocation(endLocation)
        current_action_list.append(move_action)

        return current_action_list
