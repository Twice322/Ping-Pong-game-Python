import pygame
from random import *
pygame.init()
WIDTH = 900
HEIGHT = 1500
FPS = 60
screen = pygame.display.set_mode((HEIGHT, WIDTH))
background = pygame.image.load('spaceground.png').convert()
block_rect = pygame.Rect(575, 800, 150, 30)
block = pygame.draw.rect(screen, (255, 255, 255), block_rect)
ball_rect = pygame.Rect(675, 400, 20, 20)
pygame.display.update()
dx = 1
dy = 1
move = True
start_game = True
x = y = 50
while True:
    screen.blit(background, [0,0])
    pygame.mouse.set_visible(False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION and 0 < pygame.mouse.get_pos()[0] < 1415:
            block_rect = pygame.Rect(pygame.mouse.get_pos()[0], block_rect[1], 150, 30)
    if move:
        ball_rect = pygame.Rect(ball_rect[0]+dx, ball_rect[1]+dy, 20, 15)
        if ball_rect[1] == 885:
            dy = -dy
        if ball_rect[0] == 1480:
            dx = -dx
        if ball_rect[1] == 0:
            dy = - dy
        if ball_rect[0] == 0:
            dx = - dx
        if ball_rect.colliderect(block_rect):
            dy = -dy
    pygame.draw.rect(screen, (255, 255, 255), block_rect)
    pygame.draw.circle(screen, (255, 255, 255), (ball_rect[0], ball_rect[1]), 10)
    pygame.display.update()

