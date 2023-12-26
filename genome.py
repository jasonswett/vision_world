import random, hashlib
from cell_search import CellSearch

class Genome:
    BIAS_FOR_SAME_DIRECTION = 4
    DIRECTIONS = ["up", "right", "down", "left"] + (["same"] * BIAS_FOR_SAME_DIRECTION)
    PERCENTAGE_OF_GENES_TO_MUTATE = 0.01

    def __init__(self):
        self.rules = {}
        self.last_direction = None

    def __str__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.rules.items())

    def direction(self, digest):
        key = f"{digest}/{self.last_direction}" if self.last_direction else digest

        if key not in self.rules:
            self.rules[key] = random.choice(self.DIRECTIONS)

        next_direction = self.rules[key]

        if next_direction == "same":
            if self.last_direction is None:
                next_direction = random.choice(["up", "right", "down", "left"])
            else:
                next_direction = self.last_direction

        self.last_direction = next_direction
        return next_direction

    def mutate(self):
        if not self.rules:
            return

        number_of_genes_to_mutate = int(len(self.rules.keys()) * self.PERCENTAGE_OF_GENES_TO_MUTATE)
        keys_to_mutate = random.sample(list(self.rules.keys()), number_of_genes_to_mutate)
        
        for key in keys_to_mutate:
            self.rules[key] = random.choice(self.DIRECTIONS)

    def color(self):
        # Convert the genome rules to a string
        genome_string = str(self.rules)

        # Hash the genome string into a hex value
        hash_object = hashlib.md5(genome_string.encode())
        hex_dig = hash_object.hexdigest()

        # Use the first 6 digits of the hex value to create an RGB color
        rgb = tuple(int(hex_dig[i:i+2], 16) for i in (0, 2, 4))
        
        return rgb
