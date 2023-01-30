import pygame as py
py.init()

class Tile:

    def __init__(self, x, y, n):
        text = py.font.Font("font.TTF", 25)
        self.x = x
        self.y = y
        self.w = 100
        self.h = 100
        self.n = n
        self.id = text.render(str(self.n), True, (255,255,255))
        self.rect = py.Rect(self.x, self.y, 100, 100)
        self.center = self.rect.center





