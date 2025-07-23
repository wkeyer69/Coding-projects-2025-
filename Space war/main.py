import pygame
import random
import math
import sys
import os
from pygame import mixer

pygame.init()
pygame.font.init()

font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((800, 600))

pygame.mixer.music.load("pibu.mp3")
pygame.mixer.music.play(-1)



pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("download.png")

player_img = pygame.image.load("player.png")
player_x = 370
player_y = 480
velocity = 0
enemy_img = []
enemy_x = []
enemy_y = []
enemy_velocityX = []
enemy_velocityY = []
num_of_enemies = 10
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("hq720.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(0, 150))
    enemy_velocityX.append(1)
    enemy_velocityY.append(0)

bullet_img = pygame.image.load("bullet.png")
bullet_velocityX = 0
bullet_velocityY = 40
bullet_y = 440
bullet_x = 0
bullet_state = "ready"

score = 0
score_increment = 1

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y))

def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x-bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    

running = True
while running:
    screen.blit(background, (0, 0))
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                velocity = -5

            
            if event.key == pygame.K_d:
                velocity = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               if bullet_state is "ready":
                    
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                velocity = 0
    

          
    player_x += velocity
    
    if player_x <= 0:
        player_x = 0
    elif player_x >736:
        player_x = 736

    for i in range(num_of_enemies):
        enemy(enemy_x[i], enemy_y[i], i)
        collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            mus = mixer.Sound("pabu.mp3")
            mus.play()
            bullet_y = 440 
            bullet_state = "ready"
            score += 1
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(0, 150)
        enemy_x[i] += enemy_velocityX[i]
        enemy_y[i] += enemy_velocityY[i]



    
        if enemy_x[i] <= 0: 
            enemy_velocityX[i] = 1
            enemy_velocityY[i] = 0.1
        elif enemy_x[i] > 736:
            enemy_x[i] = 736
            enemy_velocityX[i] = -1
            enemy_velocityY[i] = 0.1
        if enemy_y[i] >= 480:
            running = False

    if bullet_y == 0:
        bullet_y = 440
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_velocityY

    
    
    
    


    player(player_x, player_y)
    
   
 
    pygame.display.update()
    