from Entities.Player import Player
from Entities.LootEnemy import LootEnemy
from Entities.Enemy import Enemy

from main.Settings import *

import pygame


class Level:
    def __init__(self, surface, spawnRate, numOfEnemies):
        self.surface = surface
        self.spawnRate = spawnRate
        self.numOfEnemies = numOfEnemies

        self.enemyGroup = pygame.sprite.Group()

        self.drawLevel()

    def drawLevel(self):
        """
        create and add the player
        adds a new powerup for the number of spawn rate

        for every powerup added, add 5 enemies
        """
        for entity in range(self.spawnRate):
            for enemies in range(self.numOfEnemies):
                enemy = Enemy(self.surface,
                              red,
                              tileSize, tileSize,
                              (WIDTH - tileSize, getRandY()), 5)
                enemyGroup.add(enemy)

            enemy = LootEnemy(self.surface,
                              green,
                              tileSize, tileSize,
                              (WIDTH - tileSize, getRandY()), 5)
            enemyGroup.add(enemy)

        player = Player(self.surface,
                        lightBlue,
                        tileSize, tileSize,
                        (0, tileSize * 2), 5)
        playerSingle.add(player)

    def run(self):
        playerSingle.update()
        enemyGroup.update()
