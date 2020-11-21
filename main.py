from pygame import *
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    init()
    game_settings = Settings()
    s = display.set_mode((game_settings.screen_width, game_settings.screen_height))
    # создание корабля
    ship = Ship(s)
    # группа для хранения пуль
    bullets = Group()

    display.set_caption('Battle ship')

    while True:
        gf.check_events(ship, s, bullets)
        gf.update_screen(game_settings, s, ship, bullets)
        ship.update()
        bullets.update()


if __name__ == '__main__':
    run_game()