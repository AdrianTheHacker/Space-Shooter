from random import randint
import pygame

window = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(window)
tileSize = 50

fps = 10
score = 1
ded = False


def getRandX():
    randX = randint(0, int(WIDTH / tileSize)) * tileSize
    return randX


def getRandY():
    randY = randint(0, int(HEIGHT / tileSize)) * tileSize
    return randY


red = (255, 0, 0)
green = (0, 255, 0)

grey = (96, 96, 96)
black = (0, 0, 0)
lightBlue = (0, 255, 255)

enemyGroup = pygame.sprite.Group()
playerSingle = pygame.sprite.GroupSingle()
