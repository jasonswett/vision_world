from cell import Cell
from cell_search import CellSearch

class EyeCell(Cell):
    def digest(self, food_cells):
        total = 0
        checks = [
            CellSearch(food_cells, self.x, self.y, 0, -1).nearest_cell(),
            CellSearch(food_cells, self.y, self.x, 0, 1).nearest_cell(),
            CellSearch(food_cells, self.x, self.y, -1, 0).nearest_cell(),
            CellSearch(food_cells, self.y, self.x, 1, 0).nearest_cell()
        ]
        binary_string = "".join(["1" if check else "0" for check in checks])
        return int(binary_string, 2)
