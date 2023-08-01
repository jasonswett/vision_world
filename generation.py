import random
from organism import Organism

GENERATION_SIZE = 20

class Generation:
    def __init__(self, parent_organisms, cell_screen):
        self.parent_organisms = parent_organisms
        self.cell_screen = cell_screen

    def offspring(self):
        organisms = []
        for _ in range(GENERATION_SIZE):
            x = random.randint(self.cell_screen.width//2, 3*self.cell_screen.width//4)  # Adjust the x-coordinate within the 50%-75% range
            y = self.cell_screen.random_y()
            organism = Organism(x, y, self.random_parent_organism_genome())
            organisms.append(organism)
        return organisms

    def random_parent_organism_genome(self):
        if not self.parent_organisms:
            return None

        return random.choice(self.parent_organisms).genome
