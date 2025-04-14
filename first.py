import pygame

# Initialize Pygame
pygame.init()

# create screen
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("first game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("W key pressed")

    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))
    pygame.draw.circle(screen, (0, 255, 0), (250, 250), 50)
    pygame.display.flip()