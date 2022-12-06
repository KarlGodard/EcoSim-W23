import pygame

file = 'PixelArt/ecosimPixelArt.bmp'
image = pygame.image.load(file)
rect = image.get_rect()
print(image)

pygame.init()
screen_size = (16 * 12, 16 * 8)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

#screen.blit(image, rect)
pygame.display.update()

pixel_w = 16
pixel_h = 16
size = (16, 16)

tiles = []

#load tiles
grass = pygame.Surface(size)
dest = ((0, 0), size)
grass.blit(image, (0, 0), dest)
tiles.append(grass)

dirt = pygame.Surface(size)
dest = ((16, 0), size)
dirt.blit(image, (0, 0), dest)
tiles.append(dirt)

water = pygame.Surface(size)
dest = ((32, 0), size)
water.blit(image, (0, 0), dest)
tiles.append(water)

prey = pygame.Surface(size)
dest = ((0, 16), size)
prey.blit(image, (0, 0), dest)
tiles.append(prey)

pred = pygame.Surface(size)
dest = ((16, 16), size)
pred.blit(image, (0, 0), dest)
tiles.append(pred)

plant = pygame.Surface(size)
dest = ((32, 16), size)
plant.blit(image, (0, 0), dest)
tiles.append(plant)

screen.blit(water, (0, 0))
screen.blit(grass, (16 * 4, 16 * 3))
pygame.display.flip()

# for x in range(16):
#     for y in range(12):
#         screen.blit(tiles[x % 6], (16 * x, 16 * y))

# pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()







  