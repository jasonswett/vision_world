import pygame, random

from move import Move
from cell_screen import CellScreen
from cell import Cell
from organism import Organism

def main():
    SCREEN_WIDTH_IN_CELLS = 100
    SCREEN_HEIGHT_IN_CELLS = int(SCREEN_WIDTH_IN_CELLS * 0.618)
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH_IN_CELLS, SCREEN_HEIGHT_IN_CELLS)

    food_cells = random_food_cells(cell_screen, 50)
    organisms = random_organisms(cell_screen, 10)
    clock = pygame.time.Clock()

    counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        counter += 1
        if counter % 10 == 0:
            for organism in organisms:
                organism.move(food_cells)

        cell_screen.clear()

        for cell in food_cells:
            cell_screen.draw_cell(cell)

        for organism in organisms:
            cell_screen.draw_organism(organism)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def random_organisms(cell_screen, count):
    organisms = []
    for _ in range(count):
        organisms.append(Organism(cell_screen.random_x(), cell_screen.random_y()))
    return organisms

def random_food_cells(cell_screen, num_cells):
    cells = []
    for _ in range(num_cells):
        x = cell_screen.random_x()
        y = cell_screen.random_y()
        cell = Cell(x, y, (0, 255, 0))
        cells.append(cell)
    return cells

main()
