import pygame

import Settings
from Level_Creator.Level import Level
from Settings import screen, black

pygame.init()

testLevel = Level(screen, 2, 4)


def main():
    while not Settings.ded:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                Settings.ded = True

        screen.fill(black)
        testLevel.run()

        pygame.time.Clock().tick(10)
        pygame.display.flip()


if __name__ == "__main__":
    main()
