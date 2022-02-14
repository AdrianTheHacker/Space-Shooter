from Level_Creator.GameMaps import testLevel
from Settings import *
from Entities.Enemy import Enemy
from Entities.Player import Player

# Credits: https://www.youtube.com/watch?v=YWN8GcmJ-jA
from Settings import screen, enemyGroup, HEIGHT, tileSize


class Level:
    def __init__(self, levelData, surface):
        self.surface = surface
        self.levelSetup(levelData)

    def levelSetup(self, layout):
        for rowIndex, row in enumerate(layout):
            for cellIndex, cell in enumerate(row):
                x = cellIndex * tileSize
                y = rowIndex * tileSize

                if cell == 'E':
                    enemy = Enemy(screen, red, tileSize, tileSize, (x, y))
                    enemyGroup.add(enemy)

                if cell == 'P':
                    player = Player(screen, lightBlue, tileSize, tileSize, (x, y))
                    playerSingle.add(player)



    def run(self):
        enemyGroup.update()
        playerSingle.update()


level = Level(testLevel, screen)


