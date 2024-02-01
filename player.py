import pygame as py
import bullet

class Player(py.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT):
        super().__init__()
        self.image = py.Surface((20,20))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        self.reset_time = 0

    def movement(self,bullet_group):
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
        if current_time - self.reset_time > 800:
            print('This prints every few seconds', py.time.get_ticks())
            if keys[py.K_RIGHT]:
                self.direction = "RIGHT"
                print('pressed')
                self.shoot_bullet(bullet_group, self.direction)

            self.reset_time = current_time

    def create_bullet(self):
        bullet_obj = bullet.Bullet(self.rect.x, self.rect.y)
        return bullet_obj


    def shoot_bullet(self, bullet_group,dir):
        bullet_group.update(dir)
        return bullet_group.add(Player.create_bullet(self))







