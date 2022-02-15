from Entities.GameObjects import GameObject
from Entities.Enemy import Enemy
from Entities.LootEnemy import LootEnemy

from main.Settings import *


class Player(GameObject):
    def __init__(self, surface, colour, width, height, position, maxAmmo):
        super().__init__(surface, colour, width, height, position)

        self.maxAmmo = maxAmmo

        self.ammo = self.maxAmmo
        self.direction = 'U'

        self.bulletGroup = pygame.sprite.Group()

    def move(self):
        if self.direction == 'U':
            self.rect.y -= tileSize

        elif self.direction == 'D':
            self.rect.y += tileSize

    def movePattern(self):
        if self.rect.y == 0:
            self.direction = 'D'

        elif self.rect.y == HEIGHT - tileSize:
            self.direction = 'U'

    def shoot(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.ammo > 0:
            self.bullet = self.PlayerBullet(self.surface, grey, tileSize, tileSize, (self.rect.x, self.rect.y))
            self.bulletGroup.add(self.bullet)

            self.ammo -= 1

    def update(self):
        self.draw()
        self.move()
        self.movePattern()
        self.shoot()

        self.bulletGroup.update()

    class PlayerBullet(GameObject):
        def __init__(self, surface, colour, width, height, position):
            super().__init__(surface, colour, width, height, position)

        def move(self):
            self.rect.x += tileSize

        def checkCollision(self):
            """
            for every rect in Enemy sprite group:
                if bullet rect collides with enemy rect:
                    enemy blows up and you can shoot again
            """
            global score
            for entity in enemyGroup.sprites():
                if self.rect.colliderect(entity.rect):
                    print("Bullet hit Enemy")

                    score += 1

                    entity.onShot()
                    entity.kill()

                    if type(entity) is Enemy:
                        enemy = Enemy(self.surface,
                                      red,
                                      tileSize, tileSize,
                                      (WIDTH + tileSize * 2, getRandY()), 2)
                        enemyGroup.add(enemy)

                    elif type(entity) is LootEnemy:
                        lootEnemy = LootEnemy(self.surface,
                                              green,
                                              tileSize, tileSize,
                                              (WIDTH + tileSize * 2, getRandY()), 2)
                        enemyGroup.add(lootEnemy)

                    self.kill()

        def update(self):
            self.draw()
            self.move()
            self.checkCollision()
