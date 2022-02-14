import pygame

from Level_Creator.Level import level
from Settings import screen, black

pygame.init()

ded = False


def main():
    global ded

    while not ded:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                ded = True

        screen.fill(black)
        level.run()

        pygame.time.Clock().tick(10)
        pygame.display.flip()


if __name__ == "__main__":
    main()
