import pygame

pygame.init()

ded = False

window = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(window)

tileSize = 50

black = (0, 0, 0)
lightBlue = (0, 255, 255)


class GameObject(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, position):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.get_rect(topleft=position)

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.draw()


class ShootyMcShooterFace(GameObject):
    def __init__(self, colour, width, height, position):
        super().__init__(colour, width, height, position)
        self.direction = 'U'

    def move(self):
        if self.direction == 'U':
            self.rect.y -= tileSize

        elif self.direction == 'D':
            self.rect.y += tileSize

    def collision(self):
        if self.rect.y == 0:
            self.direction = 'D'

        elif self.rect.y == HEIGHT - tileSize:
            self.direction = 'U'

    def update(self):
        self.draw()
        self.move()
        self.collision()


player = ShootyMcShooterFace(lightBlue, tileSize, tileSize, (50, 50))
playerGS = pygame.sprite.GroupSingle(player)

while not ded:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            ded = True

    screen.fill(black)
    playerGS.update()

    pygame.time.Clock().tick(10)
    pygame.display.flip()
