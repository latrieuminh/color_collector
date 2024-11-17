# Write your codes here
import pygame
from random import randint, choice
import time
pygame.init()

S_WIDTH = 700
S_HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

main_win = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Color Collector")


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, speed):
        super().__init__()  # Initialize the sprite superclass
        
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.color = color 

    
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed 
        if keys[pygame.K_RIGHT] and self.rect.x < S_WIDTH - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < S_HEIGHT - self.rect.height:
            self.rect.y += self.speed

player = Player(WHITE, 5, S_HEIGHT - 50, 50, 50, 10)

class Block(GameSprite):
    def __init__(self, color, x, y, width, height, speed):
        super().__init__(color, x, y, width, height, speed)
        self.speed_x = speed
        self.speed_y = speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y 

        if self.rect.right >= S_WIDTH or self.rect.left <= 0:
            self.speed_x = -self.speed_x 
        if self.rect.bottom >= S_HEIGHT or self.rect.top <= 0:
            self.speed_y = -self.speed_y

player = Player(WHITE, S_WIDTH // 2, S_HEIGHT // 2, 50, 50, 5)
blocks = pygame.sprite.Group()


def create_blocks():
    color = choice(COLORS)
    block = Block(color, randint(0, S_WIDTH - 30), randint(0, S_HEIGHT - 30), 30, 30, 2)
    blocks.add(block)

for i in range(7):
    create_blocks()

score = 0
target_color = choice(COLORS)
start_time = time.time()
game_duration = 90 

game = True
clock = pygame.time.Clock()
FPS = 60

pygame.font.init()
font1 = pygame.font.Font(None, 36)
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    main_win.fill(BLACK)

    player.update()
    player.reset()

    blocks.update()
    blocks.draw(main_win)
    score_text = font1.render(f"score: {score}", True, WHITE)
    main_win.blit(score_text, (10, 10))
    color_text = font1.render(f"Target color:", True, WHITE)
    main_win.blit(color_text, (10, 40))

    pygame.display.update()
    clock.tick(FPS)





        
        

