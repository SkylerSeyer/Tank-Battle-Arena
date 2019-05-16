from Tank import *
from Map import *
from Round import *
from Wall import *
import os
import Tkinter
import tkFileDialog
from tkFileDialog import askopenfilename
from Tkinter import *
import pygame
import numpy
import sys
from pygame.locals import *
import RPi.GPIO as GPIO
from time import sleep
pygame.init()

#sound
buzzer = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer,GPIO.OUT)

#colors
BLACK = (  0,   0,   0)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
level1 = Map('./level3')
tankIMG = pygame.image.load("tankSKIN.png")
enemyTankIMG = pygame.image.load("enemyTank.png")

def drawWall(Wall, screen):
    pygame.draw.rect(screen, BLACK, [Wall.getX(), Wall.getY(), 47, 45])

def drawTank(map, Tank, color, screen):
    screen.blit(tankIMG, ([Tank.getX()-15,Tank.getY()-15]))

def drawEnemyTank(map, Tank, color, screen):
    screen.blit(enemyTankIMG, ([Tank.getX()-15,Tank.getY()-15]))


def drawAllWalls(map, screen):
    for wall in map.getWalls():
        drawWall(wall, screen)

def drawCrosshairs(mouse, screen):
    x, y = mouse
    pygame.draw.circle(screen, RED, mouse, 10, 3)
    pygame.draw.line(screen, BLUE, (x, y-13), (x, y+13), 3)
    pygame.draw.line(screen, BLUE, (x-13, y), (x+13, y), 3)

def drawRound(round, screen):
    pygame.draw.circle(screen, WHITE, round.getCoords(), 5)


def bounceRoundsX(round, map, screen):
    for wall in map.getWalls():
        if (wall.getY() < round.getY() < wall.getY()+45):
            if 0 <= abs(wall.getX() - round.getX()) <= 4 and not round.isDead():
                round.bounceX()
            if 0 <= abs(wall.getX()+47 - round.getX()) <= 4 and not round.isDead():
                round.bounceX()

def bounceRoundsY(round, map, screen):
    for wall in map.getWalls():
        if (wall.getX() < round.getX() < wall.getX()+47) :
            if 0 <= abs(wall.getY() - round.getY()) <= 4 and not round.isDead():
                round.bounceY()
            if 0 <= abs(wall.getY()+45 - round.getY()) <= 4 and not round.isDead():
                round.bounceY()


def tankHitsLeft(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getY()-12 <= tank.getY() <= wall.getY()+57):
            if 0 <= abs(wall.getX()+47 - tank.getX()+20) <= 2:
                return True
def tankHitsRight(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getY()-12 <= tank.getY() <= wall.getY()+57):
            if 0 <= abs(wall.getX() - tank.getX()-15) <= 2:
                return True
def tankHitsUp(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getX()-13 <= tank.getX() <= wall.getX()+60):
            if 0 <= abs(wall.getY()+45 - tank.getY()+20) <= 2:
                return True
def tankHitsDown(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getX()-13 <= tank.getX() <= wall.getX()+60):
            if 0 <= abs(wall.getY() - tank.getY()-15) <= 2:
                return True

def roundHitsTank(round, tank):
    if (abs(tank.getX()-round.getX())<15 and abs(tank.getY()-round.getY())<15):
        return True
    else:
        return False

def Run():

    windowSize = (600, 400)
    screen = pygame.display.set_mode(windowSize)
    clock = pygame.time.Clock()
    shots = []
    enemyTanks = level1.getEnemyTanks()
    playerTank = level1.getPlayerTank()

    while True:

        clock.tick(30)
        mousePosition = pygame.mouse.get_pos()
        x, y = mousePosition

        #keys that are hit once
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if len(shots)<5:
                    shots.append(level1.getPlayerTank().fire(mousePosition, 10))

        #Keys that are being HELD DOWN, handle player moves
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if not tankHitsUp(level1.getPlayerTank(), level1, screen):
                level1.getPlayerTank().moveUp()
        if keys[pygame.K_s]:
            if not tankHitsDown(level1.getPlayerTank(), level1, screen):
                level1.getPlayerTank().moveDown()
        if keys[pygame.K_a]:
            if not tankHitsLeft(level1.getPlayerTank(), level1, screen):
                level1.getPlayerTank().moveLeft()
        if keys[pygame.K_d]:
            if not tankHitsRight(level1.getPlayerTank(), level1, screen):
                level1.getPlayerTank().moveRight()

        screen.fill(GREY)
        drawAllWalls(level1, screen)
        drawCrosshairs(mousePosition, screen)
        for n in shots:
            if (n.getX() > 600 or n.getX() < 0 or n.getY() > 400 or n.getY() < 0):
                shots.remove(n)
                break
            if n.isDead():
                shots.remove(n)
                break
            for e in enemyTanks:
                if roundHitsTank(n, e):
                    enemyTanks.remove(e)
                    shots.remove(n)
                    GPIO.output(buzzer,GPIO.HIGH)
                    sleep(.2)
                    GPIO.output(buzzer,GPIO.LOW)
            bounceRoundsX(n, level1, screen)
            bounceRoundsY(n, level1, screen)
            n.updatePosition()
            drawRound(n, screen)
        for e in enemyTanks:
            drawEnemyTank(level1, e, RED, screen)
        drawTank(level1, playerTank, GREEN, screen)
        #Always run this
        pygame.display.update()

# start the game
def start_game():
  Run()
  
  
# toggle on/off sound
def sound():
  global sound
  if (sound == True):
    print "Sound Off"
    sound = False
  else:
    print "Sound On"
    sound = True

#~~~~~~ GUI ~~~~~~~~

root = Tk()
root.title('Tank Battle Arena Menu')
root.geometry("600x400+250+100")
mf = Frame(root)
mf.pack()
f1 = Frame(mf, width=600, height=400)
f1.pack(fill=X)
f2 = Frame(mf, width=600, height=400)
f2.pack()
f3 = Frame(mf, width=600, height=400)
f3.pack()


Button(f1, text="Start", command=start_game).grid(row=1, column=10, sticky='ew', padx=8, pady=4)
Button(f2, text="Sound", command=sound).grid(row=2, column=27, sticky='ew', padx=8, pady=4)
Button(f3, text='Quit', command=root.destroy).grid(row=3, column=0, sticky=W, pady=4)
root.mainloop()
