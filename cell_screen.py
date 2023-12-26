import pygame, random

class CellScreen:
    INNER_CELL_WIDTH = 2
    CELL_WIDTH = INNER_CELL_WIDTH + 1

    def __init__(self, width, height):
        self.organisms = []
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((self.width_in_pixels(), self.height_in_pixels()), 0, 32)

    def width_in_pixels(self):
        return self.CELL_WIDTH * self.width

    def height_in_pixels(self):
        return self.CELL_WIDTH * self.height

    def clear(self):
        self.surface.fill((0, 0, 0))

    def random_x(self):
        return random.randint(0, self.width - 1)

    def random_y(self):
        return random.randint(0, self.height - 1)

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
