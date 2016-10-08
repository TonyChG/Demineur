#!python3
# -*- coding: utf-8 -*-

from random import randint

BOMBS  = "B"
PLAYED = " "

WIN  = 0
LOSE = 1

class MineSweeper:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght
        self.nb_bombs = (self.width*self.lenght)//10
        self.pos_bombs = {}
        self.pos_flags = {}
        self.pos_played = {}

        self.place_bombs()

    def place_bombs(self):
        x = randint(0, self.width-1)
        y = randint(0, self.lenght-1)
        for i in range(self.nb_bombs):
            while (y, x) in self.pos_bombs:
                x = randint(0, self.width-1)
                y = randint(0, self.lenght-1)
            self.pos_bombs[(y, x)] = BOMBS

    def display(self):
        for j in range(self.lenght):
            for i in range(self.width):
                if (j, i) in self.pos_bombs:
                    print(BOMBS, end=" ")
                elif (j, i) in self.pos_played:
                    print(PLAYED, end=" ")
                else:
                    print("*", end=" ")
            print()

    def getBombs(self, x, y):
        count = 0
        for j in range(-1, 2):
            for i in range(-1, 2):
                if (y+j, x+i) in self.pos_bombs:
                    count += 1
        return count

    def play(self, x, y):
        self.pos_played[(y, x)] = PLAYED
        if len(self.pos_played) == self.width*self.lenght-self.nb_bombs:
            return WIN
        if (y, x) in self.pos_bombs:
            return LOSE

    def open_line(self, x, y):
        i = x
        while self.getBombs(i-1, y) == 0 and i < self.width:
            self.pos_played[(y, i)] = PLAYED
            i += 1
        i = x
        while self.getBombs(i+1, y) == 0 and i >= 0:
            self.pos_played[(y, i)] = PLAYED
            i -= 1

    def open_adj_null(self, x, y):
        i = x
        j = y
        while self.getBombs(i, j-1) == 0 and j < self.lenght:
            self.pos_played[(y, i)] = PLAYED
            self.open_line(i, j)
            j += 1
        j = y
        while self.getBombs(i, j+1) == 0 and j >= 0:
            self.pos_played[(y, i)] = PLAYED
            self.open_line(i, j)
            j -= 1