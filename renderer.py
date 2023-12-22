import pygame

class Renderer:
    GENERATION_COUNT_FONT_SIZE = 36

    def __init__(self, cell_screen):
        self.cell_screen = cell_screen

    def draw_organism(self, organism):
        for cell in organism.cells:
            self.draw_cell(cell)

    def draw_cell(self, cell):
        x_position = cell.x * self.cell_screen.CELL_WIDTH
        y_position = cell.y * self.cell_screen.CELL_WIDTH
        pygame.draw.rect(self.cell_screen.surface, cell.color, (x_position, y_position, self.cell_screen.INNER_CELL_WIDTH, self.cell_screen.INNER_CELL_WIDTH), 0)

    def draw_labels(self, generation_count, max_fitness):
        font = pygame.font.Font(None, self.GENERATION_COUNT_FONT_SIZE)
        text = font.render(f'Generation: {generation_count} Fittest Organism Fitness: {max_fitness}', True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.bottomright = self.cell_screen.surface.get_rect().bottomright
        self.cell_screen.surface.blit(text, text_rect)
