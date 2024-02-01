import pygame as py
import sys
import player as ply
import bullet

py.init()
clock = py.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = py.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = ply.Player(SCREEN_WIDTH, SCREEN_HEIGHT)
player_group = py.sprite.Group()
player_group.add(player)

bullet_group = py.sprite.Group()

reset_time = py.time.get_ticks()


while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    player.movement(bullet_group)
    #bullet_group.draw(screen)
    bullet_group.update()
    player_group.draw(screen) # Draws all player sprites in a group on the screen
    py.display.update()
    screen.fill((0,0,0))
    clock.tick(60)
    
