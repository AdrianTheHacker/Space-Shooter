import pygame

window = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(window)
tileSize = 50

red = (255, 0, 0)

grey = (96, 96, 96)
black = (0, 0, 0)
lightBlue = (0, 255, 255)

enemyGroup = pygame.sprite.Group()
playerSingle = pygame.sprite.GroupSingle()