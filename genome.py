import random, hashlib
from cell_search import CellSearch

DIRECTIONS = ["up", "down", "left", "right", "same", "same", "same", "same"]

class Genome:
    def __init__(self):
        self.rules = {}
        self.last_direction = None

    def __str__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.rules.items())

    def direction(self, digest):
        key = f"{digest}/{self.last_direction}" if self.last_direction else digest

        if key not in self.rules:
            self.rules[key] = random.choice(DIRECTIONS)

        next_direction = self.rules[key]

        if next_direction == "same":
            if self.last_direction is None:
                next_direction = random.choice(["up", "down", "left", "right"])
            else:
                next_direction = self.last_direction

        self.last_direction = next_direction
        return next_direction

    def mutate(self):
        if not self.rules:
            return
        key_to_mutate = random.choice(list(self.rules.keys()))
        self.rules[key_to_mutate] = random.choice(DIRECTIONS)

    def color(self):
        # Convert the genome rules to a string
        genome_string = str(self.rules)

        # Hash the genome string into a hex value
        hash_object = hashlib.md5(genome_string.encode())
        hex_dig = hash_object.hexdigest()

        # Use the first 6 digits of the hex value to create an RGB color
        rgb = tuple(int(hex_dig[i:i+2], 16) for i in (0, 2, 4))
        
        return rgb
