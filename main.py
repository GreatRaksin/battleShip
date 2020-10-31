from pygame import *
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    init()
    game_settings = Settings()
    s = display.set_mode((game_settings.screen_width, game_settings.screen_height))
    # создание корабля
    ship = Ship(s)

    display.set_caption('Battle ship')
    bg = game_settings.bg_color

    while True:
        gf.check_events()
        s.fill(bg)
        ship.blitme()

        display.flip()


if __name__ == '__main__':
    run_game()