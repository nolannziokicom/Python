import pygame
pygame.init()

darkblue=(0,0,139)

displaysurface=pygame.display.set_mode((500,500))

pygame.display.set_caption("Water is life")

image=pygame.image.load("water.jpg")

Defaultimagesize=(300,300)

image=pygame.transform.scale(image,Defaultimagesize)

defpos=(150,150)

while True:
    displaysurface.fill(darkblue)
    displaysurface.blit(image,Defaultimagesize)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()