from Level_Creator.Level import Level
from main import Settings

import pygame
pygame.init()

testLevel = Level(Settings.screen, 2, 4)


def main():
    while not Settings.ded:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.ded = True

        Settings.screen.fill(Settings.black)
        testLevel.run()

        print(Settings.ded)
        print(Settings.score)

        pygame.time.Clock().tick(10)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
