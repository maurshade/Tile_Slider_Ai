import pygame as py
import sys
from pygame import QUIT
from Tile import Tile

py.init()

WIDTH = 500
HEIGHT = 500
WIN = py.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE = (255,255,255)
board = []

def tileMaker(board):
    tempx = 100
    tempy = 100
    num = 0
    for i in range(9):
        board.append(Tile(tempx, tempy, num))
        num +=1
        tempx += 100
        if (i + 1) % 3 == 0:
            tempy += 100
            tempx = 100

def tileSwap(board, keys):
    for i in len(board):
        if board[i].n == 0:
            zerox = board[i].x
            zeroy = board[i].y
            zero = i

    if keys[py.K_UP]:
        #Start here


tileMaker(board)

while True:
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()
    keys = py.key.get_pressed()
    tileSwap(board, keys)
    WIN.fill(BLACK)
    for tile in board:
        py.draw.rect(WIN, WHITE, tile.rect, 2)
        WIN.blit(tile.id, tile.center)
    py.display.update()

