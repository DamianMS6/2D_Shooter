import pygame as py
import sys
import player

py.init()
clock = py.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = py.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
player = player.Player()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()

    player.movement()
    player.display_player(screen)
    py.display.update()
    screen.fill((0,0,0))
    clock.tick(60)
    
