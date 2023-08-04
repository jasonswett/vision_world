import random, copy
from eye_cell import EyeCell
from genome import Genome
from move import Move

class Organism:
    MUTATION_RATE = 0.01
    STARTING_HEALTH = 40
    MAX_HEALTH = 40
    REWARD_FOR_EATING = 10

    def __init__(self, x, y, genome=None):
        if genome:
            self.genome = copy.deepcopy(genome)
            if random.random() < self.MUTATION_RATE:
                self.genome.mutate()
        else:
            self.genome = Genome()

        self.nourishments = 0
        self.health = self.STARTING_HEALTH
        self.eye_cell = EyeCell(x, y, self.genome.color())
        self.cells = [self.eye_cell]
        self.last_direction = None

    def move(self, bounds, food_cells):
        self.health -= 1
        digest = self.eye_cell.digest(food_cells)
        for cell in self.cells:
            cell.color = self.genome.color()
        for cell in self.cells:
            move = Move(cell.coordinates(), bounds)
            direction = self.genome.direction(digest)
            coordinates = move.coordinates(direction)
            cell.move_to(coordinates)
            self.last_direction = direction
        return coordinates

    def nourish(self):
        potential_health = self.health + self.REWARD_FOR_EATING
        self.health = min(potential_health, self.MAX_HEALTH)
        self.nourishments += 1
