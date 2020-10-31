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

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
