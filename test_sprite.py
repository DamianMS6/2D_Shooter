import pygame as py
import sys


class Crosshair(py.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y,color):
        super().__init__()
        self.image = py.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


crosshair = Crosshair(50,50,100,100,(255,255,255))
crosshair_group = py.sprite.Group()
crosshair_group.add(crosshair)


py.init()
clock = py.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = py.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

        crosshair_group.draw(screen)

        py.display.update()
        clock.tick(60)
