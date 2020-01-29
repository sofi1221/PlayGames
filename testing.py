import pygame

pygame.init()
size = width, height = 1100, 700
screen = pygame.display.set_mode(size)
pos = (400, 350 + 175)
pos_vrag = (400, 175)
pos_shaiba = (400, 350)
x = 0
v_x = 0
v_y = 0


def draw():
    # screen.fill((204, 202, 202))  # светлая тема
    screen.fill((57, 57, 57))  # темная тема
    pygame.draw.rect(screen, pygame.Color(87, 87, 87), (150, 0, 500, 700), 0)
    # pygame.draw.rect(screen, pygame.Color(230, 230, 230), (150, 0, 500, 700), 0)
    pygame.draw.rect(screen, pygame.Color(147, 147, 147), (150, 340, 500, 20), 0)
    pygame.draw.circle(screen, (147, 147, 147), (400, 350), 64)
    pygame.draw.rect(screen, pygame.Color(255, 13, 0), (300, 680, 200, 20), 0)
    pygame.draw.rect(screen, pygame.Color(51, 61, 255), (300, 0, 200, 20), 0)


def otbit():
    global v_x, v_y
    if (pos[0] - pos_shaiba[0]) ** 2 + (pos[1] - pos_shaiba[1]) ** 2 <= 40 ** 2:
        v_x = (-pos[0] + pos_shaiba[0]) // 5
        v_y = (-pos[1] + pos_shaiba[1]) // 5
    if (pos_vrag[0] - pos_shaiba[0]) ** 2 + (pos_vrag[1] - pos_shaiba[1]) ** 2 <= 40 ** 2:
        v_x = (-pos_vrag[0] + pos_shaiba[0]) // 5
        v_y = (-pos_vrag[1] + pos_shaiba[1]) // 5


def kraya():
    global v_y, v_x
    if pos_shaiba[0] - 20 <= 150 or pos_shaiba[0] + 20 >= 150 + 500:
        v_x *= -1
    if pos_shaiba[1] - 20 <= 0 or pos_shaiba[1] + 20 >= 700:
        v_y *= -1


def vorota():
    pass

def vozvrat():
    pass


draw()
pygame.display.flip()
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            vozvrat()
    draw()
    pygame.display.flip()
    clock.tick(24)
