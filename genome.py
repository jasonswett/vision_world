import random

class Genome:
    def __init__(self):
        self.mapping = {i: random.choice(["up", "down", "left", "right"]) for i in range(9)}
