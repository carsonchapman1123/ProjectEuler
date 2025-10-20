import math

"""
# Brute force solution for when I was trying to figure out explicit formula:

paths = []
def lattice_paths(grid_size, i, j):
    if i == grid_size and j == grid_size:
        paths.append(1)
        return
    if j < grid_size:
        lattice_paths(grid_size, i, j + 1)
    if i < grid_size:
        lattice_paths(grid_size, i + 1, j)

lattice_paths(3, 0, 0)
for i in range(2, 21):
    paths = []
    lattice_paths(i, 0, 0)
    print(i, len(paths))
"""


def lattice_paths(grid_size: int) -> int:
    """
    Calculates the number of paths through the lattice.
    We need to do grid_size moves right and grid_size moves down, so
    the formula is (2*grid_size choose grid_size) since we have 2 * grid_size
    moves and we need to choose grid_size of those to be right/down.
    """
    return math.factorial(2 * grid_size) // math.factorial(grid_size) ** 2


print(lattice_paths(20))
