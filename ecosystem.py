from cell import Cell
from generation import Generation

class Ecosystem:
    NUMBER_OF_ORGANISMS_ALLOWED_TO_REPRODUCE = 1
    REPRODUCTION_THRESHOLD = 4
    NUMBER_OF_FOOD_CELLS = 50

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

    def starting_food_cells(self):
        cells = []

        for _ in range(self.NUMBER_OF_FOOD_CELLS):
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
            if organism.health == 0 and len(organisms) > self.REPRODUCTION_THRESHOLD:
                organisms.remove(organism)

    def organisms_ordered_by_health(self):
        return sorted(self.organisms, key=lambda organism: organism.health, reverse=True)

    def healthiest_organisms(self):
        return self.organisms_ordered_by_health()[:self.NUMBER_OF_ORGANISMS_ALLOWED_TO_REPRODUCE]

    def healthiest_organism(self):
        return self.organisms_ordered_by_health()[0]

    def is_population_at_reproduction_threshold(self):
        return len(self.organisms) <= self.REPRODUCTION_THRESHOLD
