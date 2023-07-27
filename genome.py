import random

class Genome:
    def __init__(self):
        # 11 because a digest value can go up to 10, and 0..10 is 11 elements
        self.mapping = {i: random.choice(["up", "down", "left", "right"]) for i in range(11)}

    def direction(self, digest):
        return self.mapping[digest]

    def mutate(self):
        key_to_mutate = random.choice(list(self.mapping.keys()))
        self.mapping[key_to_mutate] = random.choice(["up", "down", "left", "right"])
