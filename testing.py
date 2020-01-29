import pygame

pygame.init()
size = width, height = 1100, 700
screen = pygame.display.set_mode(size)


def draw():
    pass


def otbit():
    pass


def kraya():
    pass


def vorota():
    pass


def vozvrat():
    pass


pygame.display.flip()
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    pygame.display.flip()
    clock.tick(24)
