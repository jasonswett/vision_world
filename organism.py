from eye_cell import EyeCell
from genome import Genome
from move import Move

class Organism:
    def __init__(self, x, y):
        self.health = 30
        self.eye_cell = EyeCell(x, y, (255, 0, 255))
        self.cells = [self.eye_cell]
        self.genome = Genome()

    def move(self, food_cells):
        digest = self.eye_cell.digest(food_cells)
        dx, dy = Move().tuple(self.genome.direction(digest))
        for cell in self.cells:
            cell.move(dx, dy)
        for cell in self.cells:
            for food_cell in food_cells:
                if food_cell.x == cell.x and food_cell.y == cell.y:
                    return food_cell

    def age(self):
        self.health -= 1
