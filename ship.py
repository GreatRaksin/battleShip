from pygame import *


class Ship:
    def __init__(self, screen):
        """Иницилизирует корабль и задает его позицию на экране"""
        self.screen = screen

        # загрузка изображения корабля и получение поля
        self.image = image.load('images/spider.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # каждый новый корабль создается у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 10
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 10



    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
