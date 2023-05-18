import pygame as pg
from pygame.sprite import Sprite


WIDTH = 800
HEIGHT = 600

FPS = 30

BLUE = (0,0,255)

BLACK = (0,0,0)

tasks = ["thrusters", "e-shields" ]

YELLOW = (0,255,255)


class Thruster(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.width = 25
        self.height = 25
        self.image = pg.Surface((self.width,self.height))
        self.color = YELLOW
        self.image.fill(self.color)
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
