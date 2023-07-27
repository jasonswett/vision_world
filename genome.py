import random, hashlib

GENOME_LENGTH = 16

class Genome:
    def __init__(self):
        self.mapping = {i: random.choice(["up", "down", "left", "right", "same", "same", "same", "same"]) for i in range(GENOME_LENGTH + 1)}
        self.last_direction = None

    def direction(self, digest):
        next_direction = self.mapping[digest]

        if next_direction == "same":
            # If the last direction is None, we cannot continue in the same direction.
            # So we select a new random direction
            if self.last_direction is None:
                next_direction = random.choice(["up", "down", "left", "right"])
            else:
                next_direction = self.last_direction

        self.last_direction = next_direction
        return next_direction

    def mutate(self):
        key_to_mutate = random.choice(list(self.mapping.keys()))
        self.mapping[key_to_mutate] = random.choice(["up", "down", "left", "right", "same"])

    def color(self):
        # Convert the genome mapping to a string
        genome_string = str(self.mapping)

        # Hash the genome string into a hex value
        hash_object = hashlib.md5(genome_string.encode())
        hex_dig = hash_object.hexdigest()

        # Use the first 6 digits of the hex value to create an RGB color
        rgb = tuple(int(hex_dig[i:i+2], 16) for i in (0, 2, 4))
        
        return rgb
