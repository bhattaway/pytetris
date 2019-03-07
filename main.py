import pygame
import gameobject

def main():
    pygame.init()

    screen = pygame.display.set_mode((800,600))

    running = True

    gamestate = 0

    #gamestates
    

    while(running):
        if gamestate == 0:
            pass

        screen.lock()

        pygame.draw.rect(screen, (255,255,0), pygame.Rect(100,200,50,75))

        pygame.display.flip()
        screen.unlock()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    #random.seed(3)
    main()
