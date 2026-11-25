import pygame

def main():
    pygame.init()
    screen_width=500
    screen_height=500
    screen= pygame.display.set_mode((screen_width,screen_height))

    pygame.display.set_caption("Colour changing sprite")

    colors = {
        'red':pygame.Color('red'),
        'blue':pygame.Color('blue'),
        'green':pygame.Color('green'),
        'yellow':pygame.Color('yellow'),
        'purple':pygame.Color('purple')
    }

    currentcolor=colors['blue']

    x,y=30,30
    sprite_width, sprite_height= 50,50

    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True


        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -=2
        if pressed[pygame.K_RIGHT]: x += 2
        if pressed[pygame.K_UP]: y -= 2
        if pressed[pygame.K_DOWN]: y +=2

        x=min(max(0,x),screen_width - sprite_width)
        y=min(max(0,y),screen_height - screen_height)

        if x == 0: currentcolor == colors['purple']
        elif x ==screen_width- sprite_width: currentcolor = colors['green']
        elif y ==0 : currentcolor = colors['yellow']
        elif y == screen_height - sprite_height:
            currentcolor= colors['red']

        else:
            currentcolor = colors['blue']

        screen.fill((0,0,0))


        pygame.draw.rect(screen,currentcolor,(x,y,sprite_width,sprite_height))
        pygame.display.flip()
        clock.tick(40)

if __name__ == "__main__":
    main()