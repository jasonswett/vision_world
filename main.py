import pygame, random, time

from move import Move
from cell_screen import CellScreen
from cell import Cell
from organism import Organism
from generation import Generation

SCREEN_WIDTH_IN_CELLS = 140
FOOD_COUNT = 1000
REPRODUCTION_THRESHOLD = 10
REWARD_FOR_EATING = 50

def main():
    SCREEN_HEIGHT_IN_CELLS = int(SCREEN_WIDTH_IN_CELLS * 0.618)
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH_IN_CELLS, SCREEN_HEIGHT_IN_CELLS)

    food_cells = random_food_cells(cell_screen, FOOD_COUNT)
    organisms = Generation([], cell_screen).offspring()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    generation_game_loop_counter = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time.sleep(0.03)
        for organism in organisms:
            food_cell_eaten = organism.move(cell_screen.width, cell_screen.height, food_cells)
            if food_cell_eaten:
                organism.health += REWARD_FOR_EATING
                food_cells.remove(food_cell_eaten)
        reap(organisms)

        if len(organisms) <= REPRODUCTION_THRESHOLD:
            healthiest_organisms = organisms_ordered_by_health(organisms)[:4]
            improvements = [improvement(organism) for organism in healthiest_organisms]
            print("-------------------------------------")
            print(f"healthiest four: {improvements}")
            average_improvement = sum(improvements) / 4
            print(f"average improvement of healthiest four: {average_improvement}")
            organisms.extend(Generation(healthiest_organisms, cell_screen).offspring())
            food_cells.extend(random_food_cells(cell_screen, FOOD_COUNT - len(food_cells)))
            generation_game_loop_counter += 1

        if len(food_cells) <= 0:
            food_cells.extend(random_food_cells(cell_screen, FOOD_COUNT))

        cell_screen.clear()

        for cell in food_cells:
            cell_screen.draw_cell(cell)

        for organism in organisms:
            cell_screen.draw_organism(organism)

        draw_generation_count(cell_screen.surface, font, generation_game_loop_counter)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def improvement(organism):
    return (organism.health - Organism.STARTING_HEALTH)/REWARD_FOR_EATING

def organisms_ordered_by_health(organisms):
    return sorted(organisms, key=lambda organism: organism.health, reverse=True)

def random_food_cells(cell_screen, num_cells):
    cells = []
    for _ in range(num_cells):
        x = cell_screen.random_x()
        y = cell_screen.random_y()
        cell = Cell(x, y, (0, 127, 0))
        cells.append(cell)
    return cells

def reap(organisms):
    for organism in organisms.copy():
        if organism.health == 0:
            organisms.remove(organism)

def draw_generation_count(screen, font, generation_game_loop_counter):
    text = font.render(f'Generation: {generation_game_loop_counter}', True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.bottomright = screen.get_rect().bottomright
    screen.blit(text, text_rect)

main()
