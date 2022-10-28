from sre_constants import CATEGORY_NOT_LINEBREAK
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
backgorund = WHITE
key_dict={K_k:BLACK, K_r:RED, K_g:GREEN,K_b:BLUE,K_y:YELLOW,K_c:CYAN,K_m:MAGENTA,K_w:WHITE}
alphabet={K_a:"a", K_b:'b', K_c:'c',K_d:'d',K_e:'e'}
pygame.init()
SIZE = (640,240)
screen = pygame.display.set_mode(SIZE)
running=True
while running:
    #print(pygame.time.get_ticks()/1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            print(event)
        if event.type == pygame.KEYDOWN:
            if event.key in key_dict :
                background = key_dict[event.key]
                caption = 'background color =' + str(background)
                pygame.display.set_caption(caption)
                screen.fill(background)
            if event.key in alphabet:
                print(alphabet[event.key])
    pygame.display.update()
   

pygame.quit()

