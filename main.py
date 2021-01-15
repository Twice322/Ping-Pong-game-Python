import pygame
from random import *
from pygame.sprite import Sprite
import time
pygame.init()
HEIGHT = 1500
WIDTH = 900
FPS = 60
dy = dx = 10
x = y = i = 0
mob_image = pygame.image.load('pngflow.com (2).png')
ball_image = pygame.image.load('unchecked-circle.png')
hp_image = pygame.image.load('pngflow.com (3).png')
screen = pygame.display.set_mode((HEIGHT, WIDTH), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
background = pygame.image.load('look.com.ua-62848.jpg').convert()
background_rect = background.get_rect()
screen.blit(background, [0, 0])
start = True
game_over = False
start_game = False
clock = pygame.time.Clock()
font_name = pygame.font.match_font('arial')
with open('max_score.txt', 'r') as f:
    max_score = f.readline()


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
            self.rect = pygame.Rect(randrange(200, 1000), 450, 30, 35)
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
        self.rect[1] += int(dy)
        if self.dic_change:
            self.rect[0] += int(dx)
        if self.lives == 0:
            global game_over
            game_over = True

    def draw_lives(self, surf,x ,y ):
        for i in range(self.lives):
            x = x + 60
            surf.blit(pygame.transform.scale(hp_image, (50, 50)), [x, y])


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


class Paddle(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 30))
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(575, 800, 150, 30)

    def update(self):
        if -15 < pygame.mouse.get_pos()[0] < 1375:
            self.rect[0] = pygame.mouse.get_pos()[0]


class Button():

    def __init__(self, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(font_name, 43)

        # Build the button's rect object, and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message only needs to be prepped once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


ball = Ball()
paddle = Paddle()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites.add(ball)
all_sprites.add(paddle)
play_button = Button(screen, "Play")


def create_mobs():
    for _ in range(112):
        m = Mob()
        all_sprites.add(m)
        enemies.add(m)


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    surf.blit(text_surf, (x, y))


def acceleration(score):
    global dx, dy, i
    if score >= 10000+i:
        dx = dx * 1.25
        dy = dy * 1.25
        i += 10000
        return int(dx), int(dy)


def show_screen():
    draw_text(screen, "Game over!", 100, HEIGHT // 2 - 250, WIDTH // 2 - 100)
    pygame.display.flip()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        break


def check():
    global start_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint((mouse_x, mouse_y)):
                start_game = True
                pygame.mouse.set_visible(False)


def main():
    global game_over, all_sprites, enemies, ball, paddle, max_score
    score = 0
    play_button.draw_button()
    create_mobs()
    pygame.display.update()
    while start:
        check()
        pygame.display.update()
        if start_game:
            if game_over:
                show_screen()
                game_over = False
                ball = Ball()
                paddle = Paddle()
                all_sprites = pygame.sprite.Group()
                enemies = pygame.sprite.Group()
                all_sprites.add(ball)
                all_sprites.add(paddle)
                create_mobs()
                if score > int(max_score):
                    with open('max_score.txt', 'w') as f:
                        f.write(str(score))
                        max_score = score
                score = 0
                time.sleep(5)
            clock.tick(FPS)
            all_sprites.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            hits = pygame.sprite.spritecollide(ball, enemies, True)
            for hit in hits:
                score += 50
                m = Mob()
                all_sprites.add(m)
                enemies.add(m)
            acceleration(score)
            screen.fill((0, 0, 0))
            screen.blit(background, [0,0])
            all_sprites.draw(screen)
            ball.draw_lives(screen, -50, 830)
            draw_text(screen, str(score), 24, 725, 10)
            draw_text(screen, f'MAX SCORE: {max_score}', 24, 1250, 10)
            pygame.display.flip()


main()
