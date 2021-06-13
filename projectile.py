import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super(Projectile, self).__init__()
        self.velocity = 50
        self.player = player
        self.image = pygame.image.load('pictures/projectile/bubble.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect.x = player.rect.x + 50
        self.rect.y = player.rect.y - 30
        self.originImage = self.image
        self.angle = 0

    def Rotate(self):
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.originImage, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def Remove(self):
        self.player.allProjectiles.remove(self)

    def Move(self):
        self.rect.y -= self.velocity
        self.Rotate()

        for enemy in self.player.game.CheckCollision(self, self.player.game.allEnemies):
            self.Remove()
            enemy.Damage(self.player.attack)

        if self.rect.y < 0:
            self.Remove()
