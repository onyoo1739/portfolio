import pygame
from pygame.locals import*
BLACK = (0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
WHITE=(255,255,255)
background=WHITE
SIZE=(640,320)
screen=pygame.display.set_mode(SIZE)
screen.fill(background)
pygame.draw.ellipse(screen,RED,(50, 20, 120, 100))
pygame.draw.ellipse(screen,GREEN,(100, 60, 120, 100))
pygame.draw.ellipse(screen,BLUE,(150, 100, 120, 100))
pygame.draw.ellipse(screen,RED,(350, 20, 120, 100), 1)
pygame.draw.ellipse(screen,GREEN, (400, 60, 120, 100), 4)
pygame.draw.ellipse(screen,BLUE, (450, 100, 120, 100), 8)

pygame.display.update()