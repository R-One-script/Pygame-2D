import pygame
from player import Player
from enemy import Enemy

class Game():
    def __init__(self):

        self.isPlaying = False
        self.allPlayers = pygame.sprite.Group()
        self.player = Player(self)
        self.pressed = {}
        self.allPlayers.add(self.player)
        self.allEnemies = pygame.sprite.Group()
        self.SpawnEnemy()

    def Start(self):
        self.isPlaying = True
        self.SpawnEnemy()

    def GameOver(self):
        self.allEnemies = pygame.sprite.Group()
        self.player.health = self.player.maxHealth
        self.isPlaying = False

    def Update(self, screen):

        screen.blit(self.player.image, (self.player.rect))

        self.player.UpdateHealthBar(screen)

        for projectile in self.player.allProjectiles:
            projectile.Move()

        for enemy in self.allEnemies:
            enemy.Falling()
            enemy.UpdateHealthBar(screen)

        self.player.allProjectiles.draw(screen)

        self.allEnemies.draw(screen)

    def CheckCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def SpawnEnemy(self):
        enemy = Enemy(self)
        self.allEnemies.add(enemy)
