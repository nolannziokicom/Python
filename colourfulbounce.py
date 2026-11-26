import pygame
import random

pygame.init()


spritecolchangeeven=pygame.USEREVENT + 1
backgroundcolorchangeeve=pygame.USEREVENT + 2


Blue=pygame.Color("blue")
lightblue=pygame.Color("lightblue")
darkbl=pygame.Color("darkblue")

Yellow=pygame.Color("yellow")
red=pygame.Color("red")
lightgreen=pygame.Color("lightgreen")
cyan=pygame.Color("cyan")
orange=pygame.Color("orange")

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width ):
        super().__init__()
        self.image=pygame.Surface([width,height])

        self.image.fill(color)


        self.rect=self.image.get_rect()

        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)

        boundery_hit=False


        if self.rect.left <= 0 or self.rect.right >= 400:
            self.velocity[0] = -self.velocity[0]
            boundery_hit=True

        if self.rect.top <= 0 or self.rect.bottom >= 300:
            self.velocity[1]= -self.velocity[1]
            boundery_hit= True

        if boundery_hit:
            pygame.event.post(pygame.event.Event(spritecolchangeeven))
            pygame.event.post(pygame.event.Event(backgroundcolorchangeeve))

    def change_color(self):
        self.image.fill(random.choice([Yellow,red,lightgreen,cyan,orange]))

    @staticmethod
    def change_background_color():
        global bg_color
        bg_color = random.choice([Blue,lightblue,darkbl])
        

all_sprite_list= pygame.sprite.Group()

spl=Sprite(red,20,30)

spl.rect.x=random.randint(0,300)
spl.rect.y=random.randint(0,300)

all_sprite_list.add(spl)

screen=pygame.display.set_mode((400,400))

pygame.display.set_caption("Colourful bounce")

bg_color=Blue
screen.fill(bg_color)

running=False
exit=False

clock=pygame.time.Clock()

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=True
            exit=True

        elif event.type ==spritecolchangeeven:
            spl.change_color()
        elif event.type == backgroundcolorchangeeve:
            Sprite.change_background_color()

    all_sprite_list.update()

    screen.fill(bg_color)

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
    


