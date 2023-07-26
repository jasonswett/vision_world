import pygame
from cell_screen import CellScreen
from cell import Cell

def main():
    SCREEN_WIDTH = 100
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.618)
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

    johnny = Cell(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, (255, 0, 0))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  # check for KEYDOWN events
                if event.key == pygame.K_LEFT:
                    johnny.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    johnny.move(1, 0)
                elif event.key == pygame.K_UP:
                    johnny.move(0, -1)
                elif event.key == pygame.K_DOWN:
                    johnny.move(0, 1)

        cell_screen.clear()
        cell_screen.draw_cell(johnny)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

main()
