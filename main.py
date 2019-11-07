import pygame
import time

pygame.init()
time.sleep(1)

height = 700
width = 1200

SCREEN = pygame.display.set_mode((width, height))
SCREEN.fill((0,0,0))
pygame.display.update()

#player
x = 200
y = 300
radius = 75

#player customization (Little Square Top)
SquareHatOffset = 110
SquareSizeX = 100
SquareSizeY = 50
BaseOffset = 75
BaseSizeX = 150
BaseSizeY = 20

run = True
#this is our game loop
while run:
    pygame.time.delay(50)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
            
    keyPress = pygame.key.get_pressed()
    
    if keyPress[pygame.K_ESCAPE]:
        run = False
        
    if keyPress[pygame.K_w]:
        y = y - 20
        if y < (radius + (SquareHatOffset - radius)):
            y = radius + (SquareHatOffset - radius)
    
    if keyPress[pygame.K_s]:
        y = y + 20
        if y > height - radius:
            y = height - radius
        
    if keyPress[pygame.K_a]:
        x = x - 20
        if x < radius:
            x = radius
        
    if keyPress[pygame.K_d]:
        x = x + 20
        if x > width - radius:
            x = width - radius
        
    #Draw Functions
    SCREEN.fill((0,0,0))
    pygame.draw.circle(SCREEN, (255,0,0), (x,y), radius)
    pygame.draw.rect(SCREEN, (150, 150, 150), (x - (SquareSizeX/2), y - SquareHatOffset, SquareSizeX, SquareSizeY))
    pygame.draw.rect(SCREEN, (150, 150, 150), (x - (BaseSizeX/2), y - BaseOffset, BaseSizeX, BaseSizeY))
    pygame.display.update()
    


pygame.quit()
