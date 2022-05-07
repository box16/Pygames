import pygame
import random

DISPLAY_WIDTH = 720
DISPLAY_HEIGHT = 480
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MOVEMENT = 3
MOVEMENT_LIST = [-MOVEMENT, MOVEMENT]
PARTICLE_WIDTH = 8
PARTICLE_HEIGHT = 8
PARTICLES_NUM = 20


def get_movement(left, top, width, height):
    x_movement = random.choice(MOVEMENT_LIST)
    y_movement = random.choice(MOVEMENT_LIST)

    if ((left+x_movement) < 0) or (left+width+x_movement > DISPLAY_WIDTH):
        x_movement = 0
    if ((top+y_movement) < 0) or (top+height+y_movement > DISPLAY_HEIGHT):
        y_movement = 0

    return x_movement, y_movement


def get_random_pos():
    x = random.randint(0, DISPLAY_WIDTH)
    y = random.randint(0, DISPLAY_HEIGHT)
    return x, y


def generate_particles():
    particles = []
    for i in range(PARTICLES_NUM):
        fisrt_x, first_y = get_random_pos()
        image = pygame.Surface((PARTICLE_WIDTH, PARTICLE_HEIGHT))
        image.fill(WHITE)
        rect = pygame.Rect((fisrt_x, first_y),
                           (PARTICLE_WIDTH, PARTICLE_HEIGHT))
        particles.append((image, rect))
    return particles


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()
    particles = generate_particles()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(FPS)

        for image, rect in particles:
            x_movement, y_movement = get_movement(
                rect.left, rect.top, rect.width, rect.height)
            rect.move_ip(x_movement, y_movement)

        screen.fill(BLACK)
        screen.blits(particles)
        pygame.display.update()
