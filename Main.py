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
