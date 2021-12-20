import sys
import math
from enum import Enum

class Direction(Enum):
    SUD = "S"
    EST = "E"
    NORD = "N"
    OUEST = "O"

class Bender:
    def __init__(self, carte, l, c):
        self.prop = [Direction.SUD, Direction.EST, Direction.NORD, Direction.OUEST]
        self.carte = carte
        self.height = l
        self.width = c
        self.prop_nb = 0
        self.reached_carte = [[list() for _ in range(c)] for _ in range(l)]
        self.t1 = None
        self.t2 = None
        self.x = 0
        self.y = 0
        self.pos_char = []
        self.next_dir = Direction.SUD
        self.next_x = 0
        self.next_y = 0
        self.parcours = []
        self.is_casseur = False
        self.tour = 0
        self.init_pos()

    def init_pos(self):
        for i, ligne in enumerate(carte):
            for j, char in enumerate(ligne):
                if char == "@":
                    self.pos_char = "@"
                    self.y = i
                    self.x = j
                elif char == "T":
                    if self.t1 is None:
                        self.t1 = (i, j)
                    else:
                        self.t2 = (i, j)

    def next_dir_prop(self):
        next_dir = self.prop[self.prop_nb]
        self.prop_nb += 1
        return next_dir

    def have_access(self, y, x):
        return (self.carte[y][x] != "#" and self.carte[y][x] != "X") or (self.carte[y][x] == "X" and self.is_casseur)

    def update_state(self):
        self.pos_char = self.carte[self.y][self.x]
        if self.carte[self.y][self.x] == "X":
            self.carte[self.y][self.x] = " "
            self.reached_carte = [[list() for _ in range(self.width)] for _ in range(self.height)]
        elif self.carte[self.y][self.x] == "T":
            if self.x == self.t1[1] and self.y == self.t1[0]:
                self.x = self.t2[1]
                self.y = self.t2[0]
            else:
                self.x = self.t1[1]
                self.y = self.t1[0]
        elif self.carte[self.y][self.x] == "I":
            self.prop.reverse()
        elif self.carte[self.y][self.x] == "B":
            self.is_casseur = not self.is_casseur
        elif self.carte[self.y][self.x] == "N":
            self.next_dir = Direction.NORD
        elif self.carte[self.y][self.x] == "E":
            self.next_dir = Direction.EST
        elif self.carte[self.y][self.x] == "S":
            self.next_dir = Direction.SUD
        elif self.carte[self.y][self.x] == "W":
            self.next_dir = Direction.OUEST

    def coord_next(self):
        succes = False

        if self.next_dir == Direction.SUD:
            if self.have_access(self.y + 1, self.x):
                self.y += 1
                self.parcours.append("SOUTH")
                succes = True
            else:
                self.next_dir = self.next_dir_prop()
                self.coord_next()
        elif self.next_dir == Direction.EST:
            if self.have_access(self.y, self.x + 1):
                self.x += 1
                self.parcours.append("EAST")
                succes = True
            else:
                self.next_dir = self.next_dir_prop()
                self.coord_next()
        elif self.next_dir == Direction.NORD:
            if self.have_access(self.y - 1, self.x):
                self.y -= 1
                self.parcours.append("NORTH")
                succes = True
            else:
                self.next_dir = self.next_dir_prop()
                self.coord_next()
        elif self.next_dir == Direction.OUEST:
            if self.have_access(self.y, self.x - 1):
                self.x -= 1
                self.parcours.append("WEST")
                succes = True
            else:
                self.next_dir = self.next_dir_prop()
                self.coord_next()

        if succes:
            self.update_state()

    def run(self):
        while self.pos_char != "$":
            self.prop_nb = 0
            self.coord_next()
            self.tour += 1
            if [self.next_dir, self.is_casseur] in self.reached_carte[self.y][self.x]:
                return False
            else:
                self.reached_carte[self.y][self.x].append([self.next_dir, self.is_casseur])

        return True

l, c = [int(i) for i in input().split()]
carte = [[" " for _ in range(c)] for _ in range(l)]
for i in range(l):
    row = input()
    for j, char in enumerate(row):
        carte[i][j] = char

bender = Bender(carte, l, c)
reached = bender.run()

if reached:
    for direc in bender.parcours:
        print(direc)
else:
    print("LOOP")