import random
from organism import Organism

GENERATION_SIZE = 40

class Generation:
    def __init__(self, parent_organisms, cell_screen):
        self.parent_organisms = parent_organisms
        self.cell_screen = cell_screen

    def offspring(self):
        organisms = []
        for _ in range(GENERATION_SIZE):
            x = random.randint(0, 40)
            y = random.randint(0, 40)
            organism = Organism(x, y, self.random_parent_organism_genome())
            organisms.append(organism)
        return organisms

    def random_parent_organism_genome(self):
        if not self.parent_organisms:
            return None

        return random.choice(self.parent_organisms).genome
