from pygame import Rect
from constants import *

class Cell(Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        
        self.row = self.y // CELL_SIZE
        self.col = self.x // CELL_SIZE

        self.alive = False
        self.neighbours = self.find_neighbours()
        self.alive_neighbours = 0

    def update(self):
        self.alive = not self.alive

    def reset_neighbours(self):
        self.alive_neighbours = 0

    def find_neighbours(self):

        valid_neighbours = []

        neighbours_pos = [

            (self.row, self.col + 1),
            (self.row, self.col - 1),
            (self.row + 1, self.col),
            (self.row + 1, self.col + 1),
            (self.row + 1, self.col - 1),
            (self.row - 1, self.col),
            (self.row - 1, self.col + 1),
            (self.row -1, self.col - 1),
        ]

        for pos in neighbours_pos:
            if Cell.in_range(pos):
                valid_neighbours.append(pos)

        return valid_neighbours


    @staticmethod
    def in_range(pos):
        if (pos[0] < 0 or pos[0] > ROWS - 1) or (pos[1] < 0 or pos[1] > COLS - 1):
            return False
        
        return True
    
