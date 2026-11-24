import pygame
pygame.init()

screen=pygame.display.set_mode((500,500))

pygame.display.set_caption("A eurasian lynx. one of the biggest cat species type")

image=pygame.image.load("eurasian lynx.jpg")

defimgsize=(300,300)

image=pygame.transform.scale(image,defimgsize)

green=(0,255,0)
defpos=(90,90)


while True:
    screen.fill(green)
    screen.blit(image,defimgsize)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()

