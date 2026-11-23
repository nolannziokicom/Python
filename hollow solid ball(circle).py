

import pygame
pygame.init()

webpage=pygame.display.set_mode((900,300))



darkblue=(0,0,139)
green=(0,255,135)

pygame.draw.circle(webpage, darkblue,(90,90),35)
pygame.draw.circle(webpage, green,(145,90),35, 3)


pygame.display.update()

go=False

while not go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go=True



    

    pygame.display.flip()



    