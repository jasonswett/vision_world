import pygame, random

INNER_CELL_WIDTH = 6
CELL_WIDTH = INNER_CELL_WIDTH + 2

class CellScreen:
    def __init__(self, width, height):
        self.organisms = []

        self.width = width
        self.height = height

        width_in_pixels = CELL_WIDTH * width
        height_in_pixels = CELL_WIDTH * height
        self.display = pygame.display.set_mode((width_in_pixels, height_in_pixels), 0, 32)

    def clear(self):
        self.display.fill((0, 0, 0))

    def draw_cell(self, cell):
        x_position = cell.x * CELL_WIDTH
        y_position = cell.y * CELL_WIDTH
        pygame.draw.rect(self.display, cell.color, (x_position, y_position, INNER_CELL_WIDTH, INNER_CELL_WIDTH), 0)

    def random_x(self):
        return random.randint(0, self.width - 1)

    def random_y(self):
        return random.randint(0, self.height - 1)

    def wrapped_x(self, x):
        if x >= self.width:
            return x - self.width
        elif x < 0:
            return x + self.width
        else:
            return x

    def wrapped_y(self, y):
        if y >= self.height:
            return y - self.height
        elif y < 0:
            return y + self.height
        else:
            return y

    def space_available(self, cell):
        if cell.y < 0:
            return False
        if cell.x < 0:
            return False
        if cell.y >= self.height:
            return False
        if cell.x >= self.width:
            return False

        for other_cell in self.other_cells():
            if cell.occupies_same_space_as(other_cell):
                return False

        return True
