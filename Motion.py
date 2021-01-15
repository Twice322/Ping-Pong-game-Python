import pygame
class Motion():
    def move(self, ball_rect, block_rect, y=None):
        if y is None:
            y = 0
        move = True
        if ball_rect > -40:
            if move:
                ball_rect = pygame.Rect(645 + y, 500, 0, 0)
                y = y + 1
            else:
                ball_rect = pygame.Rect(645 + y, 500, 0, 0)
                y = y - 1
            if ball_rect > block_rect[1] + 30:
                move = False
        else:
            move = False