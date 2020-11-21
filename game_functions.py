import sys
from pygame import *
from bullet import Bullet


def check_keydown_events(event, ship, screen, bullets):
    if event.key == K_RIGHT:
        ship.moving_right = True
    elif event.key == K_LEFT:
        ship.moving_left = True
    elif event.key == K_SPACE:
        # создание пули и включение ее в группу bullets
        new_bullet = Bullet(screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == K_RIGHT:
        ship.moving_right = False
    elif event.key == K_LEFT:
        ship.moving_left = False


def check_events(ship, screen, bullets):
    for i in event.get():
        if i.type == QUIT:
            sys.exit()
        elif i.type == KEYDOWN:
            check_keydown_events(i, ship, screen, bullets)
        elif i.type == KEYUP:
            check_keyup_events(i, ship)


def update_screen(settings, screen, ship, bullets):
    '''Обновляет изображение на экране и отображает новый экран'''
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # отображаю последний прорисованный экран
    display.flip()
