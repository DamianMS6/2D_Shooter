import pygame as py
import player as Player

class Bullet(py.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = py.Surface((10,10))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

    def update(self):
        self.rect.x += 5


