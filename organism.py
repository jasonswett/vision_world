import random, copy
from eye_cell import EyeCell
from genome import Genome
from move import Move

class Organism:
    MUTATION_RATE = 0.01
    STARTING_HEALTH = 100

    def __init__(self, x, y, genome=None):
        if genome:
            self.genome = copy.deepcopy(genome)
            if random.random() < self.MUTATION_RATE:
                self.genome.mutate()
        else:
            print("making fresh genome")
            self.genome = Genome()

        self.health = self.STARTING_HEALTH
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
        return coordinates

    def age(self):
        self.health -= 1
