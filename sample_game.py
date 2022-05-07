import pygame
import random

DISPLAY_WIDTH = 720
DISPLAY_HEIGHT = 480
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

rect = pygame.Rect((0, 0), (8, 8))
image = pygame.Surface((8, 8))
image.fill(WHITE)


def get_movement():
    _random = random.randrange(3)
    if _random == 0:
        return -5
    elif _random == 1:
        return 0
    else:
        return 5


def limit_movement(rect, x_movement, y_movement):
    _left = rect.left
    _width = rect.width
    _top = rect.top
    _height = rect.height

    _x = x_movement
    _y = y_movement

    if ((_left+x_movement) < 0) or (_left+_width+x_movement > 720):
            _x = 0
    if ((_top+y_movement) < 0) or (_top+_height+y_movement > 480):
        _y = 0

    return _x, _y


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(FPS)
    x_movement, y_movement = limit_movement(
        rect, get_movement(), get_movement())
    rect.move_ip(x_movement, y_movement)
    screen.fill(BLACK)
    screen.blit(image, rect)
    pygame.display.update()
