import pygame
from pygame.locals import*
running=True
pygame.init()
SIZE = (640,640)
RED=(255,0,0)
BLUE=(150,150,255)
BLACK=(0,0,0)
screen = pygame.display.set_mode(SIZE)
drawing=False
c=pygame.image.load("c.png")
rect=ball.get.rect()
speed=[1,1]
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
        if event.type == MOUSEBUTTONDOWN:
            start= event.pos
            drawing =True
        elif event.type == MOUSEMOTION and drawing:
            screen.fill(BLACK)
            end = event.pos
            pygame.draw.circle(screen,BLUE,end,5)
            size = (abs(start[0]-end[0]),abs(start[1]-end[1]))
            start1=(min(start[0],end[0]),min(start[1],end[1]))
            pygame.draw.rect(screen,BLUE,(start1,size),1)

        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            screen.fill(BLACK)
            pygame.draw.circle(screen,BLUE,end,5)
            size = (abs(start[0]-end[0]),abs(start[1]-end[1]))
            start1=(min(start[0],end[0]),min(start[1],end[1]))
            pygame.draw.rect(screen,BLUE,(start1,size),1)
            drawing=False

        pygame.display.update()
            







pygame.quit()