import sys
from pygame import *
from settings import Settings
from ship import Ship


def run_game():
    init()
    game_settings = Settings()
    s = display.set_mode((game_settings.screen_width, game_settings.screen_height))
    # создание корабля
    ship = Ship(s)

    display.set_caption('Battle ship')
    bg = game_settings.bg_color

    while True:
        s.fill(bg)
        ship.blitme()
        for i in event.get():
            if i.type == QUIT:
                sys.exit()

        display.flip()


if __name__ == '__main__':
    run_game()