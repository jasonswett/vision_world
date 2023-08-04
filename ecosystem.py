from cell import Cell

class Ecosystem:
    def __init__(self, cell_screen):
        self.cell_screen = cell_screen
        self.food_cells = self.starting_food_cells()

    def eatable_food_cell(self, organism, food_cells):
        for cell in organism.cells:
            for food_cell in food_cells:
                if food_cell.x == cell.x and food_cell.y == cell.y:
                    return food_cell
        return None

    def starting_food_cells(self, square_size=32):
        cells = []

        top_left_x = (self.cell_screen.width - square_size) // 2
        top_left_y = (self.cell_screen.height - square_size) // 2
        bottom_right_x = top_left_x + square_size
        bottom_right_y = top_left_y + square_size

        for x in range(top_left_x, bottom_right_x):
            for y in range(top_left_y, bottom_right_y):
                cells.append(Cell(x, y, (0, 127, 0)))

        return cells
