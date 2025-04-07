import pygame
from constants import *
from cell import Cell

class Game:

    def __init__(self):
        self.grid = self.create_cells()
        self.alive_cells = []

    def select_cell(self, surface, row, col):
        cell = self.grid[row][col]

        if cell not in self.alive_cells:
            cell.update()
            self.alive_cells.append(cell)
            pygame.draw.rect(surface, ALIVE_COLOUR, cell)


    def draw_grid(self, surface):
            for row in self.grid:
                for cell in row:
                    if cell.alive == True:
                        pygame.draw.rect(surface, ALIVE_COLOUR, cell)
                    elif cell.alive == False:
                        pygame.draw.rect(surface, CELL_COLOUR, cell, 1)

    def create_cells(self):
        grid = []    
    
        for y in range(0, HEIGHT, CELL_SIZE):
            row = []
            
            for x in range(0, WIDTH, CELL_SIZE):

                cell = Cell(x, y, CELL_SIZE, CELL_SIZE)
                row.append(cell)

            grid.append(row)

        return grid
    
    def update(self):
        if len(self.alive_cells) != 0:
            for cell in self.alive_cells:
                for pos in cell.neighbours:
                    row = pos[0]
                    col = pos[1]
                    neigh_cell = self.grid[row][col]
                    neigh_cell.alive_neighbours += 1

    
    def simulate(self, surface):
        self.update()

        for row in self.grid:
            for cell in row:

                if cell.alive == True and (cell.alive_neighbours == 2 or cell.alive_neighbours == 3):
                    pygame.draw.rect(surface, ALIVE_COLOUR, cell)
                    cell.reset_neighbours()

                elif cell.alive == True and (cell.alive_neighbours < 2 or cell.alive_neighbours > 3):
                    
                    cell.update()
                    cell.reset_neighbours()
                    pygame.draw.rect(surface, CELL_COLOUR, cell, 1)
                    self.alive_cells.remove(cell)
                    
                
                elif cell.alive == False and cell.alive_neighbours == 3:
                    cell.reset_neighbours()
                    cell.update()
                    self.alive_cells.append(cell)
                    pygame.draw.rect(surface, ALIVE_COLOUR, cell)

                elif cell.alive == False:
                    cell.reset_neighbours()


