import pygame
pygame.init()
screen=pygame.display.set_mode((300,600))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            

    pygame.draw.rect(screen,(0,17,125), pygame.Rect(45,45, 60, 70))

    pygame.display.flip()