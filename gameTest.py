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
hit = 0
work = True
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
def collideCar1(carX,carY):
    topLeftX = carX
    topLeftY = carY
    topRightX = carX + 25
    topRightY = carY

    bottomLeftX = carX
    bottomLeftY = carY + 25
    bottomRightX = carX + 25
    bottomRightY = carY + 25
    hit = False

    if (wallX["walloneX"] <= topLeftX <= wallX["walloneX"] + 400 and wallY["walloneY"] <= topLeftY <= wallY["walloneY"]+30 or wallX["walloneX"] <= bottomLeftX <= wallX["walloneX"]+400 and wallY["walloneY"] <= bottomLeftY <= wallY["walloneY"]+30 or wallX["walloneX"] <= topRightX <= wallX["walloneX"]+400 and wallY["walloneY"] <= topRightY <= wallY["walloneY"]+30 or wallX["walloneX"] <= bottomRightX <= wallX["walloneX"]+400 and wallY["walloneY"] <= bottomRightY <= wallY["walloneY"]+30):
        hit = True
        print "w1"
        return hit
    if (wallX["walltwoX"] <= topLeftX <= wallX["walltwoX"] + 20 and wallY["walltwoY"] <= topLeftY <= wallY["walltwoY"]+50 or wallX["walltwoX"] <= bottomLeftX <= wallX["walltwoX"]+20 and wallY["walltwoY"] <= bottomLeftY <= wallY["walltwoY"]+50 or wallX["walltwoX"] <= topRightX <= wallX["walltwoX"]+20 and wallY["walltwoY"] <= topRightY <= wallY["walltwoY"]+50 or wallX["walltwoX"] <= bottomRightX <= wallX["walltwoX"]+20 and wallY["walltwoY"] <= bottomRightY <= wallY["walltwoY"]+50):
        hit = True
        print "w2"
        return hit
    if (wallX["wallthreeX"] <= topLeftX <= wallX["wallthreeX"] + 20 and wallY["wallthreeY"] <= topLeftY <= wallY["wallthreeY"]+50 or wallX["wallthreeX"] <= bottomLeftX <= wallX["wallthreeX"]+20 and wallY["wallthreeY"] <= bottomLeftY <= wallY["wallthreeY"]+50 or wallX["wallthreeX"] <= topRightX <= wallX["wallthreeX"]+20 and wallY["wallthreeY"] <= topRightY <= wallY["wallthreeY"]+50 or wallX["wallthreeX"] <= bottomRightX <= wallX["wallthreeX"]+20 and wallY["wallthreeY"] <= bottomRightY <= wallY["wallthreeY"]+50):
        hit = True
        print "w3"
        return hit
    else:
        print "NOT HIT"
        return hit
              
def moveCar1(carX,carY):
    pygame.draw.rect(gameDisplay,grey, (carX, carY,30,30))

def moveCar2(car2X,car2Y):
    pygame.draw.rect(gameDisplay,black, (car2X, car2Y,30,30))












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
                hit = collideCar1(carX,carY)
                if hit == True:
                    carX.rect.move(2,0)
                    hit = False
                    work = False
                else:
                    carX.rect.move(-2,0)
                    work = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hit = collideCar1(carX,carY)
                if hit == True:
                    x_change = -2
                    hit = False
                else:
                    x_change = 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hit = collideCar1(carX,carY)
                if hit == True:
                    y_change = 2
                    hit = False
                else:
                    y_change = -2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                hit = collideCar1(carX,carY)
                if hit == True:
                    y_change = -2
                    hit = False
                else:
                    y_change = 2
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
        
