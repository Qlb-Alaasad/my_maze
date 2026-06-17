import random


class Cell():
    def __init__(self, north=True, south=True, east=True, west=True):
        self.north = north # up with value 1
        self.south = south # done with value 2
        self.east = east # rite
        self.west = west # left


def Imperfect(maze, maze_config):
    """
    This function is used so that, in case it is not perfect
    it increases the number of methods.

    made by aabtah
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
    a 2D list inside an object in four directions,
    and see which direction is open

    made by aabtah
    """

    # This is regarding the seed and if it included, will buld with seed
    if maze_config.seed is not None:
        random.seed(maze_config.seed)

    # start hear
    maze: list[list[Cell]]= []
    row: list[Cell] = []

    # This is to ensure all elements are in order to clear the path later.
    for i in range(maze_config.width):
        for j in range(maze_config.height):
            row.append(Cell())
        maze.append(row)
        row = []
    entry_x, entry_y = maze_config.entry
    need_open = []
    need_open = [[False] * maze_config.width for _ in range(maze_config.height)]

#    need_open = make_42_pattern(maze_config)
    need_open[entry_y][entry_x] = True # start up

    stack = [(entry_x, entry_y)]

    while stack:
        x, y = stack[-1]
        not_open = []
        new_y = y - 1
        if new_y >= 0 and not need_open[new_y][x]:
            not_open.append((x, new_y, 0))
        new_x = x + 1
        if new_x < maze_config.width and not need_open[y][new_x]:
            not_open.append((new_x, y, 1))
        new_y = y + 1
        if new_y < maze_config.height and not need_open[new_y][x]:
            not_open.append((x, new_y, 2))
        new_x = x - 1
        if new_x >= 0 and not need_open[y][new_x]:
            not_open.append((new_x, y, 3))

        if not_open:
            new_x, new_y, go_site = random.choice(not_open)
            if go_site == 0:
                maze[y][x].north = False
                maze[new_y][new_x].south = False
            elif go_site == 1:
                maze[y][x].east = False
                maze[new_y][new_x].west = False
            elif go_site == 2:
                maze[y][x].south = False
                maze[new_y][new_x].north = False
            elif go_site == 3:
                maze[y][x].west = False
                maze[new_y][new_x].east = False
            need_open[new_y][new_x] = True
            stack.append((new_x, new_y))         
        else:
            stack.pop()
        if not maze_config.perfect:
            maze = Imperfect(maze, maze_config)  
    return maze
