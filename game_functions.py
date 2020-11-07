import sys
from pygame import *


def check_events():
    for i in event.get():
        if i.type == QUIT:
            sys.exit()


def update_screen(settings, screen, ship):
    '''Обновляет изображение на экране и отображает новый экран'''
    screen.fill(settings.bg_color)
    ship.blitme()

    # отображаю последний прорисованный экран
    display.flip()