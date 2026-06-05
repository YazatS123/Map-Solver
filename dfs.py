from funcs import *


"""
WHAT TO DO (for personal reference)
create a 2-way df that treats grid as a map with connected nodes
code a recursive function to navigate through said df
figure out a way to display said navigation (?)
"""

"""
okay so i am washed and sleepy and got stuck on step 2 so im gonna see if i can pseudocode a dfs given a 2-way df that was coded when i was less sleepy
figure out what the starting and ending nodes are
function search:
    add that index to some sort of log
    go to that index in the 2-way df
    call search on all elements in the element
    when u hit the ending node return that so the cycle breaks

wow maybe im less washed than i thought
hm still too tired to impl tho thats a problem for tomorrow 
oh also i still need to figure out how ts is gonna get displayed... maybe log what direction ur moving towards when doing log? also how about backtracking
eh problems for tmr
"""
log = []
grid = []
df = []
def search(linear):
    global log
    log.append(delinearize(grid, linear))
    delin = delinearize(grid, linear)
    if grid[delin[0]][delin[1]] == '#': return linear
    if len(df[linear]) == 0: return -1
    for coord in df[linear]:
        ans = search(linear)
        if ans >= 0: return ans
    return -1

def dfs(gr):
    global grid
    grid = gr
    global df
    df = generate_df(grid)
    start = -1
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '/': start = linearize(grid, x, y)
    if start >= 0: search(start)
    else: print("no starting pos found?????")
    if len(log) == 0: print("Blank log??")
    for step in log:
        print(step)