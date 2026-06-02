# takes a grid coordinate and returns a linear index for adj[][]
def linearize(grid, x, y):
    return y * len(grid[0]) + x

# takes a linear index (typically from adj[][]) and returns a grid coordinate (figured if i have a linearize might be useful to have a delinearize too lol)
def delinearize(grid, lin):
    length = len(grid[0])
    x = lin % length
    y = (lin - x) / length
    return [x, y]

# gets all adjacent coordinates to a grid coordinate
def get_adjacent(grid, x, y):
    out = []
    length = len(grid[0])
    width = len(grid)
    if x % length != 0: out.append([x - 1, y])
    if x % length != length - 1: out.append([x + 1, y])
    if y != 0: out.append([x, y - 1])
    if y != width - 1: out.append([x, y + 1])
    return out

# takes a map as input and returns [[x, y], [x, y], adj[][]] (first coord start second coord end)
def generate_df(grid):
    df = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            adj = get_adjacent(grid, x, y)
            current_entry = []
            for coord in adj:
                if grid[coord[x]][coord[y]] != '.':
                    l = linearize(grid, x, y)
                    current_entry.append(l)
            df.append(current_entry)
    return df