import pygame

class SmallScreen:
    def __init__(self, surface, container_width, container_height):
        self.surface = surface
        self.container_width = container_width
        self.container_height = container_height

    def draw(self):
        border_width = 2
        small_screen_size = 100
        small_screen_color = (0, 0, 0)
        border_color = (255, 255, 255)

        pygame.draw.rect(
                self.surface,
                border_color,
                (self.container_width - small_screen_size - border_width,
                 self.container_height - small_screen_size - border_width,
                 small_screen_size + 2*border_width,
                 small_screen_size + 2*border_width))

        pygame.draw.rect(
                self.surface,
                small_screen_color,
                (self.container_width - small_screen_size,
                 self.container_height - small_screen_size,
                 small_screen_size,
                 small_screen_size))
