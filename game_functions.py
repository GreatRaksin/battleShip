import sys
from pygame import *


def check_events(ship):
    for i in event.get():
        if i.type == QUIT:
            sys.exit()
        elif i.type == KEYDOWN:
            if i.key == K_RIGHT:
                ship.moving_right = True
            elif i.key == K_LEFT:
                ship.moving_left = True
        elif i.type == KEYUP:
            if i.key == K_RIGHT:
                ship.moving_right = False
            elif i.key == K_LEFT:
                ship.moving_left = False


def update_screen(settings, screen, ship):
    '''Обновляет изображение на экране и отображает новый экран'''
    screen.fill(settings.bg_color)
    ship.blitme()

    # отображаю последний прорисованный экран
    display.flip()