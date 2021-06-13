import pygame

class Enemy (pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.health = 50
        self.maxHealth = 100
        self.attack = 50
        self.image = pygame.image.load('pictures/enemy/enemy.png')
        self.image = pygame.transform.scale(self.image, (200, 250))
        self.rect = self.image.get_rect()
        self.rect.x = 910
        self.rect.y = 0
        self.velocity = 10

    def Damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.Remove()


    def UpdateHealthBar(self, surface):

        pygame.draw.rect(surface, (160, 68, 4), [self.rect.x + 50, self.rect.y - 10, self.maxHealth, 8])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y - 10, self.health, 8])

    def Remove(self):
        self.game.allEnemies.remove()


    def Falling(self):
        if not self.game.CheckCollision(self, self.game.allPlayers):
            self.rect.y += self.velocity
        else:
            self.game.player.Damage(self.attack)