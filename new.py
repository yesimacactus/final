# file created by Joshua Cortezano
# new goal: jlasdlkfj

import pygame as pg
from random import randint
from sets1 import *
from time import sleep

global a
a = 0
# function that uses randint to create a 50/50 chance of the task variable being one of 2 things in a list
def type():
            global num
            num = randint(0,1)
            global task
            task = tasks[num]

# prints the directions of the task using if elif to make it different depending on which task
def direction():
    if task == "thrusters":
        global num2
        num2 = randint(0,3)
        global num3
        num3 = num2
        print("thrusters to level " + str(num2))
    elif task == "shields":
        a = randint(0,1)
        if a == 0:
            print("shields on")
        if a == 1:
            print("shields off")

# varaiableblebs
WIDTH = 800
HEIGHT = 600

FPS = 30
# tuple, RGB :)
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

# fucntions
    type()
    direction()
    # if u type in the number on  the directions, game continues, if not, game over
    if task == "thrusters":
        x = input("thruster level: ")
        if x == str(num2):
            print("good work")
        else:
            print("game over")
            running = False
            break
    
    # if follow direction ,game continues, if not, game over

    if task == "e-shields":
        if a == 0:
            y = input ("turn shields on")
            if y == "on":
                print("good stuff")
            else: 
                print("hint: type 'on' to turn on shields")
                running = False
                break
        if a == 1:
            y = input ("turn shields off")
            if y == "off":
                print("good stuff")
            else:
                print("hint: type 'off' to turn off shields")
                running = False
                break

    
pg.quit()
print("game over")