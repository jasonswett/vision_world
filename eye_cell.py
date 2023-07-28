from cell import Cell
from cell_search import CellSearch

class EyeCell(Cell):
    def digest(self, food_cells):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        binary_distances = [
            format(
                CellSearch(food_cells, self.x, self.y, dx, dy).nearest_cell_distance() or CellSearch.MAX_DISTANCE_TO_LOOK,
                f'0{CellSearch.MAX_DISTANCE_TO_LOOK}b'
            )
            for dx, dy in directions
        ]
        return "".join(binary_distances)
