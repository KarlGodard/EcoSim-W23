class Tile:

    def __init__(self, temp=60, terrain="E", water=False, plant=False):
        self.terrain = terrain
        self.occupied = False
        self.animal = False
        self.animal_id = -1
        # this is in Fahrenheit because we are Americans
        self.temp = temp
        self.has_water = water
        self.has_plant = plant
        self.has_pred = 0
        self.has_prey = 0

    def get_terrain(self):
        return self.terrain

    def get_organism(self):
        if self.has_pred:
            self.occupied = True
            return "P"
        elif self.has_prey:
            self.occupied = True
            return "p"
        elif self.has_plant:
            self.occupied = True
            return "F"
        else:
            self.occupied = False
            return "E"

    # this is a bigger function to just search what lives there

    def is_pred(self):
        return self.has_pred

    def is_prey(self):
        return self.has_prey

    def is_plant(self):
        return self.has_plant

    def is_water(self):
        return self.has_water

    def set_water(self):
        self.has_water = True
        self.occupied = True
        self.terrain = "W"
        return

    def set_plant(self):
        self.has_plant = True
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
        return self.has_pred or self.has_prey
