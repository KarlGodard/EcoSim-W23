
class Tile:
    def __init__(self, temp=60, terrain="E", water=False, food=False):
        self.terrain = terrain
        self.occupied = False
        self.animal = False
        # this is in Fahrenheit because we are Americans
        self.temp = temp
        self.has_water = water
        self.has_food = food
        self.has_pred = 0
        self.has_prey = 0
        self.totalFood = 0

    def get_terrain(self):
        return self.terrain

    def get_organism(self):
        if self.has_pred:
            self.occupied = True
            return "P"
        elif self.has_prey:
            self.occupied = True
            return "p"
        elif self.has_food:
            self.occupied = True
            return "F"
        else:
            self.occupied = False
            return "E"
    # this is a bigger function to just search what lives there

    def is_pred(self):
        if self.has_pred:
            return True
        else:
            return False

    def is_prey(self):
        if self.has_prey:
            return True
        else:
            return False

    def is_food(self):
        if self.has_food:
            return True
        else:
            return False

    def is_water(self):
        if self.has_water:
            return True
        else:
            return False

    def set_water(self):
        self.has_water = True
        self.occupied = True
        self.terrain = "W"
        return

    def set_food(self):
        self.has_food = True
        self.totalFood = self.totalFood + 1
        self.occupied = True
        self.terrain = "F"
        return

    def set_predator(self):
        self.animal = True
        self.has_pred = self.has_pred + 1
        self.occupied = True
        self.terrain = "P"
        return

    def set_prey(self):
        self.animal = True
        self.has_prey = self.has_prey + 1
        self.occupied = True
        self.terrain = "p"
        return

    def is_animal(self):
        if self.is_predator == True:
            return True
        elif self.is_prey == True:
            return True
        else: return False

