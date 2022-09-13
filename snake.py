import pygame 
from pygame import *
import time
import random

pygame.init()
status = True
WIDTH = 800
HEIGHT = 500

#Colors
BLUE = (0, 100, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0 )
RED = (255, 0 , 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
posX = 300
posY = 300

newX = 0
newY = 0

font_style = pygame.font.SysFont("Colibri", 30)

snake_size = 20

# funzione messaggio
def messaggio (msg, color):
    mess = font_style.render(msg, True, color)
    screen.blit(mess, [10, 10])
        



while status:
    screen.fill(GREEN)
    for event in pygame.event.get():
        
        if event.type == QUIT:
            status = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                status = False
            if event.key == pygame.K_RIGHT: 
                newX = 5
                newY = 0
            if event.key == pygame.K_LEFT:
                newX = -5
                newY = 0
            if event.key == pygame.K_UP:
                newX = 0
                newY = -5
            if event.key == pygame.K_DOWN:
                newX = 0
                newY = 5


    posX += newX
    posY += newY
    if posX < 5 or posX > WIDTH-(snake_size+5):
        status = False
    if posY < 5 or posY > HEIGHT-(snake_size+5):
        status = False
    
    pygame.draw.rect(screen, RED, [0,0 , WIDTH, HEIGHT], 5) 
    pygame.draw.rect(screen, BLUE, [posX, posY, snake_size, snake_size])
    pygame.display.update()
    clock.tick(100)
 
messaggio("GAME OVER !", RED) 
pygame.display.update()

time.sleep(1)
pygame.quit()
quit()

