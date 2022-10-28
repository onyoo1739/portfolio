import pygame
from pygame.locals import*
running=True
drawing = False
SIZE = (640,640)
RED=(255,0,0)
BLUE=(150,150,255)
screen = pygame.display.set_mode(SIZE)
line_li=[]
pygame.init()
while running:
    screen.fill("BLACK")
    for event in pygame.event.get():
        #print(event)
        if event.type ==pygame.QUIT:
            running=False

        if event.type == MOUSEBUTTONDOWN:
            drawing= True
            start = event.pos
            line_li.append(start)
        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            if len(line_li) <=1:
                line_li.append(end)
            line_li[-1] = end
            
            pygame.draw.lines(screen,RED,True,line_li,3)
            pygame.display.update()

        elif event.type == MOUSEBUTTONUP:
            drawing= False
            end = event.pos
            max(i[0] for i in line_li)
            start1= (min(i[0] for i in line_li),min(j[1] for j in line_li))
            a=abs(max(i[0] for i in line_li) - min(j[0] for j in line_li ))
            b=abs(max(i[1] for i in line_li) - min(j[1] for j in line_li ))
            size=(a,b)
            pygame.draw.lines(screen,RED,True,line_li,3)
            pygame.draw.rect(screen,BLUE,(start1,size),1)
            pygame.display.update()
        if event.type == KEYDOWN:
            if event.key == K_r:
                line_li.pop()
                a=abs(max(i[0] for i in line_li) - min(j[0] for j in line_li ))
                b=abs(max(i[1] for i in line_li) - min(j[1] for j in line_li ))
                size=(a,b)
                pygame.draw.lines(screen,RED,True,line_li,3)
                pygame.draw.rect(screen,BLUE,(start1,size),1)
                pygame.display.update()



    
    #for i in line_li:
        #pygame.draw.lines(screen,RED,True,i,3)

pygame.quit()