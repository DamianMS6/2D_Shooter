import pygame as py
import bullet

class Player(py.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__()
        self.image = py.Surface((20,20))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

    def movement(self,bullet_group):
        reset_time = 386
        keys = py.key.get_pressed()
        if keys[py.K_w]:
            self.rect.y -= 2
        if keys[py.K_s]:
            self.rect.y += 2
        if keys[py.K_a]:
            self.rect.x -= 2
        if keys[py.K_d]:
            self.rect.x += 2
        current_time = py.time.get_ticks()
        if current_time - reset_time > 2000:
            print('This prints every few seconds')
            if keys[py.K_RIGHT]:
                print('pressed')
                bullet_group.add(Player.create_bullet(self))
            reset_time = current_time

    def create_bullet(self):
        return bullet.Bullet(self.rect.x, self.rect.y)







