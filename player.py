import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 10
        self.velocity = 10
        self.image = pygame.image.load('pictures/character/characterRight.png')
        self.rect = self.image.get_rect()
        self.rect.x = 750
        self.rect.y = 840
        self.allProjectiles = pygame.sprite.Group()

    def Damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.GameOver()

    def UpdateHealthBar(self, surface):

        pygame.draw.rect(surface, (160, 68, 4), [self.rect.x + 80, self.rect.y, self.maxHealth, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 80, self.rect.y, self.health, 10])

    def lauchProjectile(self):
        self.allProjectiles.add(Projectile(self))

    def moveRight(self):
        if not self.game.CheckCollision(self, self.game.allEnemies):
            self.rect.x += self.velocity

    def moveLeft(self):
        if not self.game.CheckCollision(self, self.game.allEnemies):
            self.rect.x -= self.velocity