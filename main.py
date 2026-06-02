import pygame
import random
from pathlib import Path

# Goal - take a random map from the map files and display

# Navigate to maps folder
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


# Visualize grid
pygame.init()
window = pygame.display.set_mode((len(grid[0]) * 40, len(grid) * 40))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 255))
    y = 0
    for row in grid:
        x = 0
        for char in row:
            color = pygame.Color(0, 0, 0)
            match char:
                case '.':
                    color = pygame.Color(0, 0, 0)
                case '_':
                    color = pygame.Color(255, 255, 255)
                case '#':
                    color = pygame.Color(0, 255, 0)
                case '/':
                    color = pygame.Color(255, 0, 255)
            pygame.draw.rect(window, color, (x, y, 40, 40))
            x += 40
        y += 40
    pygame.display.flip()