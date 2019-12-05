import pygame
import time
import random

pygame.init()
time.sleep(1)

height = 700
width = 1200

SCREEN = pygame.display.set_mode((width, height))
SCREEN.fill((0,0,0))
pygame.display.update()

#BasicColors
BasicRed = (255, 0, 0)
BasicGreen = (0, 255, 0)
BasicBlue = (0, 0, 255)
BasicYellow = (255, 255, 0)

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

#Background
BackRed = 0
BackGreen = 0
BackBlue = 0

DanceFloorDelay = 5 #Change this to change the rate of change of the dance floor.
CurrentDanceDelay = 0

#DoorInfo
CommonDoorWidth = 40
DoorTeleportSpacing = 10
DoorColors = (BasicBlue, BasicGreen, BasicYellow, BasicRed) #L, R, U, D
DoorLeft = (0, 0, CommonDoorWidth, height) #x, y, SizeX, SizeY
DoorRight = (width - CommonDoorWidth, 0, CommonDoorWidth, height)

#Room
Rooms = ("Spawn", "DanceFloor")
CurrentRoom = "Spawn" #Default


run = True
#this is our game loop
while run:
    pygame.time.delay(50)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
            
    #Input
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
        
    #State Checks
    if x < (CommonDoorWidth + radius): #Left
        if CurrentRoom == Rooms[0]:
            CurrentRoom = Rooms[1]
            x = width - (CommonDoorWidth + radius + DoorTeleportSpacing)
            
            
    if x > (width - (CommonDoorWidth + radius)): #height
        if CurrentRoom == Rooms[1]:
            CurrentRoom = Rooms[0]
            x = CommonDoorWidth + radius + DoorTeleportSpacing
            
    #Draw Functions
        
    #Background
    SCREEN.fill((0, 0, 0)) #Default Room Colour
    if CurrentRoom == Rooms[1]:
        if CurrentDanceDelay >= DanceFloorDelay:
            BackRed = random.randint(1, 255)
            BackGreen = random.randint(1, 255)
            BackBlue = random.randint(1, 255)
            CurrentDanceDelay = 0
        else:
            CurrentDanceDelay = CurrentDanceDelay + 1
        SCREEN.fill((BackRed, BackGreen, BackBlue))
    
    
    pygame.draw.circle(SCREEN, (255,0,0), (x,y), radius)
    pygame.draw.rect(SCREEN, (150, 150, 150), (x - (SquareSizeX/2), y - SquareHatOffset, SquareSizeX, SquareSizeY))
    pygame.draw.rect(SCREEN, (150, 150, 150), (x - (BaseSizeX/2), y - BaseOffset, BaseSizeX, BaseSizeY))
    #Doors L, R, U, D
    pygame.draw.rect(SCREEN, DoorColors[0], (DoorLeft[0], DoorLeft[1], DoorLeft[2], DoorLeft[3]))
    pygame.draw.rect(SCREEN, DoorColors[1], (DoorRight[0], DoorRight[1], DoorRight[2], DoorRight[3]))
    pygame.display.update()
    


pygame.quit()
