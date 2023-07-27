import random, hashlib

class Genome:
    def __init__(self):
        # 11 because a digest value can go up to 10, and 0..10 is 11 elements
        self.mapping = {i: random.choice(["up", "down", "left", "right"]) for i in range(11)}

    def direction(self, digest):
        return self.mapping[digest]

    def mutate(self):
        key_to_mutate = random.choice(list(self.mapping.keys()))
        self.mapping[key_to_mutate] = random.choice(["up", "down", "left", "right"])

    def color(self):
        # Convert the genome mapping to a string
        genome_string = str(self.mapping)

        # Hash the genome string into a hex value
        hash_object = hashlib.md5(genome_string.encode())
        hex_dig = hash_object.hexdigest()

        # Use the first 6 digits of the hex value to create an RGB color
        rgb = tuple(int(hex_dig[i:i+2], 16) for i in (0, 2, 4))
        
        return rgb
