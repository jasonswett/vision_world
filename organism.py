import random, copy
from eye_cell import EyeCell
from genome import Genome
from move import Move

MUTATION_RATE = 0.01

class Organism:
    def __init__(self, x, y, genome=None):
        if genome:
            self.genome = copy.deepcopy(genome)
            if random.random() < MUTATION_RATE:
                self.genome.mutate()
        else:
            print("making fresh genome")
            self.genome = Genome()

        self.health = 100
        self.eye_cell = EyeCell(x, y, self.genome.color())
        self.cells = [self.eye_cell]
        self.last_direction = None

    def move(self, bounds_width, bounds_height, food_cells):
        self.health -= 1
        digest = self.eye_cell.digest(food_cells)
        for cell in self.cells:
            cell.color = self.genome.color()
        for cell in self.cells:
            move = Move(cell.coordinates(), bounds_width, bounds_height)
            direction = self.genome.direction(digest)
            coordinates = move.coordinates(direction)
            cell.move_to(coordinates)
            self.last_direction = direction
        for cell in self.cells:
            for food_cell in food_cells:
                if food_cell.x == cell.x and food_cell.y == cell.y:
                    return food_cell

    def age(self):
        self.health -= 1
