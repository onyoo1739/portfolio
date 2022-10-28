import pygame
from pygame.locals import*
SIZE=(640,320)
width,height=SIZE
GREEN=(150,255,150)
RED=(255,0,0)
pygame.init()
screen=pygame.display.set_mode(SIZE)
running=True
ball=pygame.image.load("ball.gif")
rect=ball.get_rect()
speed=[1,1]
while running:
    rect=rect.move(speed)
    screen.fill(GREEN)
    pygame.draw.rect(screen,RED,rect,1)
    screen.blit(ball,rect)
    pygame.display.update()
    pygame.time.delay(5)
    if rect.left <0 or rect.right > width :
        speed[0]=-speed[0]
    if rect.top<0 or rect.bottom > height:
        speed[1]=-speed[1]

    for event in pygame.event.get():
        if event.type == QUIT:
            running=False
    