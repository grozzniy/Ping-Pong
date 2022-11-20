from pygame import *
from random import randint
win_width = 900
win_height = 700
w = display.set_mode((win_width, win_height))
background = (255,255,255)
w.fill(background)
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

game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()        
    clock.tick(FPS)
