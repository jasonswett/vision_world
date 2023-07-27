import pygame

class SmallScreen:
    def __init__(self, cell_screen):
        self.cell_screen = cell_screen

    def draw(self):
        border_width = 2
        small_screen_size = 100
        small_screen_color = (0, 0, 0)
        border_color = (255, 255, 255)

        pygame.draw.rect(
                self.cell_screen.surface,
                border_color,
                (self.cell_screen.width_in_pixels() - small_screen_size - border_width,
                 self.cell_screen.height_in_pixels() - small_screen_size - border_width,
                 small_screen_size + 2*border_width,
                 small_screen_size + 2*border_width))

        pygame.draw.rect(
                self.cell_screen.surface,
                small_screen_color,
                (self.cell_screen.width_in_pixels() - small_screen_size,
                 self.cell_screen.height_in_pixels() - small_screen_size,
                 small_screen_size,
                 small_screen_size))
