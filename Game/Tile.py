import pygame as py
py.init()

class Tile:
    def __init__(self, x, y, h):
        self.font = py.font.Font("font.TTF", 25)
        self.x = x
        self.y = y
        self.w = 100
        self.h = 100
        self.num = h
        self.home = h
        self.id = self.font.render(str(self.home), True, (255,255,255))
        self.rect = py.Rect(self.x, self.y, 100, 100)
        self.center = self.rect.center
    def update(self):
        self.id = self.font.render(str(self.num), True, (255, 255, 255))
        self.rect = py.Rect(self.x, self.y, 100, 100)




