import sys
from pygame import *


def check_keydown_events(event, ship):
    if event.key == K_RIGHT:
        ship.moving_right = True
    elif event.key == K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == K_RIGHT:
        ship.moving_right = False
    elif event.key == K_LEFT:
        ship.moving_left = False


def check_events(ship):
    for i in event.get():
        if i.type == QUIT:
            sys.exit()
        elif i.type == KEYDOWN:
            check_keydown_events(i, ship)
        elif i.type == KEYUP:
            check_keyup_events(i, ship)


def update_screen(settings, screen, ship):
    '''Обновляет изображение на экране и отображает новый экран'''
    screen.fill(settings.bg_color)
    ship.blitme()

    # отображаю последний прорисованный экран
    display.flip()
