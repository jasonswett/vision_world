TUPLES = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

class Move:
    def __init__(self, starting_coordinates, bounds_width, bounds_height):
        self.starting_coordinates = starting_coordinates
        self.bounds_width = bounds_width
        self.bounds_height = bounds_height

    def coordinates(self, direction):
        delta = TUPLES[direction]
        new_x = self.wrapped_x(self.starting_coordinates[0] + delta[0])
        new_y = self.wrapped_y(self.starting_coordinates[1] + delta[1])
        return (new_x, new_y)

    def wrapped_x(self, x):
        if x >= self.bounds_width:
            return x - self.bounds_width
        elif x < 0:
            return x + self.bounds_width
        else:
            return x

    def wrapped_y(self, y):
        if y >= self.bounds_height:
            return y - self.bounds_height
        elif y < 0:
            return y + self.bounds_height
        else:
            return y
