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


    blocks = []

    blocks.append(block.Block(blocktype='i', x=0, y=0))
    blocks.append(block.Block(blocktype='o', x=0, y=100))
    blocks.append(block.Block(blocktype='s', x=0, y=250))
    blocks.append(block.Block(blocktype='z', x=0, y=400))
    blocks.append(block.Block(blocktype='l', x=300, y=0))
    blocks.append(block.Block(blocktype='j', x=300, y=200))
    blocks.append(block.Block(blocktype='t', x=300, y=400))

    print(blocks[0])


    
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

        for b in blocks:
            b.draw(screen)

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
