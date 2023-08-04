import pygame, random, math, time

from move import Move
from cell_screen import CellScreen
from cell import Cell
from organism import Organism
from generation import Generation
from ecosystem import Ecosystem

SCREEN_WIDTH_IN_CELLS = 140
REPRODUCTION_THRESHOLD = 15
NUMBER_OF_ORGANISMS_ALLOWED_TO_REPRODUCE = 4
SLOWDOWN_DELAY = 0.01

def main():
    SCREEN_HEIGHT_IN_CELLS = int(SCREEN_WIDTH_IN_CELLS * 0.618)
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH_IN_CELLS, SCREEN_HEIGHT_IN_CELLS)

    ecosystem = Ecosystem(cell_screen)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    generation_game_loop_counter = 1
    pygame.event.get()

    while True:
        time.sleep(SLOWDOWN_DELAY)

        for organism in ecosystem.organisms:
            organism.move((cell_screen.width, cell_screen.height), ecosystem.food_cells)
            ecosystem.offer_food_to(organism)
            ecosystem.kill_unhealthy_organisms(ecosystem.organisms)

        if is_population_at_reproduction_threshold(ecosystem.organisms):
            healthiest_organisms = organisms_ordered_by_health(ecosystem.organisms)[:NUMBER_OF_ORGANISMS_ALLOWED_TO_REPRODUCE]
            ecosystem.organisms.extend(Generation(healthiest_organisms, cell_screen).offspring())
            ecosystem.food_cells.clear()
            ecosystem.food_cells.extend(ecosystem.starting_food_cells())
            generation_game_loop_counter += 1

        cell_screen.clear()

        for cell in ecosystem.food_cells:
            cell_screen.draw_cell(cell)

        for organism in ecosystem.organisms:
            cell_screen.draw_organism(organism)

        draw_generation_count(cell_screen.surface, font, generation_game_loop_counter)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def improvement(organism):
    return (organism.health - Organism.STARTING_HEALTH)/Organism.REWARD_FOR_EATING

def organisms_ordered_by_health(organisms):
    return sorted(organisms, key=lambda organism: organism.health, reverse=True)

def draw_generation_count(screen, font, generation_game_loop_counter):
    text = font.render(f'Generation: {generation_game_loop_counter}', True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.bottomright = screen.get_rect().bottomright
    screen.blit(text, text_rect)

def is_population_at_reproduction_threshold(organisms):
    return len(organisms) <= REPRODUCTION_THRESHOLD

main()
