from cell import Cell
from cell_search import CellSearch

class EyeCell(Cell):
    def digest(self, food_cells):
        total = 0
        findings = [
            CellSearch(food_cells, self.x, self.y, 0, -1).nearest_cell(),
            CellSearch(food_cells, self.x, self.y, 0, 1).nearest_cell(),
            CellSearch(food_cells, self.x, self.y, -1, 0).nearest_cell(),
            CellSearch(food_cells, self.x, self.y, 1, 0).nearest_cell()
        ]
        binary_string = "".join(["1" if finding else "0" for finding in findings])
        return binary_string
