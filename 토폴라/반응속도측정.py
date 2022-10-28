import random as rd
import pygame 
from pygame.locals import*
#(R,G,B)
BLACK = (0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
WHITE=(255,255,255)
background = WHITE
key_dict={K_k:BLACK, K_r:RED, K_g:GREEN,K_b:BLUE,K_y:YELLOW,K_c:CYAN,K_m:MAGENTA,K_w:WHITE}
alphabet={K_a:"a", K_b:'b', K_c:'c',K_d:'d',K_e:'e'}
pygame.init()
SIZE = (640,240)
screen = pygame.display.set_mode(SIZE)
screen.fill(background)

running=True
game_status = 'start'
while running:
    c_t = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            print(event)
        if event.type == pygame.KEYDOWN:
            if game_status == "start":
                if event.key == K_SPACE:
                    game_status = "wait"
                    w_t = c_t + rd.randint(1000,5000)
            if game_status =='wait for reaction':
                if a==key_dict[event.key]:
                    print(c_t - w_t)
                    '''
                    print(c_t)
                    print('Restart?')
                    if K_y :
                        running=True
                    elif K_n:
                        running=False
                    '''
                else:
                    game_status = 'start'
        
                
    if game_status == "wait":
        if c_t > w_t : 
            game_status = "wait for reaction"
            a=rd.choice([RED,GREEN])
            screen.fill(a)

    pygame.display.update()
   

pygame.quit()

