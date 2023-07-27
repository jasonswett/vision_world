from eye_cell import EyeCell
from genome import Genome
from move import Move

class Organism:
    def __init__(self, x, y):
        self.health = 10
        self.eye_cell = EyeCell(x, y, (255, 0, 0))
        self.cells = [self.eye_cell]
        self.genome = Genome()

    def move(self, food_cells):
        digest = self.eye_cell.digest(food_cells)
        move = self.genome.mapping[digest]
        dx, dy = Move().tuple(move)
        for cell in self.cells:
            cell.move(dx, dy)

    def age(self):
        self.health -= 1
