TUPLES = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

class Move:
    def tuple(self, direction):
        return TUPLES[direction]