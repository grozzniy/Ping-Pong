from pygame import *
from random import randint
win_width = 900
win_height = 700
w = display.set_mode((win_width, win_height))
background = (255,255,255)
display.set_caption('Пинг-понг.')

class GameSprite(sprite.Sprite):
    def __init__ (self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        w.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<700:
            self.rect.y += self.speed
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<700:
            self.rect.y += self.speed



player1 = Player("wall.png", 50, 0, 26, 200, 10)
player2 = Player("wall.png", 850, 0, 26, 200, 10)
ball = GameSprite('ball.png', 350, 450, 60, 60, 10)

        
game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    w.fill(background)
    player1.reset()
    player1.update()
    player2.reset()
    player2.update1()
    display.update()        
    clock.tick(FPS)
