import pygame as py
import player as Player

class Bullet(Player):
    def __init__(self):
        super().__init__(x_pos)
        super().__init__(y_pos)

    def draw_bullet(self,screen):
        self.bullet = py.Rect(self.x_pos, self.y_pos)
        py.draw.rect(screen, 'brown1', self.bullet)

    def update(self):
        keys = py.key.get_pressed()
        if keys[py.K_UP]:
            draw_bullet(screen)





