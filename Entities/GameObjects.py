import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, surface, colour, width, height, position):
        super().__init__()

        self.surface = surface

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.get_rect(topleft=position)

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def update(self):
        self.draw()
