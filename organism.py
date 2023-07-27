from eye_cell import EyeCell
from genome import Genome
from move import Move

class Organism:
    def __init__(self, x, y):
        self.health = 20
        self.eye_cell = EyeCell(x, y, (255, 0, 255))
        self.cells = [self.eye_cell]
        self.genome = Genome()

    def move(self, bounds_width, bounds_height, food_cells):
        digest = self.eye_cell.digest(food_cells)
        for cell in self.cells:
            move = Move(cell.coordinates(), bounds_width, bounds_height)
            coordinates = move.coordinates(self.genome.direction(digest))
            cell.move_to(coordinates)
        for cell in self.cells:
            for food_cell in food_cells:
                if food_cell.x == cell.x and food_cell.y == cell.y:
                    return food_cell

    def age(self):
        self.health -= 1
