import pygame

BORDER_WIDTH = 2
BORDER_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 100
GRID_SIZE = 3  # Number of cells per side of the grid
CELL_SIZE = SIZE // GRID_SIZE  # Size of each cell

class SmallScreen:
    def __init__(self, surface, container_width, container_height):
        self.surface = surface
        self.container_width = container_width
        self.container_height = container_height

    def draw(self):
        # Draw the outer border and black inside area
        pygame.draw.rect(self.surface, BORDER_COLOR, 
                         (self.left_edge_x() - SIZE - BORDER_WIDTH,
                          self.top_edge_y() - SIZE - BORDER_WIDTH,
                          SIZE + 2 * BORDER_WIDTH,
                          SIZE + 2 * BORDER_WIDTH))

        pygame.draw.rect(self.surface, BLACK,
                         (self.left_edge_x() - SIZE,
                          self.top_edge_y() - SIZE,
                          SIZE, SIZE))

    def draw_indicator(self, color, cell_x, cell_y):
        if color is None:
            color = BLACK

        # Define cell size, which is the third of the whole size (since we have a 3x3 grid)
        cell_size = SIZE // 3

        # Calculate the pixel position of the cell
        pixel_x = self.left_edge_x() - SIZE + cell_x * cell_size
        pixel_y = self.top_edge_y() - SIZE + cell_y * cell_size

        # Draw the indicator in the specified cell
        pygame.draw.rect(self.surface, color,
                         (pixel_x, pixel_y, cell_size, cell_size))

    def left_edge_x(self):
        return self.container_width

    def top_edge_y(self):
        return self.container_height
