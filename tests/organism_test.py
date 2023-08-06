import pytest
from vision_world.organism import Organism

def test_move():
    organism = Organism(0, 0)
    bounds_width = 140
    bounds_height = 100
    food_cells = []

    initial_health = organism.health
    organism.move((bounds_width, bounds_height), food_cells)
    assert organism.health == initial_health - 1
