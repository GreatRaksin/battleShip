from pygame import *
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = Rect(0, 0, 3, 15)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = 60, 60, 60
        self.speed = 1

    def update(self):
        """Перемещает пулю вверх по экрану"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран"""
        draw.rect(self.screen, self.color, self.rect)