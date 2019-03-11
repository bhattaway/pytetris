import pygame
import tile
import gameobject
import grid
import block

def main():
    print("HELLO WORLD!!!")
    pygame.init()

    screen = pygame.display.set_mode((800,900))

    running = True

    #init clock

    clk = pygame.time.Clock()

    gamestate = 0

    #gamestates


    objects = []

    TESTSTATE = 1
    
    #teststates
    SIMPLEBLOCKTEST = 1

    if TESTSTATE == 1:
        objects.append(block.Block(blocktype='i', TILESIZE=30, x=0, y=0))
        objects.append(block.Block(blocktype='o', TILESIZE=30, x=0, y=100))
        objects.append(block.Block(blocktype='s', TILESIZE=30, x=0, y=250))
        objects.append(block.Block(blocktype='z', TILESIZE=30, x=0, y=400))
        objects.append(block.Block(blocktype='l', TILESIZE=30, x=300, y=0))
        objects.append(block.Block(blocktype='j', TILESIZE=30, x=300, y=200))
        objects.append(block.Block(blocktype='t', TILESIZE=30, x=300, y=400))

    print(objects[0])


    
    newgrid = grid.Grid()

    newgrid.add_tile(objects[0].tiles[0], 1, 1)

    #print(newgrid.__repr__())

    while(running):
        if gamestate == 0:
            pass

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            print("pressing a")
            #dropspeed = softdrop
        else:
            pass
            #dropspeed = standarddrop

        screen.lock()

        '''
        for o in objects:
            o.draw(screen)
        '''
        newgrid.draw(screen)

        pygame.display.flip()
        screen.unlock()

        if keys[pygame.K_ESCAPE]:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #run at 60fps
        clk.tick(60)

if __name__ == "__main__":
    #random.seed(3)
    main()
