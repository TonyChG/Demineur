#!python3
# -*- coding: utf-8 -*-

import pygame
from time import sleep
from pygame.locals import *
from game import *

BOMBS       = "B"
PLAYED      = " "

WIN         = 0
LOSE        = 1

IMG_SIZE    = 20
UNPLAYED    = "unplayed"
MOUSE       = "mouse"
FLAGS       = "flags"

PRINT_BOMBS = 1

class Game:
    def __init__(self, width=10, lenght=10):
        self.grid = MineSweeper(width, lenght)
        self.width = width * IMG_SIZE
        self.lenght = lenght * IMG_SIZE
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.lenght))
        pygame.display.set_caption("Demineur " + str(width) + "x" + str(lenght))
        self.stopGame = True
        self.img = {}
        self.img[0] = pygame.image.load("./Sprites/0.png").convert()
        self.img[1] = pygame.image.load("./Sprites/1.png").convert()
        self.img[2] = pygame.image.load("./Sprites/2.png").convert()
        self.img[3] = pygame.image.load("./Sprites/3.png").convert()
        self.img[4] = pygame.image.load("./Sprites/4.png").convert()
        self.img[5] = pygame.image.load("./Sprites/5.png").convert()
        self.img[6] = pygame.image.load("./Sprites/6.png").convert()
        self.img[7] = pygame.image.load("./Sprites/7.png").convert()
        self.img[8] = pygame.image.load("./Sprites/8.png").convert()
        self.img[BOMBS] = pygame.image.load("./Sprites/bomb_box.png").convert()
        self.img[MOUSE] = pygame.image.load("./Sprites/mouse_box.jpg").convert()
        self.img[FLAGS] = pygame.image.load("./Sprites/flags_box.png").convert()
        self.img[UNPLAYED] = pygame.image.load("./Sprites/unplayed_box.png").convert()
    def display(self, opts=0):
        for j in range(0, self.width, IMG_SIZE):
            for i in range(0, self.lenght, IMG_SIZE):
                if not (j//IMG_SIZE, i//IMG_SIZE) in self.grid.pos_bombs and (j//IMG_SIZE, i//IMG_SIZE) in self.grid.pos_played:
                    self.window.blit(self.img[self.grid.getBombs(i//IMG_SIZE, j//IMG_SIZE)], (j, i))
                elif (j//IMG_SIZE, i//IMG_SIZE) in self.grid.pos_bombs and opts == PRINT_BOMBS:
                    self.window.blit(self.img[BOMBS], (j, i))
                elif (j//IMG_SIZE, i//IMG_SIZE) in self.grid.pos_flags:
                    self.window.blit(self.img[FLAGS], (j, i))
                else:
                    self.window.blit(self.img[UNPLAYED], (j, i))
        pygame.display.flip()
    def mainloop(self):
        self.display()
        last_x_play = 0
        last_y_play = 0
        while self.stopGame:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stopGame = False
                if event.type == MOUSEMOTION:
                    self.display()
                    if not (event.pos[1]//IMG_SIZE, event.pos[0]//IMG_SIZE) in self.grid.pos_played:
                        self.window.blit(self.img[MOUSE], ((event.pos[0]//IMG_SIZE)*IMG_SIZE,
                            (event.pos[1]//IMG_SIZE)*IMG_SIZE))
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    last_x_play = event.pos[1]//IMG_SIZE
                    last_y_play = event.pos[0]//IMG_SIZE
                    if self.grid.play(event.pos[1]//IMG_SIZE, event.pos[0]//IMG_SIZE) == LOSE:
                        self.stopGame = False
                    else:
                        if self.grid.getBombs(last_x_play, last_y_play) == 0:
                            self.grid.open_adj_null(last_x_play, last_y_play)
                    self.display()
                if event.type == MOUSEBUTTONUP and event.button == 3:
                    if not (event.pos[0]//IMG_SIZE, event.pos[1]//IMG_SIZE) in self.grid.pos_flags:
                        self.grid.pos_flags[(event.pos[0]//IMG_SIZE, event.pos[1]//IMG_SIZE)] = FLAGS
                    else:
                        del(self.grid.pos_flags[(event.pos[0]//IMG_SIZE, event.pos[1]//IMG_SIZE)])
                    self.display()
            pygame.display.flip()
        if (last_y_play, last_x_play) in self.grid.pos_bombs:
            self.display(opts=PRINT_BOMBS)
            sleep(2)

if __name__ == "__main__":
    game = Game(50, 50)
    game.mainloop()