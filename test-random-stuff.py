import random
from pathlib import Path
from funcs import *


# uh this exists entirely so i can test funcs without cluttering the code i actually wanna advance
cwd = Path.cwd()
map_path = cwd / "Map Solver" / "maps"
maps = sum(1 for item in map_path.iterdir()) # Count number of maps
mapno = random.randint(1, maps)
map_to_open = "map" + str(mapno) + ".txt"
map_to_open_path = map_path / map_to_open

print(map_to_open)
# Build grid
grid = []
with open(map_to_open_path, "r") as file:
    content = file.read()
    l = ""
    for ch in content:
        if ch != '\n':
            l = l + ch
        else:
            grid.append(list(l))
            
            l = ""
    if len(l) > 0: grid.append(list(l))
print(grid)

for x in range(len(grid)):
    for y in range(len(grid[x])):
        out = "(" + str(x) + ", " + str(y) + ") - ["
        adj = get_adjacent(grid, x, y)
        for coord in adj:
            out += "(" + str(coord[0]) + ", " + str(coord[1]) + ", " + grid[coord[0]][coord[1]] + "), "
        print(out)
#test_df = generate_df(grid)
#print(test_df)