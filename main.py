import pygame, random, math, time

from move import Move
from cell_screen import CellScreen
from cell import Cell
from organism import Organism
from generation import Generation
from ecosystem import Ecosystem
from renderer import Renderer

SCREEN_WIDTH_IN_CELLS = 300
SLOWDOWN_DELAY = 0.01
FRAME_RATE = 60

def main():
    SCREEN_HEIGHT_IN_CELLS = int(SCREEN_WIDTH_IN_CELLS * 0.618)
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH_IN_CELLS, SCREEN_HEIGHT_IN_CELLS)
    renderer = Renderer(cell_screen)

    ecosystem = Ecosystem(cell_screen)
    clock = pygame.time.Clock()

    generation_count = 1
    max_fitness_of_last_generation = None
    pygame.event.get()

    while True:
        time.sleep(SLOWDOWN_DELAY)

        for organism in ecosystem.organisms:
            organism.move((cell_screen.width, cell_screen.height), ecosystem.food_cells)
            ecosystem.offer_food_to(organism)

        ecosystem.kill_unhealthy_organisms(ecosystem.organisms)

        if ecosystem.is_population_at_reproduction_threshold() and ecosystem.healthiest_organism().health <= 0:
            print('----')
            initial_food_count = Ecosystem.NUMBER_OF_FOOD_CELLS
            remaining_food_count = len(ecosystem.food_cells)
            food_eaten_count = initial_food_count - remaining_food_count
            percentage_eaten = (food_eaten_count / initial_food_count) * 100
            print(f'Percentage of food eaten: {percentage_eaten:.2f}')

            max_fitness_of_last_generation = ecosystem.healthiest_organism().fitness
            ecosystem.organisms = Generation(ecosystem.healthiest_organisms(), cell_screen).offspring()
            ecosystem.food_cells = ecosystem.starting_food_cells()
            generation_count += 1

        cell_screen.clear()

        for cell in ecosystem.food_cells:
            renderer.draw_cell(cell)

        for organism in ecosystem.organisms:
            renderer.draw_organism(organism)

        renderer.draw_labels(generation_count, max_fitness_of_last_generation)

        pygame.display.update()
        clock.tick(FRAME_RATE)

    pygame.quit()

main()
