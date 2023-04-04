import pygame



class Visualization:

    def __init__(self, mapSize=(300, 200)):
        #load in file
        file = 'PixelArt/ecosimPixelArt.bmp'
        image = pygame.image.load(file)  #.convert_alpha()
        rect = image.get_rect()

        #create screen
        pygame.init()
        self.mapSize = mapSize
        screenSize = (16 * mapSize[0], 16 * mapSize[1])
        self.screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)

        #screen.blit(image, rect)
        pygame.display.update()

        self.tiles = []
        self.tileSize = (16, 16)

        #load tiles
        self.grass = pygame.Surface(self.tileSize)
        dest = ((1, 1), self.tileSize)
        self.grass.blit(image, (0, 0), dest)
        self.tiles.append(self.grass)

        self.dirt = pygame.Surface(self.tileSize)
        dest = ((18, 1), self.tileSize)
        self.dirt.blit(image, (0, 0), dest)
        self.tiles.append(self.dirt)

        self.water = pygame.Surface(self.tileSize)
        dest = ((35, 1), self.tileSize)
        self.water.blit(image, (0, 0), dest)
        self.tiles.append(self.water)

        self.prey = pygame.Surface(self.tileSize)
        dest = ((1, 18), self.tileSize)
        self.prey.blit(image, (0, 0), dest)
        self.tiles.append(self.prey)

        self.pred = pygame.Surface(self.tileSize)
        dest = ((18, 18), self.tileSize)
        self.pred.blit(image, (0, 0), dest)
        self.tiles.append(self.pred)

        self.plant = pygame.Surface(self.tileSize)
        dest = ((35, 18), self.tileSize)
        self.plant.blit(image, (0, 0), dest)
        self.tiles.append(self.plant)

        

        

        def convertToPixels(self, loc):
            if type(loc) == int:
                return loc * 16
            elif type(loc) == tuple:
                return (loc[0] * 16, loc[1] * 16)
            else:
                print(
                    "Convert to pixels should take either an integer or a tuple"
                )
                exit(1)

    # converts each tile to 16 each time

    def updateMap(self, map):
        #update map to show current reflection
        numRows = len(map)
        numCols = len(map[0])
        for row in range(numRows):
            for col in range(numCols):
                if (map[row][col] == "prey"):
                    self.screen.blit(self.prey, (col * 16, row * 16))
                elif (map[row][col] == "pred"):
                    self.screen.blit(self.pred, (col * 16, row * 16))
                #change self.water back to grass
                elif (map[row][col] == "grass"):
                    self.screen.blit(self.grass, (col * 16, row * 16))
                elif (map[row][col] == "water"):
                    self.screen.blit(self.water, (col * 16, row * 16))
                elif (map[row][col] == "plant"):
                    self.screen.blit(self.plant, (col * 16, row * 16))
                elif (map[row][col] == "dirt"):
                    self.screen.blit(self.dirt, (col * 16, row * 16))
        
        
        pygame.display.flip()




