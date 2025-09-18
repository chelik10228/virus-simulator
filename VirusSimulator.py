import pygame
import random

def draw(c1,c2,c3,sx,sy,x,y):
    pygame.draw.rect(screen, (c1,c2,c3), (sx,sy,x,y))
pygame.display.set_caption("virus-simulator")
screen = pygame.display.set_mode([640,480])
screen.fill((56,2,58))
while True:
    cube = random.randint(4,32)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_s:
                draw(150,255,0,random.randint(0,640),random.randint(0,480),cube,cube)
            elif e.key == pygame.K_k:
                draw(56,2,58,random.randint(0,640),random.randint(0,480),cube,cube)
            elif e.key == pygame.K_c:
                screen.fill((56,2,58))
            elif e.key == pygame.K_q:
                exit()

    pygame.display.flip()