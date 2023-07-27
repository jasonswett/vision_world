import random

class Genome:
    def __init__(self):
        # 11 because a digest value can go up to 10, and 0..10 is 11 elements
        self.mapping = {i: random.choice(["up", "down", "left", "right"]) for i in range(11)}
