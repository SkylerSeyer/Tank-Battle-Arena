import pygame
from random import randint

pygame.init()

display_width = 600
display_height = 400

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Save My Soul')

black = (0,0,0)
white = (255,255,255)
grey = (123,123,123)
clock = pygame.time.Clock()
running = True
wallX = {
    "walloneX" : (100),
    "walltwoX" : (100),
    "wallthreeX" : (480)
    }
wallY = {
    "walloneY" : (200),
    "walltwoY" : (300),
    "wallthreeY" : (80)
    }






wallImg = pygame.draw.rect(gameDisplay,black, [100,100,50,100])
def moveCar1(carX,carY):
    if  not (wallX["walloneX"] < carX < wallX["walloneX"] + 400 and wallY["walloneY"] < carY < wallY["walloneY"]+30):
        pygame.draw.rect(gameDisplay,grey, (carX, carY,30,30))
    else:
        pygame.draw.rect(gameDisplay,grey, (randX, randY,50,50))
def moveCar2(car2X,car2Y):
    pygame.draw.rect(gameDisplay,black, (car2X, car2Y,30,30))

def tankHitsLeft(carX,carY):
    for wall in map.getWalls():
        if (wall.getY()-15 <= tank.getY() <= wall.getY()+95):
            if 0 <= abs(wall.getX()+80 - tank.getX()+15) <= 2:
                return True
def tankHitsRight(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getY()-15 <= tank.getY() <= wall.getY()+95):
            if 0 <= abs(wall.getX() - tank.getX()-15) <= 2:
                return True
def tankHitsUp(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getX()-15 <= tank.getX() <= wall.getX()+95):
            if 0 <= abs(wall.getY()+80 - tank.getY()+15) <= 2:
                return True
def tankHitsDown(tank, map, screen):
    for wall in map.getWalls():
        if (wall.getX()-15 <= tank.getX() <= wall.getX()+95):
            if 0 <= abs(wall.getY() - tank.getY()-15) <= 2:
                return True










def wall(wallX,wallY):
        pygame.draw.rect(gameDisplay,black,(wallX["walloneX"],wallY["walloneY"],400,30))
        pygame.draw.rect(gameDisplay,black,(wallX["walltwoX"],wallY["walltwoY"],20,50))
        pygame.draw.rect(gameDisplay,black,(wallX["wallthreeX"],wallY["wallthreeY"],20,50))

carX =  (display_width * 0.5)
carY = (display_height * 0.9)
car2X = (display_width * .5)
car2Y = (display_height * .1)
x_change = 0
y_change = 0
car_speed = 0

while running:
    gameDisplay.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2
                moveCar1(carX,carY)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_change = 2
                moveCar1(carX,carY)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -2
                moveCar1(carX,carY)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_change = 2
                moveCar1(carX,carY)
#############################################################################

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                x2_change = -2
                moveCar2(car2X,car2Y)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                x2_change = 2
                moveCar2(car2X,car2Y)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                y2_change = -2
                moveCar2(car2X,car2Y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                y2_change = 2
                moveCar2(car2X,car2Y)

        else:
            y_change = 0
            x_change = 0
            y2_change = 0
            x2_change = 0

                
        ######################
    ##
    carX += x_change
    carY += y_change
    car2X += x2_change
    car2Y += y2_change
   ##         
    #gameDisplay.fill(white)
    moveCar1(carX,carY)
    moveCar2(car2X,car2Y)
    wall(wallX,wallY)
    #wall(wallX,wallY) 
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

        
