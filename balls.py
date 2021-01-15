import pygame
import os
from pygame.sprite import Sprite
from paddle import Paddle
from random import *
dy = dx = 10
ball_image = pygame.image.load('unchecked-circle.png')
hp_image = pygame.image.load('pngflow.com (3).png')

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(ball_image, (30, 30))
        self.image.set_colorkey((255, 255, 255))
        self.rect = pygame.Rect(574, 450, 30, 30)
        self.lives = 3
        self.dic_change = False

    def update(self):
        global dx, dy
        if self.rect.bottom > 885:
            self.lives -= 1
            self.rect = pygame.Rect(574, 450, 30, 35)
            self.dic_change = False
        if self.rect.right > 1480:
            dx = -dx
        if self.rect.top < 0:
            dy = -dy
        if self.rect.left < 0:
            dx = -dx
        paddle_rect = pygame.Rect(pygame.mouse.get_pos()[0], 800, 150, 30)
        if paddle_rect.colliderect(self.rect):
            dy = -dy
            self.dic_change = True
        self.rect[1] += dy
        if self.dic_change:
            self.rect[0] += dx

    def draw_lives(self, surf,x ,y ):
        for i in range(self.lives):
            x = x + 60
            surf.blit(pygame.transform.scale(hp_image, (50, 50)), [x, y])









































    #def draw_ball(self, screen, x, y):
        #global dx, dy
        #if self.ball_rect[1] == 885:
            #dy = -dy
        #if self.ball_rect[0] == 1480:
            #dx = -dx
        #if self.ball_rect[1] == 0:
            #dy = -dy
        #if self.ball_rect[0] == 0:
            #dx = -dx
        #if self.ball_rect.colliderect(Paddle.paddle_rect(screen, pygame.mouse.get_pos()[0])):
            #dy = -dy
        #self.ball_rect[0] += dx
        #self.ball_rect[1] += dy
        #pygame.draw.circle(screen, (255, 255, 255), (self.ball_rect[0], self.ball_rect[1]), 15)
