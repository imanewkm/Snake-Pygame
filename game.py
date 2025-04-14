import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Start point
x = 250
y = 250
speed = 0.1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]:
        x -= speed
    if keys [pygame.K_RIGHT]:
        x += speed
    if keys [pygame.K_UP]:
        y -= speed
    if keys [pygame.K_DOWN]:
        y += speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))
    pygame.display.flip()