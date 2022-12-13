import pygame
import random
import math
from SpriteSheet import *
pygame.init()

screen = pygame.display.set_mode([900,700])
pygame.display.set_caption('Block Runner')
pygame_icon = pygame.image.load('player.png')
pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()

start = "starting"
background = ("")
player = pygame.image.load("player.png")
playerX = 435
playerY = 615
xSpeed = 5
ySpeed = 5
playerX_Speed = 0
playerY_Speed = 0

block = pygame.image.load('block.png') 
blockX = random.randint(68, 816)
blockY = random.randint(119, 632)

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 62
textY = 80

settings = pygame.image.load("settingsButton.png")
settingsX = 790
settingsY = 65

def show_score(x, y):
    score = font.render("Score:" + " " + str(score_value), True, (60, 60, 60))
    screen.blit(score, (x, y))

def isCollision(blockX, blockY, playerX, playerY):
	distance = math.sqrt((math.pow(blockX-playerX, 2)) + (math.pow(blockY-playerY, 2)))
	if distance < 27:
		return True
	else:
		return False

while True:
    
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    sys.exit();
    
    if event.type == pygame.KEYDOWN:
	    print("down")
	    if event.key == pygame.K_RETURN:
		    start = "play"
	    if event.key == pygame.K_RSHIFT:
		    start = "settings"
	    if event.key == pygame.K_LEFT:
		    playerX_Speed = -xSpeed
		    playerY_Speed = 0
	    if event.key == pygame.K_RIGHT:
		    playerX_Speed = xSpeed
		    playerY_Speed = 0
	    if event.key == pygame.K_UP:
		    playerX_Speed = 0
		    playerY_Speed = -ySpeed
	    if event.key == pygame.K_DOWN:
		    playerX_Speed = 0
		    playerY_Speed = ySpeed
		    
    if start == "starting":
	    background = pygame.image.load("startScreen.png")
    if start == "play":
	    background = pygame.image.load("background.png")
    print(playerX_Speed, playerY_Speed, playerX, playerY)

    if playerX <= 64:
	    playerX = 64
    if playerX >= 812:
	    playerX = 812
    if playerY <= 115:
	    playerY = 115
    if playerY >= 636:
	    playerY = 636


    collision = isCollision(blockX, blockY, playerX, playerY)
    if collision:
	    score_value += 1
	    blockX = random.randint(68, 816)
	    blockY = random.randint(119, 632)

    screen.blit(background, (0, 0))
    if start == "play":
	    screen.blit(player,(playerX, playerY))

    playerX = playerX + playerX_Speed
    playerY = playerY + playerY_Speed

    if start == "play":
	    screen.blit(block,(blockX, blockY))
    #pygame.transform.scale(player, (1 + (score_value/100)), (1 + (score_value/100)))
    if start == "play":
	    show_score(textX, textY)
    if start == "play":
	    screen.blit(settings, (settingsX, settingsY))

    if start == "settings":
	    background = pygame.image.load("SettingsScreen.png")
    pygame.display.flip()

    
    clock.tick(60)
import pygame
import sys
from SpriteSheet import *
pygame.init()

screen = pygame.display.set_mode([900,700])
pygame.display.set_caption('Block Runner')
pygame_icon = pygame.image.load('player.png')
pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()

background = pygame.image.load("background.png")
player = pygame.image.load("player.png")




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
            
 
        
            
    
    screen.blit(background, (0, 0))
    screen.blit(player, (435, 615))

    pygame.display.flip()
    clock.tick(60)
