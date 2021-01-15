import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 30))
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(575, 800, 150, 30)

    def update(self):
        if -15 < pygame.mouse.get_pos()[0] < 1375:
            self.rect[0] = pygame.mouse.get_pos()[0]
