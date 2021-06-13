import random
import sys
import math
import pygame
from game import Game
from enemy import Enemy

pygame.init()




sizeWindow = weigh, height = 1920, 1080
screen = pygame.display.set_mode(sizeWindow)
pygame.display.set_caption("R-One 2D pygame")


gameScreen = pygame.image.load('pictures/screen_game.jpg')

game = Game()

running = True

while running :

    screen.blit(gameScreen, (0, 0))
    banner = pygame.image.load('pictures/banner.png')
    bannerRect = banner.get_rect()

    playButton = pygame.image.load('pictures/playButton.png')
    playButton = pygame.transform.scale(playButton, (1000, 500))
    playButtonRect = playButton.get_rect()
    playButtonRect.x = 450
    playButtonRect.y = 100

    quitButton = pygame.image.load('pictures/quitButton.png')
    quitButton = pygame.transform.scale(quitButton, (1000, 500))
    quitButtonRect = quitButton.get_rect()
    quitButtonRect.x = 450
    quitButtonRect.y = 500



    if game.isPlaying:
        game.Update(screen)

    else:
        screen.blit(banner, (0, 0))
        screen.blit(playButton, (playButtonRect))
        screen.blit(quitButton, (quitButtonRect))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game closed")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key]= False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if playButtonRect.collidepoint(event.pos):
                game.Start()
            elif quitButtonRect.collidepoint(event.pos):
                pygame.quit()

    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width() - 360:
        game.player.moveRight()
        print("moving on the right side")
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.moveLeft()
        print("moving on the left side")
    elif game.pressed.get(pygame.K_SPACE):
        game.player.lauchProjectile()


    pygame.display.flip()

