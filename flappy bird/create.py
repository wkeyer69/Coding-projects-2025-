import pygame 
from sys import exit 
import random 

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((551, 720))

bird_images = [pygame.image.load("flappy bird/assets/bird_down.png"),
               pygame.image.load("flappy bird/assets/bird_mid.png"),
               pygame.image.load("flappy bird/assets/bird_up.png")]
skyline_image = pygame.image.load("flappy bird/assets/background.png")
ground_image = pygame.image.load("flappy bird/assets/ground.png")
top_pipe_image = pygame.image.load("flappy bird/assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("flappy bird/assets/pipe_bottom.png")
game_over_image = pygame.image.load("flappy bird/assets/game_over.png")
start_image = pygame.image.load("flappy bird/assets/start.png")


scroll_speed = 1
bird_start_position = (100, 250)
score = 0
font = pygame.font.SysFont('Segoe', 26)
game_stopped = True

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.alive = True

    def update(self, user_input):
        if self.alive:
           self.image_index += 1 
        if self.image_index < 20:
            self.image_index = 0
        self.image = bird_images[self.image_index // 10]

        self.vel += 1
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500 and self.rect.y > 0: 
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False 
        
        self.image = pygame.transform.rotate(self.image, self.vel * -7)

        if user_input[pygame.K_SPACE]: 
            self.vel = -7 
            self.flap = True 
        if user_input[pygame.K_a]:
            self.vel = 7 
            

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.passed, self.exit = False, False, False 
        self.pipe_type = pipe_type 

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.x <= 30:
            self.kill()
        

        global score
        if self.pipe_type == 'bottom': 
            if bird_start_position > self.rect.topleft:
                self.enter = True 
            if bird_start_position > self.rect.topright:
                self.exit = True 
            if self.enter and self.exit and not self.passed: 
                self.passed = True
                score += 1

class Ground(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        
        self.rect.x -= scroll_speed
        if self.rect.x <= -551:
            self.kill()


def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()



def main():

    global score 

    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())

    pipe_timer = 0
    pipe = pygame.sprite.Group()
    


    ground_x = 0
    ground_y = 520
    ground = pygame.sprite.Group()
    ground.add(Ground(ground_x, ground_y))

    run = True
    while run: 

        quit_game()
        window.fill((0, 0, 0))
        window.blit(skyline_image, (0, 0))

        bird.draw(window)
        pipe.draw(window)
        ground.draw(window)

        score_text = font.render("score: " + str(score), True, pygame.Color(255, 0, 0))
        window.blit(score_text, (0, 0))

        if len(ground) <= 1:
            ground.add(Ground(551, ground_y))


        user_input = pygame.key.get_pressed()
        
        if bird.sprite.alive: 
            pipe.update()
            ground.update()
        bird.update(user_input)

        if pipe_timer <= 0: 
            pipe_top_x = 500 
            pipe_top_y = random.randint(-800, -700)
            pipe_bottom_x = 500 
            pipe_bottom_y = random.randint(1100, 1200) + pipe_top_y
            pipe.add(Pipe(pipe_top_x, pipe_top_y, top_pipe_image, 'top'))
            pipe.add(Pipe(pipe_bottom_x, pipe_bottom_y, bottom_pipe_image, 'bottom'))
            pipe_timer = random.randint(90, 180)
        pipe_timer -= 1

        col_pipe = pygame.sprite.spritecollide(bird.sprites()[0], pipe, False)
        col_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
        if bird.sprite.rect.y <= 20:
            bird.sprite.alive = False
            bird.sprite.y = 0
            window.blit(game_over_image, (200, 350)) 
            if user_input[pygame.K_r]:
                score = 0
                break
        
        if col_pipe or col_ground:
            bird.sprite.alive = False
            bird.sprite.vel = 0
            window.blit(game_over_image, (200, 350)) 
            if user_input[pygame.K_r]:
                score = 0
                break

        clock.tick(60)

        pygame.display.update()







def menu():
    global game_stopped
    while game_stopped:
        quit_game()
        window.fill((0, 0, 0))
        window.blit(skyline_image, (0, 0))
        window.blit(bird_images[0], (100, 250))
        window.blit(ground_image, (0, 520))
        window.blit(start_image, (150, 250))
        user_input = pygame.key.get_pressed()
        
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()

menu()
            
            





    


        


