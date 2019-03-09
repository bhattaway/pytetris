import pygame
import tile
import gameobject
import grid
import block

def main():
    print("HELLO WORLD!!!")
    pygame.init()

    screen = pygame.display.set_mode((800,600))

    running = True

    gamestate = 0

    #gamestates


    o = block.Block(blocktype='o', x=50, y=0)
    i = block.Block(blocktype='i')

    
    newgrid = grid.Grid()

    print(newgrid.__repr__())

    while(running):
        if gamestate == 0:
            pass

        screen.lock()

        '''
        for o in objects:
            o.draw(screen)
        '''
        o.draw(screen)
        i.draw(screen)

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
