import pygame, sys, random

pygame.init()

CLOCK  = pygame.time.Clock()

width, height = 600, 500

display = pygame.display.set_mode((width, height))


player_img = pygame.image.load("racket.jpg")

player_img = pygame.transform.scale(player_img, (30, 80))




player_x = 30
player_y = 80
velocity = 0

def player(x, y):
    display.blit(player_img, (x, y))





while True:
    display.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                velocity = -20

            
            if event.key == pygame.K_d:
                velocity = 20

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                velocity = 0

        player_y += velocity

    player(player_x, player_y)

    pygame.display.update()
    CLOCK.tick(300)