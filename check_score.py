import pygame
import os
from pygame.sprite import Sprite
from paddle import Paddle
from random import *


def check(score, dx, dy):
    if score > 10000:
        dx = dx + 10
        dy = dy + 10
        return (dx, dy)