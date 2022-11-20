from pygame import *
from random import randint
win_width = 900
win_height = 700
w = display.set_mode((win_width, win_height))
background = (255,255,255)
w.fill(background)
display.set_caption('Пинг-понг.')

game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()        
    clock.tick(FPS)