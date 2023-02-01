import pygame as py
import sys
import random
from pygame import QUIT
from Tile import Tile

py.init()

WIDTH = 500
HEIGHT = 500
WIN = py.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
board = []
move = 0
moveRect = py.Rect(0,0,50,50)

font = py.font.Font("font.TTF", 25)
def tileMaker(board):
    tempx = 100
    tempy = 100
    home = 0
    for i in range(9):
        board.append(Tile(tempx, tempy, home))
        home +=1
        tempx += 100
        if (i + 1) % 3 == 0:
            tempy += 100
            tempx = 100

def shuffle(board):
    for i in range(1000):
        randDir = random.randint(1,4)
        if randDir == 1:
            tileSwap(board, "up")
        elif randDir == 2:
            tileSwap(board, "down")
        elif randDir == 3:
            tileSwap(board, "left")
        elif randDir == 4:
            tileSwap(board, "right")
def findZero(board):
    for i in range(len(board)):
        if board[i].num == 0:
            zero = i
            print(zero)
            return zero
def tileSwap(board, dir):
    global move
    print("Enter tile Swap")
    zero = findZero(board)
    if dir == "up" and zero -3 >= 0 :
                print("swap up")
                board[zero].num = board[zero - 3].num
                board[zero - 3].num = 0
                move += 1

                return
    elif dir == "down" and zero + 3 <= 8:
                print("swap down")
                board[zero].num = board[zero + 3].num
                board[zero + 3].num = 0
                move += 1
                return
    elif dir == "left" and zero -1 >= 0 and board[zero].x != 100:
                print("swap down")
                board[zero].num = board[zero -1].num
                board[zero - 1].num = 0
                move += 1
                return
    elif dir == "right" and zero + 1 <= 8 and board[zero].x != 300:
                print("swap down")
                board[zero].num = board[zero + 1].num
                board[zero + 1].num = 0
                move += 1
                return

def winCheck(board):
    for tile in board:
        if tile.home != tile.num:
            return False
    return True

first = True
tileMaker(board)
clock = py.time.Clock()

while True:
    clock.tick(60)
    if first:
        shuffle(board)
        move = 0
        first = False
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                tileSwap(board, "up")

            elif event.key == py.K_s:
                tileSwap(board, "down")

            elif event.key == py.K_a:
                tileSwap(board, "left")
            elif event.key == py.K_d:
                tileSwap(board, "right")


    keys = py.key.get_pressed()
    moveTxt = font.render(str(move), True, (255, 255, 255))
    if winCheck(board):
        WIN.fill(GREEN)
    else:
        WIN.fill(BLACK)
    for tile in board:
        tile.update()
        py.draw.rect(WIN, WHITE, tile.rect, 2)
        if tile.num != 0:
            WIN.blit(tile.id, tile.center)
    WIN.blit(moveTxt, moveRect)
    py.display.update()

