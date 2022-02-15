from Entities.GameObjects import GameObject
from main import Settings


class Enemy(GameObject):
    def __init__(self, surface, colour, width, height, position, speed):
        super().__init__(surface, colour, width, height, position)

        self.speed = speed

    def move(self):
        self.rect.x -= self.speed

    def onShot(self):
        Settings.score += 1

    def checkCollision(self):
        if self.rect.x < 0:
            Settings.ded = True

    def update(self):
        self.draw()
        self.move()
        self.checkCollision()
