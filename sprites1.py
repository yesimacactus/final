import pygame as pg
from random import randint
from Settings1 import *
from time import sleep

def type():
            num = randint(0,1)
            global task
            task = tasks[num]



def direction():
    if task == "thrusters":
        num2 = randint(0,3)
        print("thrusters to level " + str(num2))
    elif task == "e-shields":
        print("Engage/Disengage e-shields")



'''
type()
direction() '''
'''

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        thruster1 = Thruster(1,1)
        self.all_sprites.add(thruster1)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    def update(self):
        self.all_sprites.update()
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)  
        pg.display.flip()  

g = Game()

while g.running:
    g.new() '''
    
      

            


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("my game")
clock = pg.time.Clock()
running = True
print(screen)


running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False

    thruster1 = Thruster(1,1)


    type()
    direction()
    if task == "thrusters":
        print("a")

    if task == "e-shields":
        print("b")

    
    pg.display.flip



pg.quit()