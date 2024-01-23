import pygame as py
import bullet

class Player(py.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__()
        self.image = py.Surface((20,20))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    def movement(self):
        keys = py.key.get_pressed()
        if keys[py.K_w]:
            self.rect.y -= 2
        if keys[py.K_s]:
            self.rect.y += 2
        if keys[py.K_a]:
            self.rect.x -= 2
        if keys[py.K_d]:
            self.rect.x += 2

    def create_bullet(self):
        return bullet.Bullet(self.rect.x, self.rect.y)







