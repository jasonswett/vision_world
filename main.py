import pygame, random

from move import Move
from cell_screen import CellScreen
from cell import Cell
from organism import Organism
from generation import Generation

SCREEN_WIDTH_IN_CELLS = 140
FOOD_COUNT = 1000
REPRODUCTION_THRESHOLD = 10
REWARD_FOR_EATING = 10

def main():
    SCREEN_HEIGHT_IN_CELLS = int(SCREEN_WIDTH_IN_CELLS * 0.618)
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH_IN_CELLS, SCREEN_HEIGHT_IN_CELLS)

    food_cells = random_food_cells(cell_screen, FOOD_COUNT)
    organisms = Generation([], cell_screen).offspring()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    counter = 0
    generation_counter = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        counter += 1
        if counter % 3 == 0:
            for organism in organisms:
                food_cell_eaten = organism.move(cell_screen.width, cell_screen.height, food_cells)
                if food_cell_eaten:
                    organism.health += REWARD_FOR_EATING
                    food_cells.remove(food_cell_eaten)
            generation_counter = reap(organisms, food_cells, cell_screen, generation_counter)

        cell_screen.clear()

        for cell in food_cells:
            cell_screen.draw_cell(cell)

        for organism in organisms:
            cell_screen.draw_organism(organism)

        draw_generation_count(cell_screen.surface, font, generation_counter)

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
        cell = Cell(x, y, (0, 127, 0))
        cells.append(cell)
    return cells

def reap(organisms, food_cells, cell_screen, generation_counter):
    for organism in organisms.copy():
        if organism.health == 0:
            organisms.remove(organism)
        if len(organisms) <= REPRODUCTION_THRESHOLD:
            organisms.extend(Generation(organisms, cell_screen).offspring())
            food_cells.extend(random_food_cells(cell_screen, FOOD_COUNT - len(food_cells)))
            generation_counter += 1
    return generation_counter

def draw_generation_count(screen, font, generation_counter):
    text = font.render(f'Generation: {generation_counter}', True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.bottomright = screen.get_rect().bottomright
    screen.blit(text, text_rect)

main()
