import pygame

from Entities.GameObjects import GameObject


class Enemy(GameObject):
    def __init__(self, surface, colour, width, height, position):
        super().__init__(surface, colour, width, height, position)
        self.direction = 'U'
