from Entities.Enemy import Enemy
from Settings import playerSingle


class LootEnemy(Enemy):
    def __init__(self, surface, colour, width, height, position, speed):
        super().__init__(surface, colour, width, height, position, speed)

    def onShot(self):
        for player in playerSingle:
            player.ammo = player.maxAmmo
