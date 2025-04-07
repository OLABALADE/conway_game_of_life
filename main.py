
import pygame
from constants import *
from game import Game

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOUR)
pygame.display.set_caption("Conway game of life")

game = Game()
simulating = False
running = True

while running:
    
    game.draw_grid(screen)

    if simulating:

        pygame.time.wait(500)
        game.simulate(screen)
        screen.fill(BG_COLOUR)
        game.draw_grid(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            row = pos[1] // CELL_SIZE
            col = pos[0] // CELL_SIZE

            if simulating != True:
                game.select_cell(screen, row, col)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                simulating = not simulating
            
            if event.key == pygame.K_r:

                simulating = False
                game.__init__()              
                screen.fill(BG_COLOUR)
            
                
    
    pygame.display.update()
    
