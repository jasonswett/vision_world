import pygame, time
from cell_screen import CellScreen
from cell import Cell

def main():
    SCREEN_WIDTH = 100
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.618)
    pygame.init()
    cell_screen = CellScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

    johnny = Cell(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, (255, 0, 0))
    cell_screen.draw_cell(johnny)
    pygame.display.update()
    time.sleep(20)

main()
