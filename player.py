import pygame as py

class Player():
    def __init__(self):
        self.x_pos = 400
        self.y_pos = 300


    def display_player(self,screen):
        self.player = py.Rect(self.x_pos,self.y_pos,15,15)
        py.draw.rect(screen, 'aliceblue', self.player)

    def movement(self):
        keys = py.key.get_pressed()
        if keys[py.K_w]:
            self.y_pos -= 1.5
        if keys[py.K_s]:
            self.y_pos += 1.5
        if keys[py.K_a]:
            self.x_pos -= 1.5
        if keys[py.K_d]:
            self.x_pos += 1.5








