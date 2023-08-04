from cell import Cell
from generation import Generation

class Ecosystem:
    def __init__(self, cell_screen):
        self.cell_screen = cell_screen
        self.food_cells = self.starting_food_cells()
        self.organisms = Generation([], self.cell_screen).offspring()

    def eatable_food_cell(self, organism):
        for cell in organism.cells:
            for food_cell in self.food_cells:
                if food_cell.x == cell.x and food_cell.y == cell.y:
                    return food_cell
        return None

    def starting_food_cells(self, number_of_cells=400):
        cells = []

        for _ in range(number_of_cells):
            x = self.cell_screen.random_x()
            y = self.cell_screen.random_y()
            cells.append(Cell(x, y, (0, 127, 0)))

        return cells

    def offer_food_to(self, organism):
        food_cell = self.eatable_food_cell(organism)
        if food_cell:
            organism.nourish()
            self.food_cells.remove(food_cell)

    def kill_unhealthy_organisms(self, organisms):
        for organism in organisms.copy():
            if organism.health == 0:
                organisms.remove(organism)
