import pygame, random

from move import Move
from cell_screen import CellScreen
from cell import Cell
from organism import Organism
from small_screen import SmallScreen

def main():
    SCREEN_WIDTH_IN_CELLS = 100
    SCREEN_HEIGHT_IN_CELLS = int(SCREEN_WIDTH_IN_CELLS * 0.618)
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH_IN_CELLS, SCREEN_HEIGHT_IN_CELLS)

    food_cells = random_cells(cell_screen, 50)
    johnny = Organism(cell_screen.random_x(), cell_screen.random_y())
    clock = pygame.time.Clock()

    counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        counter += 1
        if counter % 10 == 0:
            johnny.move(food_cells)

        cell_screen.clear()

        for cell in food_cells:
            cell_screen.draw_cell(cell)

        cell_screen.draw_organism(johnny)
        small_screen = SmallScreen(cell_screen.surface, cell_screen.width_in_pixels(), cell_screen.height_in_pixels())
        small_screen.draw()
        small_screen.draw_indicator(johnny.cells[0].north_color(food_cells), 1, 0)
        small_screen.draw_indicator(johnny.cells[0].south_color(food_cells), 1, 2)
        small_screen.draw_indicator(johnny.cells[0].east_color(food_cells), 2, 1)
        small_screen.draw_indicator(johnny.cells[0].west_color(food_cells), 0, 1)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def random_cells(cell_screen, num_cells):
    cells = []
    for _ in range(num_cells):
        x = cell_screen.random_x()
        y = cell_screen.random_y()
        cell = Cell(x, y, (0, 255, 0))
        cells.append(cell)
    return cells

main()
