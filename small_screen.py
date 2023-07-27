import pygame

BORDER_WIDTH = 2
BORDER_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 100

class SmallScreen:
    def __init__(self, surface, container_width, container_height):
        self.surface = surface
        self.container_width = container_width
        self.container_height = container_height

    def draw(self):
        pygame.draw.rect(
                self.surface,
                BORDER_COLOR,
                (self.left_edge_x() - SIZE - BORDER_WIDTH,
                 self.top_edge_y() - SIZE - BORDER_WIDTH,
                 SIZE + 2 * BORDER_WIDTH,
                 SIZE + 2 * BORDER_WIDTH))

        pygame.draw.rect(
                self.surface,
                BLACK,
                (self.left_edge_x() - SIZE,
                 self.top_edge_y() - SIZE,
                 SIZE,
                 SIZE))

    def draw_indicator(self, color):
        if color is None:
            color = BLACK

        pygame.draw.rect(
                self.surface,
                color,
                (self.left_edge_x() - SIZE,
                 self.top_edge_y() - SIZE,
                 SIZE,
                 SIZE))

    def left_edge_x(self):
        return self.container_width

    def top_edge_y(self):
        return self.container_height
