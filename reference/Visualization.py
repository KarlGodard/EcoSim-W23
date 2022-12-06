import pygame
 
from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
 
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100
 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


##Making each tileset into a file

file = 'ecosim pixel art.bmp'
image = pygame.image.load(file)
print(image)
rect = image.get_rect()

tileset = pygame.image.load("PixelArt/ecosimPixelArt.bmp").convert()

grass_tile = tileset.subsurface([0,16,16,16])

screen.blit(grass_tile, (0, 0))