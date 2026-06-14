import random



class Cell():

    def __init__(self, north=True, south=True, east=True, west=True):
        self.north = north
        self.south = south
        self.east = east
        self.west = west




def create_maze(maze_config):
    if maze_config.seed is not None:
        random.seed(maze_config.seed)
    maze: list[list[Cell]]= []
    row: list[Cell] = []

    for i in range(maze_config.width):

        for j in range(maze_config.height):
            row.append(Cell())
        maze.append(row)
        row = []
    entry_x, entry_y = maze_config.entry
    open_maze = []
    open_maze = [[False] * maze_config.width for _ in range(maze_config.height)]
    open_maze[entry_y][entry_x] = True

    stack = [(entry_x, entry_y)]

    while stack:
        x, y = stack[-1]
        not_open = []
        ny = y - 1
        if ny >= 0 and not open_maze[ny][x]:
            not_open.append((x, ny, 0))
        nx = x + 1
        if nx < maze_config.width and not open_maze[y][nx]:
            not_open.append((nx, y, 1))
        ny = y + 1
        if ny < maze_config.height and not open_maze[ny][x]:
            not_open.append((x, ny, 2))
        nx = x - 1
        if nx >= 0 and not open_maze[y][nx]:
            not_open.append((nx, y, 3))

        if not_open:
            nx, ny, go_site = random.choice(not_open)
            if go_site == 0:
                maze[y][x].north = False
                maze[ny][nx].south = False
            elif go_site == 1:
                maze[y][x].east = False
                maze[ny][nx].west = False
            elif go_site == 2:
                maze[y][x].south = False
                maze[ny][nx].north = False
            elif go_site == 3:
                maze[y][x].west = False
                maze[ny][nx].east = False
            open_maze[ny][nx] = True
            stack.append((nx, ny))         
        else:
            stack.pop()        
    return maze
