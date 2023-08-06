import pygame, random, math, time

from move import Move
from cell_screen import CellScreen
from cell import Cell
from organism import Organism
from generation import Generation
from ecosystem import Ecosystem
from generation_count import GenerationCount

SCREEN_WIDTH_IN_CELLS = 140
SLOWDOWN_DELAY = 0.01
FRAME_RATE = 60

def main():
    SCREEN_HEIGHT_IN_CELLS = int(SCREEN_WIDTH_IN_CELLS * 0.618)
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH_IN_CELLS, SCREEN_HEIGHT_IN_CELLS)

    ecosystem = Ecosystem(cell_screen)
    clock = pygame.time.Clock()

    generation_game_loop_counter = 1
    pygame.event.get()

    while True:
        time.sleep(SLOWDOWN_DELAY)

        for organism in ecosystem.organisms:
            organism.move((cell_screen.width, cell_screen.height), ecosystem.food_cells)
            ecosystem.offer_food_to(organism)
            ecosystem.kill_unhealthy_organisms(ecosystem.organisms)

        if ecosystem.is_population_at_reproduction_threshold():
            ecosystem.organisms = Generation(ecosystem.healthiest_organisms(), cell_screen).offspring()
            ecosystem.food_cells = ecosystem.starting_food_cells()
            generation_game_loop_counter += 1

        cell_screen.clear()

        for cell in ecosystem.food_cells:
            cell_screen.draw_cell(cell)

        for organism in ecosystem.organisms:
            cell_screen.draw_organism(organism)

        GenerationCount(cell_screen.surface, generation_game_loop_counter).draw()

        pygame.display.update()
        clock.tick(FRAME_RATE)

    pygame.quit()

main()
