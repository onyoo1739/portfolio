import pygame
from pygame.locals import*
running=True
drawing = False
SIZE = (640,240)
RED=(255,0,0)
BLUE=(0,0,255)
screen = pygame.display.set_mode(SIZE)
rect_li=[]
pygame.init()
while running:
    screen.fill("BLACK")
    for event in pygame.event.get():
        #print(event)
        if event.type ==pygame.QUIT:
            running=False
        for rect in range(1,10) :
            if event.type == MOUSEBUTTONDOWN:
                drawing= True
                start = event.pos
            elif event.type == MOUSEMOTION and drawing:
                end = event.pos
                size=(abs(end[0]-start[0]),abs(end[1]-start[1]))
                start1=(min(start[0],end[0]),min(start[1],end[1]))
                pygame.draw.rect(screen,BLUE,(start1,size),1)
                pygame.display.update()

            elif event.type == MOUSEBUTTONUP:
                drawing= False
                end=event.pos
                size=(abs(end[0]-start[0]),abs(end[1]-start[1]))
                start1=(min(start[0],end[0]),min(start[1],end[1]))
                print(size)
                rect_li.append((starot1,size))

    
    for i in rect_li:
        pygame.draw.rect(screen,RED,i,3)
    pygame.display.update()

pygame.quit()