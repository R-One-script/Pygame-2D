import pygame

class CometFallEvent:
    def __init__(self):
        self.percent = 0

    def AddPercent(self):
        self.percent += 1

    def UpdateBar(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height(), surface.get_width(), 10])
        pygame.draw.rect(surface, (187, 11, 11), [0, surface.get_height(), (surface.get_width() / 100) * self.percent, 10])