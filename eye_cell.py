from cell import Cell
from cell_search import CellSearch

MAX_DISTANCE_TO_LOOK = 10

class EyeCell(Cell):
    def digest(self, cells):
        total = 0
        checks = [
            CellSearch(cells, self.x, self.y, -1, MAX_DISTANCE_TO_LOOK, True).nearest_cell(),
            CellSearch(cells, self.y, self.x, 1, MAX_DISTANCE_TO_LOOK, False).nearest_cell(),
            CellSearch(cells, self.x, self.y, 1, MAX_DISTANCE_TO_LOOK, True).nearest_cell(),
            CellSearch(cells, self.y, self.x, -1, MAX_DISTANCE_TO_LOOK, False).nearest_cell()
        ]
        binary_string = "".join(["1" if check else "0" for check in checks])
        return int(binary_string, 2)
