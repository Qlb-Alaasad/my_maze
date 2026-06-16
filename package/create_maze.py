import random



class Cell():

    def __init__(self, north=True, south=True, east=True, west=True):
        self.north = north
        self.south = south
        self.east = east
        self.west = west



def Imperfect(maze, maze_config):
    """
    This function is used so that, in case it is not perfect, it increases the number of methods.
    """
    num_removals = (maze_config.width * maze_config.height) // 20
    for i in range(num_removals):
        y = random.randint(0, maze_config.height - 1)
        x = random.randint(0, maze_config.width - 1)
        direction = random.randint(0, 3)
        if direction == 0 and y > 0: 
            maze[y][x].north = False
            maze[y-1][x].south = False
        elif direction == 1 and x < maze_config.width - 1: 
            maze[y][x].east = False
            maze[y][x+1].west = False
    return maze
        
            
def create_maze(maze_config):
    """
    A function to build a maze in the form of a list inside 
    a 2D list inside an object in four directions, and see which direction is open
    """
    
    # This is regarding the issue of Mr. [Name], whether he exists or not. 
    if maze_config.seed is not None:
        random.seed(maze_config.seed)
    maze: list[list[Cell]]= []
    row: list[Cell] = []
    # This is to ensure all elements are in order to clear the path later.
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
        if not maze_config.perfect:
            maze = Imperfect(maze, maze_config)  
    return maze


