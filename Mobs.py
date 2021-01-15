import pygame
from pygame.sprite import Sprite
from random import *
x = y = 0
mob_image = pygame.image.load('pngflow.com (2).png')
class Mob(Sprite):
    def __init__(self):
        global x, y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(mob_image, (70, 60))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 50 + x
        self.rect.y = 50 + y
        x = x + 100
        if x > 1350:
            x = 0
            y = y + 50
        if y >= 400:
            y = 0



